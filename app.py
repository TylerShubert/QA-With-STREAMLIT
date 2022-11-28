import pandas as pd
from pathlib import Path
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt




whale_navs = pd.read_csv(
    Path("./Resources/Whale_navs.csv"),
    index_col="date",
    parse_dates=True,
    infer_datetime_format=True
)
st.write("Reviewing the first 5 lines of the Data")
st.write(whale_navs.head())


st.write("Using Pandas to create a daily returns DataFrame & reviewing the first 5 lines of said DataFrame ")
st.write(whale_navs.pct_change().dropna())


st.write("Using Pandas to visualize the previously created Daily returns DataFrame ")
st.area_chart(whale_navs)


st.write("Dropping the S&P500 from the chart and reviewing only the hedge fund daily returns.  ")
whale_navs_hf = whale_navs.drop(columns=["S&P 500"])

st.line_chart(whale_navs_hf)