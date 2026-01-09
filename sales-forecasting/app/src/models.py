import pandas as pd
import numpy as np

from prophet import Prophet


def naive_last_value(ts, steps):
    last_y = float(ts["y"].iloc[-1])
    last_d = ts["ds"].iloc[-1]
    future = pd.date_range(start=last_d, periods=steps + 1, freq="W-FRI")[1:]
    return pd.DataFrame({"ds": future, "yhat": np.full(steps, last_y)})


def seasonal_naive(ts, steps, season_length=52):
    if len(ts) < season_length:
        return naive_last_value(ts, steps)

    history = ts["y"].to_numpy()
    pattern = history[-season_length:]

    reps = int(np.ceil(steps / season_length))
    yhat = np.tile(pattern, reps)[:steps]

    last_d = ts["ds"].iloc[-1]
    future = pd.date_range(start=last_d, periods=steps + 1, freq="W-FRI")[1:]
    return pd.DataFrame({"ds": future, "yhat": yhat})


def prophet_forecast(ts, steps):
    """
    Trains Prophet on the cleaned time series and predicts future weeks.
    """
    df = ts.rename(columns={"ds": "ds", "y": "y"})
    
    model = Prophet(
        weekly_seasonality=True,
        yearly_seasonality=True,
        daily_seasonality=False
    )
    model.fit(df)

    future = model.make_future_dataframe(periods=steps, freq="W-FRI")
    forecast = model.predict(future)

    fc = forecast[["ds", "yhat"]].tail(steps)

    return fc
