import streamlit as st

st.set_page_config(
    page_title="Hybrid Medical Diagnosis System",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🩺 Hybrid Medical Diagnosis Prediction System")
st.markdown("""
Welcome to the **Hybrid Medical Diagnosis Prediction System**.

### Use the sidebar to navigate:
- **Dashboard** → Understand how the system works
- **Predict** → Enter symptoms and get a disease prediction
""")

st.info("⚠️ This system is for educational and decision-support purposes only. It does not replace professional medical diagnosis.")
    