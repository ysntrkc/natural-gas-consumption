import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Graphs", page_icon="📈")
st.title("Graphs for Every District")

df = pd.read_csv("data/data.csv")
option = st.selectbox("Select a district", df["ilce"].unique())

# Import future data for selected district
chart_data = pd.read_csv(f"data/tahmin/{option}_tahmin.csv")
chart_data["tarih"] = pd.to_datetime(chart_data["tarih"])
chart_data["tarih"] = chart_data["tarih"].dt.strftime("%Y.%m")

# Plotting the data
fig = px.bar(
    chart_data,
    x="tarih",
    y="tuketim",
    title=f"{option}: Natural Gas Consumption Prediction (Nov 2021 - Dec 2022)",
    # title=f"{option}: Doğalgaz Tüketim Tahmini (Kasım 2021 - Aralık 2022)",
)
fig.update_yaxes(title="Natural Gas Consumption (MWh)")
fig.update_xaxes(title="Date", tickangle=30)
# fig.update_yaxes(title="Doğalgaz Tüketimi (MWh)")
# fig.update_xaxes(title="Tarih", tickangle=30)
st.plotly_chart(fig)

# Import train and test data for selected district
chart_data_2 = pd.read_csv(f"data/train_test/{option}.csv")
chart_data_2["tarih"] = pd.to_datetime(chart_data_2["tarih"])
chart_data_2["tarih"] = chart_data_2["tarih"].dt.strftime("%Y.%m")

train_test_data = chart_data_2[chart_data_2["tarih"] >= "2020.04"]

# Plot train/test data
fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=train_test_data["tarih"],
        y=train_test_data["tuketim"],
        name="Actual",
        mode="lines+markers",
    )
)
fig.add_trace(
    go.Scatter(
        x=train_test_data["tarih"],
        y=train_test_data["prediction"],
        name="Predicted",
        mode="lines+markers",
    )
)
fig.update_layout(
    title={
        "text": f"{option}: Test Data (Apr 2020 - Oct 2021)",
        "y": 0.9,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    },
    xaxis_title="Date",
    xaxis_tickangle=45,
    yaxis_title="Natural Gas Consumption (MWh)",
)

st.plotly_chart(fig)
