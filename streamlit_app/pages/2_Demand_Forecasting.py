import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# -----------------------------
# Load model
# -----------------------------
model = joblib.load("../models/demand_forecast_model.pkl")

st.title("🏥 Hospital Demand Prediction System")

st.write("Fill patient + appointment details to predict demand.")

# -----------------------------
# MAPPINGS
# -----------------------------
SPECIALTY_MAP = {
    "assist": 0,
    "enf": 1,
    "occupational therapy": 2,
    "pedagogo": 3,
    "physiotherapy": 4,
    "psychotherapy": 5,
    "sem especialidade": 6,
    "speech therapy": 7,
    "unknown": 8
}

DISABILITY_MAP = {
    "intellectual": 0,
    "motor": 1,
    "unknown": 2
}

# Example places (replace with your real encoded list)
PLACE_OPTIONS = [
    "Penha",
    "Baln. Piçarras",
    "Camboriu",
    "Itajaí",
    "Unknown"
]

# -----------------------------
# UI INPUTS
# -----------------------------
age = st.slider("Age", 0, 120, 30)

gender = st.selectbox("Gender", ["Male", "Female"])

specialty = st.selectbox("Specialty", list(SPECIALTY_MAP.keys()))

disability = st.selectbox("Disability", list(DISABILITY_MAP.keys()))

place = st.selectbox("Place", PLACE_OPTIONS)

appointment_date = st.date_input("Appointment Date", datetime.today())

# -----------------------------
# FEATURE ENGINEERING
# -----------------------------
def build_features(age, gender, specialty, disability, place, date):

    cols = model.feature_names_in_
    df = pd.DataFrame(0, index=[0], columns=cols)

    # -----------------------------
    # Age
    # -----------------------------
    if "age" in df.columns:
        df["age"] = age

    # -----------------------------
    # Gender encoding
    # -----------------------------
    if "gender" in df.columns:
        df["gender"] = 1 if gender == "Male" else 0

    # -----------------------------
    # Specialty mapping
    # -----------------------------
    spec_val = SPECIALTY_MAP[specialty]

    spec_col = f"specialty_{spec_val}_count"
    if spec_col in df.columns:
        df[spec_col] = 1

    # -----------------------------
    # Disability mapping
    # -----------------------------
    dis_val = DISABILITY_MAP[disability]

    dis_col = f"disability_{dis_val}_count"
    if dis_col in df.columns:
        df[dis_col] = 1

    # -----------------------------
    # Place encoding (safe fallback)
    # -----------------------------
    place_col = f"place_{place}_count"

    if place_col in df.columns:
        df[place_col] = 1
    else:
        if "place_unknown_count" in df.columns:
            df["place_unknown_count"] = 1

    # -----------------------------
    # Date features
    # -----------------------------
    dow = date.weekday()

    if "day_of_week" in df.columns:
        df["day_of_week"] = dow

    if "dow_sin" in df.columns:
        df["dow_sin"] = np.sin(2 * np.pi * dow / 7)

    if "dow_cos" in df.columns:
        df["dow_cos"] = np.cos(2 * np.pi * dow / 7)

    # -----------------------------
    # SAFE LAG FEATURES
    # -----------------------------
    base = 100

    for lag in ["lag_1", "lag_7", "lag_14"]:
        if lag in df.columns:
            df[lag] = base

    if "rolling_mean_7" in df.columns:
        df["rolling_mean_7"] = base

    return df


# -----------------------------
# Predict button
# -----------------------------
if st.button("📊 Predict Demand"):

    X = build_features(age, gender, specialty, disability, place, appointment_date)

    # HARD ALIGNMENT (prevents ALL sklearn errors)
    X = X.reindex(columns=model.feature_names_in_, fill_value=0)

    prediction = model.predict(X)[0]

    st.subheader("📈 Predicted Demand")

    st.success(f"Expected Appointments: {int(prediction)}")