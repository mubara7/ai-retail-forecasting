import pandas as pd

REQUIRED_COLS = {"Store", "Dept", "Date", "Weekly_Sales", "IsHoliday"}

def load_walmart_data(csv_file) -> pd.DataFrame:
    df = pd.read_csv(csv_file)
    missing = REQUIRED_COLS - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    df["Date"] = pd.to_datetime(df["Date"])
    df["Weekly_Sales"] = pd.to_numeric(df["Weekly_Sales"])
    df["IsHoliday"] = df["IsHoliday"].astype(str).str.lower().isin(["true", "1", "yes"])

    return df
