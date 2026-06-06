import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# -----------------------------
# Load model and encoders
# -----------------------------
model = joblib.load("../models/no_show_model.pkl")
specialty_encoder = joblib.load("../models/specialty_encoder.pkl")
place_encoder = joblib.load("../models/place_encoder.pkl")

st.title("🏥 Patient No-Show Prediction")

# -----------------------------
# User Inputs
# -----------------------------

age = st.number_input("Age", min_value=0, max_value=120, value=30)

gender = st.selectbox(
    "Gender",
    ["Female", "Male"]
)

appointment_date = st.date_input(
    "Appointment Date",
    value=datetime.today()
)

appointment_hour = st.slider(
    "Appointment Hour",
    min_value=0,
    max_value=23,
    value=10
)

specialty = st.selectbox(
    "Specialty",
    specialty_encoder.classes_
)

place = st.selectbox(
    "Place",
    place_encoder.classes_
)

hypertension = st.selectbox("Hypertension", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
alcoholism = st.selectbox("Alcoholism", [0, 1])
handcap = st.selectbox("Handicap", [0, 1])
scholarship = st.selectbox("Scholarship", [0, 1])
sms_received = st.selectbox("SMS Received", [0, 1])

# Weather inputs
average_temp_day = st.number_input(
    "Average Temperature",
    value=25.0
)

average_rain_day = st.number_input(
    "Average Rainfall",
    value=0.0
)



rainy_day_before = st.selectbox(
    "Rainy Day Before",
    [0, 1]
)



rain_intensity = st.selectbox(
    "Rain Intensity",
    [0, 1, 2, 3]
)

heat_intensity = st.selectbox(
    "Heat Intensity",
    [0, 1, 2, 3]
)

disability = st.selectbox(
    "Disability",
    [0, 1]
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict No-Show Risk"):

    # Derived features
    under_12_years_old = int(age < 12)

    over_60_years_old = int(age > 60)

    patient_needs_companion = int(
        age < 12 or age > 60
    )

    age_missing = 0

    appointment_year = appointment_date.year
    appointment_month = appointment_date.month
    appointment_day = appointment_date.day

    appointment_time = appointment_hour

    specialty_encoded = specialty_encoder.transform(
        [specialty]
    )[0]

    place_encoded = place_encoder.transform(
        [place]
    )[0]

    # Exact feature order used during training
    sample = pd.DataFrame({
    'appointment_time': [appointment_time],
    'gender': [1 if gender == "Male" else 0],
    'disability': [disability],
    'age': [age],
    'under_12_years_old': [under_12_years_old],
    'over_60_years_old': [over_60_years_old],
    'patient_needs_companion': [patient_needs_companion],
    'average_temp_day': [average_temp_day],
    'average_rain_day': [average_rain_day],
    'rainy_day_before': [rainy_day_before],
    'rain_intensity': [rain_intensity],
    'heat_intensity': [heat_intensity],
    'Hipertension': [hypertension],
    'Diabetes': [diabetes],
    'Alcoholism': [alcoholism],
    'Handcap': [handcap],
    'Scholarship': [scholarship],
    'SMS_received': [sms_received],
    'age_missing': [age_missing],
    'appointment_year': [appointment_year],
    'appointment_month': [appointment_month],
    'appointment_day': [appointment_day],
    'appointment_hour': [appointment_hour],
    'specialty_encoded': [specialty_encoded],
    'place_encoded': [place_encoded]
})
        

    probability = model.predict_proba(sample)[0][1]

    st.subheader("Prediction Result")

    st.metric(
        "No-Show Risk",
        f"{probability:.1%}"
    )

    if probability >= 0.5:
        st.error("⚠️ High Risk of No-Show")
    else:
        st.success("✅ Likely to Attend")