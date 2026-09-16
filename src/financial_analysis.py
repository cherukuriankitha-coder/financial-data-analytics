"""Reusable financial KPI calculations."""
import pandas as pd

REQUIRED_COLUMNS = {"date", "revenue", "expense"}


def prepare_financials(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"], errors="raise")
    out[["revenue", "expense"]] = out[["revenue", "expense"]].apply(pd.to_numeric, errors="raise")
    out["profit"] = out["revenue"] - out["expense"]
    out["margin_pct"] = (out["profit"] / out["revenue"].replace(0, pd.NA) * 100).fillna(0)
    return out


def monthly_kpis(df: pd.DataFrame) -> pd.DataFrame:
    clean = prepare_financials(df)
    monthly = clean.set_index("date").resample("MS")[["revenue", "expense", "profit"]].sum()
    monthly["margin_pct"] = (monthly["profit"] / monthly["revenue"].replace(0, pd.NA) * 100).fillna(0)
    monthly["revenue_growth_pct"] = monthly["revenue"].pct_change().mul(100)
    return monthly.reset_index()
