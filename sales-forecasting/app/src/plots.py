import matplotlib.pyplot as plt

def plot_forecast(ts, fc):
    fig, ax = plt.subplots()
    ax.plot(ts["ds"], ts["y"], label="Actual")
    ax.plot(fc["ds"], fc["yhat"], label="Forecast")
    ax.legend()
    return fig

def plot_backtest(test, pred):
    fig, ax = plt.subplots()
    ax.plot(test["ds"], test["y"], label="Actual (test)")
    ax.plot(pred["ds"], pred["yhat"], label="Prediction")
    ax.legend()
    return fig
