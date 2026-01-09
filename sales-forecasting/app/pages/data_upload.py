import streamlit as st
import pandas as pd
from src.loader import load_walmart_data
from src.preprocess import make_weekly_series

st.header("📁 Upload & Prepare Data")

csv_file = st.file_uploader("Upload Walmart train.csv", type=["csv"])

if csv_file is None:
    st.info("Please upload train.csv")
    st.stop()

try:
    df = load_walmart_data(csv_file)
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

st.success(f"Loaded {len(df):,} rows")
st.dataframe(df.head())

stores = sorted(df["Store"].unique())
store = st.selectbox("Select Store", stores)

dept_mode = st.radio("Choose Department Mode", 
                     ["All Departments", "Single Department"], 
                     horizontal=True)

dept = None
if dept_mode == "Single Department":
    depts = sorted(df[df["Store"] == store]["Dept"].unique())
    dept = st.selectbox("Select Department", depts)

agg = st.selectbox("Aggregation", ["sum", "mean"], index=0)

weekly = make_weekly_series(df, store=store, dept=dept, agg=agg)

st.subheader("Weekly Time Series")
st.dataframe(weekly.tail(15))

# store in session state
st.session_state["ts"] = weekly
st.session_state["store"] = store
st.session_state["dept"] = dept

st.success("Data saved. Move to Forecasting page →")
