import pandas as pd

def make_weekly_series(df, store, dept=None, agg="sum"):
    sub = df[df["Store"] == store]
    if dept is not None:
        sub = sub[sub["Dept"] == dept]

    grouped = (
        sub.groupby("Date", as_index=False)
        .agg(
            y=("Weekly_Sales", agg),
            is_holiday=("IsHoliday", "max")
        )
    )

    grouped = grouped.sort_values("Date").rename(columns={"Date": "ds"})
    return grouped.reset_index(drop=True)
