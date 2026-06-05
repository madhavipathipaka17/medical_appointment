import streamlit as st
import pandas as pd
import joblib

model = joblib.load("../models/no_show_model.pkl")

st.title("Patient No-Show Risk Prediction")

age = st.number_input("Age", 0, 100)

gender = st.selectbox(
    "Gender",
    ["Male","Female"]
)

hypertension = st.selectbox(
    "Hypertension",
    [0,1]
)

diabetes = st.selectbox(
    "Diabetes",
    [0,1]
)

sms_received = st.selectbox(
    "SMS Received",
    [0,1]
)

if st.button("Predict"):

    sample = pd.DataFrame({
        "age":[age],
        "gender":[1 if gender=="Male" else 0],
        "Hipertension":[hypertension],
        "Diabetes":[diabetes],
        "SMS_received":[sms_received]
    })

    probability = model.predict_proba(sample)[0][1]

    st.metric(
        "No Show Risk",
        f"{probability:.1%}"
    )