🏥 Medical Appointment Analytics System
No-Show Prediction & Demand Forecasting for Healthcare Optimization


📌 Project Overview

This project is a machine learning-based healthcare analytics system designed to solve two major hospital operational challenges:

1️⃣ Patient No-Show Prediction

Predict whether a patient will attend or miss an appointment.

2️⃣ Appointment Demand Forecasting

Predict daily hospital appointment demand for better staffing and resource planning.

🎯 Objectives
Reduce patient no-shows
Improve hospital scheduling efficiency
Optimize staff allocation
Forecast appointment demand accurately
Build a deployable Streamlit application

📊 Dataset Information
No-Show Dataset
~110,000+ appointment records
Binary target: no_show
Demand Forecasting Dataset
498 unique appointment dates (~1.36 years)

Target: daily appointment count

🧹 Data Preprocessing
🔹 Missing Value Handling
Age missing rate: ~21%
Strategy:
Median imputation
Added age_missing indicator

🔹 Feature Cleaning Decisions
Removed inconsistent age-group flags
Fixed encoding mismatches
Standardized categorical variables

⚙️ Feature Engineering

👤 Patient Features
Age
Gender
Disability encoding:
intellectual → 0
motor → 1
unknown → 2
Hypertension
Diabetes
🏥 Appointment Features
Appointment time
SMS received
Day of week
📍 Location Features
Encoded hospital place
🧠 Specialty Encoding
Specialty	Code
assist	0
enf	1
occupational therapy	2
pedagogo	3
physiotherapy	4
psychotherapy	5
sem especialidade	6
speech therapy	7
unknown	8

📈 Exploratory Data Analysis (Key Insights)
🧍 No-Show Patterns
Specialty is the strongest predictor (16%–53% variation)
Young adults → ~47% no-show (highest risk)
Seniors → ~22% no-show
SMS reminders → minimal impact (~31.8% no-show)
Hypertension/Diabetes patients → lower no-show rates

🕒 Time Insights
Peak no-show times:
10 AM → ~39%
5 PM → ~37%
Morning slightly worse than afternoon

📍 Location Insights
Unknown locations → ~34.8% no-show
Best-performing locations → <10% no-show
🌦️ Weather Insights
Minimal effect (~2% variation only)

📊 Demand Forecasting Insights
Average demand: ~220 appointments/day
Median: ~126.5
Highly skewed distribution
Weekly Pattern
Sunday: lowest demand (~156)
Thursday: highest demand (~259)
Key Insight

👉 Specialty mix is the strongest driver of demand

🤖 Machine Learning Models
🧍 No-Show Prediction
Tree-based models used
Strong predictors:
Specialty
Age
Location
Weak predictors:
SMS reminders
Weather

📊 Demand Forecasting Models
Model	MAE	RMSE	R²
Random Forest	114.94	183.31	0.583
XGBoost	123.20	198.33	0.513
Lag-based baseline	Poor	Poor	-0.539
⚠️ Leakage Warning

A high-performing model (R² = 0.946) was found but:

It used same-day features (specialty counts, place counts)
❌ Not valid for real forecasting
⚠️ Key Challenges
Feature mismatch between training & deployment
Encoding inconsistencies in Streamlit app
Data leakage in demand model
Place encoding standardization issues
🖥️ Streamlit Application

The project includes a full interactive dashboard:

Features
Age slider input
Gender selection
Specialty dropdown
Disability selection
Place selection
Real-time prediction
Modules
No-show prediction page
Demand forecasting page
Analytics dashboard

📌 Tech Stack
Python 🐍
Pandas, NumPy
Scikit-learn
XGBoost
Streamlit
Joblib

📊 Key Conclusions
Specialty is the dominant predictor in both problems
Weather has minimal predictive power
Age + location are secondary strong features
Data leakage must be strictly avoided in forecasting models

🚀 Future Improvements
Add deep learning time-series models (LSTM/Prophet)
Improve real-time hospital integration
Deploy on cloud (AWS / Streamlit Cloud)
Add patient risk scoring system

📁 Project Structure
MedicalAppointment/
│
├── streamlit_app/
│   ├── pages/
│   │   ├── No_Show_Prediction.py
│   │   ├── Demand_Forecasting.py
│   │   └── Analytics.py
│
├── models/
│   ├── no_show_model.pkl
│   ├── demand_forecast_model.pkl
│
├── encoders/
├── cleaned_data/
└── README.md
👨‍💻 Author

Madhavi Pathipaka

📌 License

This project is for educational and research purposes.
