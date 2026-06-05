import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

model = joblib.load("../models/demand_forecast_model.pkl")

st.title("Demand Forecasting")

days = st.slider(
    "Forecast Horizon",
    7,
    30,
    14
)

future = pd.DataFrame({
    "day_num": range(days)
})

forecast = model.predict(future)

result = pd.DataFrame({
    "Day": range(1, days+1),
    "Forecasted Appointments": forecast
})

fig = px.line(
    result,
    x="Day",
    y="Forecasted Appointments",
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.dataframe(result)