import matplotlib.pyplot as plt

# ----------------------------------------------------
# Forecast Plot
# ----------------------------------------------------
def plot_forecast(ts, fc):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ts["ds"], ts["y"], label="Actual", color="blue")
    ax.plot(fc["ds"], fc["yhat"], label="Forecast", color="green")
    ax.legend()
    ax.set_title("Forecast vs Actual")
    return fig


# ----------------------------------------------------
# Backtest Plot
# ----------------------------------------------------
def plot_backtest(test, pred):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(test["ds"], test["y"], label="Actual (Test)", color="blue")
    ax.plot(pred["ds"], pred["yhat"], label="Predicted", color="orange")
    ax.legend()
    ax.set_title("Backtest Results")
    return fig


# ----------------------------------------------------
# Anomaly Plot
# ----------------------------------------------------
def plot_anomalies(df):
    fig, ax = plt.subplots(figsize=(10, 5))

    # Actual values
    ax.plot(df["ds"], df["y"], label="Sales", color="blue")

    # Highlight anomalies
    anomalies = df[df["anomaly"] == True]
    ax.scatter(
        anomalies["ds"],
        anomalies["y"],
        color="red",
        label="Anomaly",
        s=60,
        zorder=5
    )

    ax.legend()
    ax.set_title("Detected Anomalies")
    return fig
