# Financial Data Analytics

A reusable analytics project for transforming transaction-level financial data into revenue, expense, profit, margin, and growth KPIs.

## Business Questions
- How are revenue and expenses changing month over month?
- What is operating profit for each reporting period?
- How is profit margin trending?
- Where are the largest changes in revenue?

## Tech Stack
Python, Pandas, pytest, SQL/Power BI-ready outputs

## Structure
```text
src/financial_analysis.py       # cleaning and KPI calculations
tests/test_financial_analysis.py # automated calculation test
```

## Core Metrics
- Revenue
- Expenses
- Profit = Revenue - Expenses
- Profit Margin %
- Month-over-month Revenue Growth %

## Usage
```python
import pandas as pd
from src.financial_analysis import monthly_kpis

df = pd.read_csv("financials.csv")
print(monthly_kpis(df))
```

## Engineering Practices
The analysis validates required columns, converts dates/numeric fields explicitly, handles zero revenue safely, and includes a unit test for KPI correctness.

## Next Steps
Add an anonymized sample dataset, Power BI dashboard screenshots, category-level variance analysis, forecasting, and CI tests.