# importing necessary libs
import numpy as np
import pandas as pd
from pyparsing import col
import streamlit as st

st.set_page_config(page_title="Main Page", page_icon="🏡")

st.title("Main Page")

st.markdown(
    """
        ---
        ## Description
        ##### This project is our graduation project for K136. Istanbul Data Science Bootcamp. In this project, we used the weather and natural gas consumption data from İBB. To estimate natural gas use, we first found the monthly average temperature and humidity data for 2022 using time series. Then, using this data and historical data, we estimated the natural gas consumption in 2022 with XGBoost.
        ---
        ## Model Development
        ##### We used Prophet for time series forecasting and XGBoost for regression.
        ---
        ## Supporters
    """
)

col1, _, col2 = st.columns([2, 1, 2])
with col1:
    st.image("images/1.png")
    st.image("images/3.png")
with col2:
    st.image("images/2.png")
    st.image("images/4.png")

_, col1, _ = st.columns([1.5, 2, 1.5])
with col1:
    st.image("images/5.png")
