import streamlit as st
import pandas as pd
import joblib
from datetime import datetime
import numpy as np

# -----------------------------
# Load model and encoders
# -----------------------------
model = joblib.load("../models/no_show_model.pkl")
specialty_encoder = joblib.load("../models/specialty_encoder.pkl")
place_encoder = joblib.load("../models/place_encoder.pkl")

st.title("🏥 Patient No-Show Prediction")

# -----------------------------
# UI INPUTS (Human Friendly Only)
# -----------------------------

age = st.slider("Age", min_value=0, max_value=120, value=30)

gender = st.selectbox("Gender", ["Female", "Male"])

disability = st.selectbox("Disability", ['intellectual' ,'motor','other','none'])
hypertension = st.selectbox("Hypertension", ["yes", "no"])
diabetes = st.selectbox("Diabetes", ["yes", "no"])
alcoholism = st.selectbox("Alcoholism", ["yes", "no"])
handcap = st.selectbox("Handicap", ["yes", "no"])
scholarship = st.selectbox("Scholarship", ["yes", "no"])
sms_received = st.selectbox("SMS Received", ["yes", "no"])

appointment_date = st.date_input("Appointment Date", datetime.today())
appointment_hour = st.slider("Appointment Hour", 0, 23, 10)

specialty = st.selectbox("Specialty", specialty_encoder.classes_)
place = st.selectbox("Place", place_encoder.classes_)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict No-Show Risk"):

    # -----------------------------
    # Derived features (AGE LOGIC)
    # -----------------------------
    under_12_years_old = int(age < 12)
    over_60_years_old = int(age > 60)
    patient_needs_companion = int(age < 12 or age > 60)

    appointment_time = appointment_hour

    # -----------------------------
    # SAFE ENCODING
    # -----------------------------
    specialty_encoded = (
        specialty_encoder.transform([specialty])[0]
        if specialty in specialty_encoder.classes_
        else -1
    )

    place_encoded = (
        place_encoder.transform([place])[0]
        if place in place_encoder.classes_
        else -1
    )

    # -----------------------------
    # AUTO WEATHER GENERATION
    # -----------------------------
    month = appointment_date.month

    if month in [3, 4, 5]:
        average_temp_day = np.random.normal(38, 2)
        heat_intensity = 3
    elif month in [6, 7, 8, 9]:
        average_temp_day = np.random.normal(30, 2)
        heat_intensity = 1
    else:
        average_temp_day = np.random.normal(26, 2)
        heat_intensity = 0

    if month in [6, 7, 8, 9]:
        average_rain_day = np.random.normal(12, 5)
        rainy_day_before = np.random.choice([0, 1], p=[0.3, 0.7])
        rain_intensity = np.random.choice([1, 2, 3], p=[0.4, 0.4, 0.2])
    else:
        average_rain_day = np.random.normal(1, 1)
        rainy_day_before = np.random.choice([0, 1], p=[0.9, 0.1])
        rain_intensity = 0

    # -----------------------------
    # BUILD INPUT FRAME
    # -----------------------------
    sample = pd.DataFrame([{
        "appointment_time": appointment_time,
        "gender": 1 if gender == "Male" else 0,
        "disability": disability,
        "age": age,
        "under_12_years_old": under_12_years_old,
        "over_60_years_old": over_60_years_old,
        "patient_needs_companion": patient_needs_companion,
        "average_temp_day": average_temp_day,
        "average_rain_day": average_rain_day,
        "rainy_day_before": rainy_day_before,
        "rain_intensity": rain_intensity,
        "heat_intensity": heat_intensity,
        "Hipertension": hypertension,
        "Diabetes": diabetes,
        "Alcoholism": alcoholism,
        "Handcap": handcap,
        "Scholarship": scholarship,
        "SMS_received": sms_received,
        "specialty_encoded": specialty_encoded,
        "place_encoded": place_encoded
    }])

    # -----------------------------
    # FIX FEATURE ORDER
    # -----------------------------
    sample = sample[model.feature_names_in_]

    # -----------------------------
    # PREDICTION
    # -----------------------------
    probability = model.predict_proba(sample)[0][1]

    st.subheader("Prediction Result")

    st.metric("No-Show Risk", f"{probability:.1%}")

    if probability >= 0.5:
        st.error("⚠️ High Risk of No-Show")
    else:
        st.success("✅ Likely to Attend")