import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------
# Load model + encoders
# -----------------------------
model = joblib.load("../models/demand_forecast_model.pkl")
specialty_encoder = joblib.load("../models/specialty_encoder.pkl")
place_encoder = joblib.load("../models/place_encoder.pkl")

st.title("🏥 Medical Demand Forecasting")

# -----------------------------
# REQUIRED TRAINING FEATURES
# -----------------------------
feature_cols = [
    'appointment_time', 'gender', 'disability', 'age',
    'under_12_years_old', 'over_60_years_old', 'patient_needs_companion',
    'average_temp_day', 'average_rain_day', 'max_temp_day', 'max_rain_day',
    'rainy_day_before', 'storm_day_before', 'rain_intensity', 'heat_intensity',
    'Hipertension', 'Diabetes', 'Alcoholism', 'Handcap', 'Scholarship',
    'SMS_received', 'age_missing',
    'appointment_year', 'appointment_month', 'appointment_day', 'appointment_hour',
    'specialty_encoded', 'place_encoded'
]

# -----------------------------
# USER INPUTS
# -----------------------------
age = st.number_input("Age", 0, 100, 30)
gender = st.selectbox("Gender", ["M", "F"])
disability = st.number_input("Disability", 0, 5, 0)

appointment_date = st.date_input("Appointment Date")
appointment_time = st.time_input("Appointment Time")

sms = st.selectbox("SMS Received", [0, 1])
diabetes = st.selectbox("Diabetes", [0, 1])
hypertension = st.selectbox("Hypertension", [0, 1])

specialty = st.selectbox("Specialty", specialty_encoder.classes_)
place = st.selectbox("Place", place_encoder.classes_)

# -----------------------------
# WEATHER (you can replace with API later)
# -----------------------------
avg_temp = st.number_input("Avg Temp", 0.0, 50.0, 30.0)
avg_rain = st.number_input("Avg Rain", 0.0, 200.0, 5.0)
max_temp = st.number_input("Max Temp", 0.0, 50.0, 35.0)
max_rain = st.number_input("Max Rain", 0.0, 200.0, 10.0)

rainy_day_before = st.selectbox("Rainy Day Before", [0, 1])
storm_day_before = st.selectbox("Storm Day Before", [0, 1])

rain_intensity = st.selectbox("Rain Intensity", [0, 1, 2])
heat_intensity = st.selectbox("Heat Intensity", [0, 1, 2])

# -----------------------------
# BUILD INPUT DATAFRAME
# -----------------------------
input_data = {}

# numeric features
input_data['age'] = age
input_data['disability'] = disability
input_data['average_temp_day'] = avg_temp
input_data['average_rain_day'] = avg_rain
input_data['max_temp_day'] = max_temp
input_data['max_rain_day'] = max_rain
input_data['rainy_day_before'] = rainy_day_before
input_data['storm_day_before'] = storm_day_before
input_data['rain_intensity'] = rain_intensity
input_data['heat_intensity'] = heat_intensity
input_data['SMS_received'] = sms
input_data['Hipertension'] = hypertension
input_data['Diabetes'] = diabetes
input_data['Alcoholism'] = 0
input_data['Handcap'] = 0
input_data['Scholarship'] = 0

# encoded categorical
input_data['specialty_encoded'] = specialty_encoder.transform([specialty])[0]
input_data['place_encoded'] = place_encoder.transform([place])[0]

# derived features (IMPORTANT)
input_data['under_12_years_old'] = 1 if age < 12 else 0
input_data['over_60_years_old'] = 1 if age > 60 else 0
input_data['patient_needs_companion'] = 1 if age < 12 or age > 60 else 0
input_data['age_missing'] = 0

# datetime features (MATCH TRAINING)
input_data['appointment_year'] = appointment_date.year
input_data['appointment_month'] = appointment_date.month
input_data['appointment_day'] = appointment_date.day
input_data['appointment_hour'] = appointment_time.hour

# appointment_time (VERY IMPORTANT: model expects this column)
input_data['appointment_time'] = appointment_time.hour * 60 + appointment_time.minute

# gender encoding (adjust if your training used different encoding)
input_data['gender'] = 1 if gender == "M" else 0

# -----------------------------
# CREATE DATAFRAME
# -----------------------------
future = pd.DataFrame([input_data])

# -----------------------------
# ALIGN FEATURES (CRITICAL FIX)
# -----------------------------
for col in feature_cols:
    if col not in future.columns:
        future[col] = 0  # safe default

# remove extra columns
future = future[feature_cols]

# -----------------------------
# PREDICT
# -----------------------------
if st.button("Predict Demand"):
    prediction = model.predict(future)[0]
    st.success(f"📊 Predicted Demand: {int(prediction)}")