import pandas as pd
import numpy as np
from prophet import Prophet

# ----------------------------------------------------
# Simple Z-Score Based Anomaly Detection
# ----------------------------------------------------
def detect_anomalies_zscore(ts, threshold=2.5):
    df = ts.copy()
    df["zscore"] = (df["y"] - df["y"].mean()) / df["y"].std()

    df["anomaly"] = df["zscore"].abs() > threshold
    anomalies = df[df["anomaly"] == True]

    return df, anomalies


# ----------------------------------------------------
# Prophet-Based Residual Anomaly Detection
# ----------------------------------------------------
def detect_anomalies_prophet(ts, threshold=0.25):
    """
    threshold = 0.25 → 25% deviation from predicted
    """
    df = ts.rename(columns={"ds": "ds", "y": "y"}).copy()

    model = Prophet(
        weekly_seasonality=True,
        yearly_seasonality=True,
        daily_seasonality=False
    )
    model.fit(df)

    future = model.make_future_dataframe(periods=0, freq="W-FRI")
    forecast = model.predict(future)

    merged = df.copy()
    merged["yhat"] = forecast["yhat"]
    merged["residual"] = merged["y"] - merged["yhat"]

    merged["percentage_deviation"] = abs(merged["residual"] / merged["yhat"])

    merged["anomaly"] = merged["percentage_deviation"] > threshold

    anomalies = merged[merged["anomaly"] == True]

    return merged, anomalies
