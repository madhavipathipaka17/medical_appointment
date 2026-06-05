import streamlit as st

st.set_page_config(
    page_title="Medical Appointment Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Medical Appointment Analytics")

st.markdown("""
### Project Overview

This system helps healthcare providers:

✅ Predict patient no-shows

✅ Forecast appointment demand

✅ Visualize operational patterns

✅ Improve scheduling efficiency
""")

st.info(
    "Use the left sidebar to navigate through the application."
)