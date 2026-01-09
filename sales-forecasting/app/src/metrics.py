import numpy as np
from src.models import naive_last_value, seasonal_naive

def mae(y_true, y_pred):
    return float(np.mean(np.abs(y_true - y_pred)))

def mape(y_true, y_pred):
    denom = np.where(y_true == 0, np.nan, y_true)
    return float(np.nanmean(np.abs((y_true - y_pred) / denom)) * 100)

def backtest(ts, test_steps, model_name, season_len=None):
    train = ts.iloc[:-test_steps].reset_index(drop=True)
    test = ts.iloc[-test_steps:].reset_index(drop=True)

    if model_name == "Seasonal Naive":
        pred = seasonal_naive(train, test_steps, season_length=season_len)
    else:
        pred = naive_last_value(train, test_steps)

    return {
        "mae": mae(test["y"], pred["yhat"]),
        "mape": mape(test["y"], pred["yhat"]),
        "test": test,
        "pred": pred
    }
