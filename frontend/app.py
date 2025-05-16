# frontend/app.py

import streamlit as st
import requests

st.set_page_config(page_title="Wiserbond Report", layout="wide")
st.title("Wiserbond Macro Impact Synthesizer")
# ✅ 사용자에게 자연어형 문장으로 질문 의도 전달
st.markdown(
    "#### This tool tells how a macro topic affects an industry in a country, explained in your preferred language."
)
# --- 사용자 입력 ---
topic = st.text_input("Macro Topic - Type a macro topic and press Enter (ex, Inflation)", value="Inflation")
industry = st.text_input("Industry or Sector - Type an industry/sector and press Enter (ex, Supply Chain)", value="Supply Chain")
country = st.text_input("Country - Type a country and press Enter (ex, Canada)", value="Canada")
language = st.selectbox("Output Language", ["English", "한국어", "Español", "Chinese", "Hindi"])

# --- 내부 분석자 입력 (개발자만 보게끔) ---
with st.expander("🔒 Internal Analyst Comment (Developer Only)", expanded=False):
    user_comment = st.text_area("Enter your interpretation or analyst comment", height=100)

# --- 실행 ---
if st.button("Generate Report"):
    with st.spinner("Analyzing with AI..."):
        response = requests.post(
            "http://localhost:8000/generate_report",  # FastAPI 서버 URL
            json={
                "topic": topic,
                "industry": industry,
                "country": country,
                "language": language,
                "user_comment": user_comment
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
            st.error("API Error: Could not generate report.")
