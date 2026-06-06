import streamlit as st

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 Analytics Dashboard")

st.markdown("## 🔍 Key Business Insights")




st.subheader("🚫 1.No-Show Prediction")

st.markdown("""
    - Specialty is the strongest driver of no-show behavior.
                
    - Young adults exhibit the highest no-show rates (~47%).
                
    - SMS reminders show minimal impact on attendance.
                
    - Certain locations consistently experience higher no-show rates.
    """)


st.subheader("📈 2.Demand Forecasting")

st.markdown("""
    - Specialty mix is the primary driver of appointment demand.
                
    - Thursday records the highest average demand.
                
    - Demand distribution is highly skewed, with occasional extreme spikes.
                
    - Weather variables contribute minimal forecasting value.
    """)
st.title("👩‍💻 Creator of this Project")
st.subheader("Developed by:")
st.markdown("***Madhavi Pathipaka***")

st.markdown("### 🛠 Skills:")
st.markdown("Python, Pandas, Data Analysis,Machine learning, Streamlit")