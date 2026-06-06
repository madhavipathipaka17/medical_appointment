# 3_Analytics_Dashboard.py

import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# LOAD DATA (PUT IT HERE)
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR.parent.parent / "/Users/venkatakrishnavanaparthi/Desktop/MedicalAppointment/cleaned_data/medical_appointment_cleaned .csv"

df = pd.read_csv(CSV_PATH)

# -----------------------------
# NOW USE df BELOW
# -----------------------------
st.title("Analytics Dashboard")

st.dataframe(df.head())