import streamlit as st
import requests

st.set_page_config(page_title="Wiserbond Report", layout="wide")
st.title("Wiserbond Macro Impact Synthesizer")

# 사용자 입력
st.markdown("#### This tool tells how a macro topic affects an industry in a country, explained in your preferred language.")
topic = st.text_input("Macro Topic - Type a macro topic and press Enter (ex, Inflation)", value="Inflation")
industry = st.text_input("Industry or Sector - Type an industry/sector and press Enter (ex, Supply Chain)", value="Supply Chain")

st.markdown("#### Optional - pro mode: if checked, the output should use more technical, domain-specific language tailored for professionals.")
is_pro = st.checkbox("Pro mode (I know this industry well)")

country = st.text_input("Country - Type a country and press Enter (ex, Canada)", value="Canada")
language = st.selectbox("Output Language", ["English", "한국어", "Español", "Chinese", "Hindi"])

# 내부 분석자 입력
with st.expander("🔒 Internal Analyst Comment (Developer Only)", expanded=False):
    internal_comment = st.text_area("Enter your interpretation or analyst comment", height=100)

# 사용자 분석&예측 입력
st.markdown("---")
st.subheader("Add Your Interpretation and Forecast")
st.markdown("Let us learn from you.")

with st.expander("✍️ Submit Your Forecast", expanded=False):
    email = st.text_input("Your Email (e.g., jamie@wiserbond.com)")
    user_analysis = st.text_area("Your Interpretation")
    user_forecast = st.text_area("Your Forecast (What will happen in 3 months?)")

if st.button("Submit"):
    if not email:
        st.warning("Please enter your email.")
    elif not user_analysis and not user_forecast:
        st.warning("Please provide either an interpretation or a forecast.")
    else:
        payload = {
            "email": email,
            "topic": topic,
            "industry": industry,
            "country": country,
            "user_analysis": user_analysis,
            "user_forecast": user_forecast,
        }

        try:
            res = requests.post("https://wiserbond-synthesizerv3.onrender.com/submit-feedback", json=payload)
            if res.status_code == 200:
                st.success("✅ Your input has been saved. Thank you!")
            else:
                try:
                    error_detail = res.json()
                except:
                    error_detail = res.text
                st.error(f"⚠️ Server responded with an error.\n\n{error_detail}")
        except Exception as e:
            st.error(f"❌ Error occurred while submitting: {e}")

# 보고서 생성 실행
st.markdown("---")
if st.button("Generate Report"):
    with st.spinner("Wiserbond is analyzing with AI..."):
        response = requests.post(
            "https://wiserbond-synthesizerv3.onrender.com/generate_report",
            json={
                "topic": topic,
                "industry": industry,
                "country": country,
                "language": language,
                "internal_comment": internal_comment,
                "user_forecast": user_forecast,
                "user_analysis": user_analysis,
                "is_pro": is_pro
            }
        )

        if response.status_code == 200:
            result = response.json()

            st.subheader("Executive Summary")
            st.write(result["executive_summary"])

            st.subheader("Big Picture")
            st.write(result["big_picture"])

            st.subheader("Mid Picture")
            st.write(result["mid_picture"])

            st.subheader("Small Picture")
            st.write(result["small_picture"])

            st.subheader("Wiserbond Interpretation")
            st.write(result["interpretation"])
        else:
            try:
                error_detail = response.json()
            except:
                error_detail = response.text
            st.error(f"API Error: Could not generate report.\n\n{error_detail}")
