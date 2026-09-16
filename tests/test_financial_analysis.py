import pandas as pd
from src.financial_analysis import prepare_financials


def test_profit_and_margin_calculation():
    df = pd.DataFrame({"date": ["2026-01-01"], "revenue": [1000], "expense": [600]})
    result = prepare_financials(df)
    assert result.loc[0, "profit"] == 400
    assert result.loc[0, "margin_pct"] == 40
