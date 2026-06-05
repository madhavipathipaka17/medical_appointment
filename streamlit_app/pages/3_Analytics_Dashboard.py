import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "../cleaned_data/cleaned_appointment_data.csv"
)

st.title("Analytics Dashboard")

tab1, tab2, tab3 = st.tabs([
    "Specialty",
    "Age",
    "Appointments"
])

with tab1:

    specialty = (
        df.groupby("specialty")
        ["no_show"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        specialty,
        x="specialty",
        y="no_show"
    )

    st.plotly_chart(fig)

with tab2:

    fig = px.histogram(
        df,
        x="age"
    )

    st.plotly_chart(fig)

with tab3:

    fig = px.histogram(
        df,
        x="appointment_hour"
    )

    st.plotly_chart(fig)