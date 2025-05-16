# frontend/admin.py

import streamlit as st
import requests
from config import BASE_API_URL

st.set_page_config(page_title="Wiserbond Internal Comment Editor", layout="wide")
st.title("🔒 Internal Analyst Comment (Admin Only)")

# --- Load current internal comment from backend ---
try:
    response = requests.get(f"{BASE_API_URL}/load_internal_comment")
    response.raise_for_status()
    current_comment = response.json().get("comment", "")
except Exception as e:
    st.error(f"Failed to load comment: {e}")
    current_comment = ""

# --- Text input for new comment ---
new_comment = st.text_area("✍️ Edit Internal Wiserbond Comment", value=current_comment, height=150)

# --- Save to backend ---
if st.button("💾 Save Comment"):
    try:
        response = requests.post(
            f"{BASE_API_URL}/save_internal_comment",
            json={"comment": new_comment}
        )
        response.raise_for_status()
        st.success("✅ Internal comment saved successfully!")
    except Exception as e:
        st.error(f"❌ Save failed: {e}")
