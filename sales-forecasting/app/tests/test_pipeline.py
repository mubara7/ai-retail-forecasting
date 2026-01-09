import pandas as pd
from src.loader import load_walmart_data
from src.preprocess import make_weekly_series
from src.models import naive_last_value

def test_pipeline():
    df = load_walmart_data("data/train.csv")
    ts = make_weekly_series(df, store=1, dept=None)
    fc = naive_last_value(ts, steps=8)
    assert len(fc) == 8
