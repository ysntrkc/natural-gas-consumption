import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("data/data.csv")

st.set_page_config(page_title="Graphs", page_icon="📈")
st.title("Graphs for Every District")

option = st.selectbox("Select a district", df["ilce"].unique())

chart_data = pd.read_csv(f"data/tahmin/{option}_tahmin.csv")
chart_data["tarih"] = pd.to_datetime(chart_data["tarih"])
chart_data["tarih"] = chart_data["tarih"].dt.strftime("%Y.%m")

fig = px.bar(
    chart_data,
    x="tarih",
    y="tuketim",
    title=f"{option}: From 2021-11 to 2022-12 Natural Gas Consumption Prediction",
)
fig.update_yaxes(title="Natural Gas Consumption (MWh)")
fig.update_xaxes(title="Date", tickangle=30)
st.plotly_chart(fig)

fig = px.line(
    chart_data,
    x="tarih",
    y="tuketim",
    title=f"{option}: From 2021-11 to 2022-12 Natural Gas Consumption Prediction",
)
fig.update_yaxes(title="Natural Gas Consumption (MWh)")
fig.update_xaxes(title="Date", tickangle=30)
st.plotly_chart(fig)
