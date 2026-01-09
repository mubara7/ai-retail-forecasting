import streamlit as st
import numpy as np
import pandas as pd

from src.metrics import backtest
from src.models import naive_last_value, seasonal_naive, prophet_forecast
from src.plots import plot_backtest

st.header("📉 Model Evaluation")

# ------------------------------
# Guard: Ensure Data Exists
# ------------------------------
if "ts" not in st.session_state:
    st.error("Upload data first.")
    st.stop()

ts = st.session_state["ts"]

# ------------------------------
# Model Selection
# ------------------------------
model = st.selectbox("Model", ["Naive", "Seasonal Naive", "Prophet"])
test_steps = st.slider("Test Window (weeks)", 4, 16, 6)

# ------------------------------
# Seasonal parameter (optional)
# ------------------------------
season_len = None
if model == "Seasonal Naive":
    season_len = st.slider("Season Length", 4, 104, 52)

# ------------------------------
# Backtesting Logic
# ------------------------------
def backtest_prophet(ts, steps):
    """
    Backtest Prophet by training on ts[:-steps],
    forecasting next `steps` weeks,
    and comparing with actual.
    """
    train = ts[:-steps]
    actual = ts[-steps:]

    pred = prophet_forecast(train, steps=steps)

    # Align by date
    df = pd.merge(actual, pred, on="ds", how="inner")

    # Metrics
    mae = np.mean(np.abs(df["y"] - df["yhat"]))
    mape = np.mean(np.abs((df["y"] - df["yhat"]) / df["y"])) * 100

    return {
        "test": df,
        "pred": pred,
        "mae": mae,
        "mape": mape
    }

# Decide which model to evaluate
if model == "Prophet":
    result = backtest_prophet(ts, test_steps)
else:
    result = backtest(ts, test_steps, model, season_len)

# ------------------------------
# Display Metrics
# ------------------------------
c1, c2 = st.columns(2)
c1.metric("MAE", f"{result['mae']:.2f}")
c2.metric("MAPE %", f"{result['mape']:.2f}")

# ------------------------------
# Plot Backtest
# ------------------------------
st.pyplot(plot_backtest(result["test"], result["pred"]))
