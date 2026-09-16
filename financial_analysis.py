"""Starter financial analytics workflow using pandas."""
import pandas as pd

def prepare_financials(df: pd.DataFrame) -> pd.DataFrame:
    data = df.copy()
    data["revenue"] = pd.to_numeric(data["revenue"], errors="coerce").fillna(0)
    data["expenses"] = pd.to_numeric(data["expenses"], errors="coerce").fillna(0)
    data["profit"] = data["revenue"] - data["expenses"]
    data["profit_margin_pct"] = (data["profit"] / data["revenue"].replace(0, pd.NA) * 100).fillna(0)
    return data

def summarize(df: pd.DataFrame) -> dict:
    data = prepare_financials(df)
    return {
        "total_revenue": round(data["revenue"].sum(), 2),
        "total_expenses": round(data["expenses"].sum(), 2),
        "total_profit": round(data["profit"].sum(), 2),
        "average_margin_pct": round(data["profit_margin_pct"].mean(), 2),
    }

if __name__ == "__main__":
    sample = pd.DataFrame({"revenue": [12000, 15000, 18000], "expenses": [8000, 9500, 11000]})
    print(summarize(sample))
