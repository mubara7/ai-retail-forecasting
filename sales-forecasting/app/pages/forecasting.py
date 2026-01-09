import streamlit as st
from src.models import naive_last_value, seasonal_naive, prophet_forecast
from src.plots import plot_forecast

st.header("🔮 Forecasting")

if "ts" not in st.session_state:
    st.error("Please upload data first.")
    st.stop()

ts = st.session_state["ts"]

model = st.selectbox(
    "Select Model",
    ["Naive", "Seasonal Naive", "Prophet"]
)

horizon = st.slider("Forecast Horizon (weeks)", 4, 24, 8)

if model == "Seasonal Naive":
    season_length = st.slider("Season Length (weeks)", 4, 104, 52)
    fc = seasonal_naive(ts, steps=horizon, season_length=season_length)

elif model == "Prophet":
    st.info("Prophet automatically handles trends + seasonality.")
    fc = prophet_forecast(ts, steps=horizon)

else:
    fc = naive_last_value(ts, steps=horizon)

st.subheader("Forecast Table")
st.dataframe(fc)

st.pyplot(plot_forecast(ts, fc))

st.session_state["forecast"] = fc
st.success("Forecast saved. Move to Evaluation page →")
