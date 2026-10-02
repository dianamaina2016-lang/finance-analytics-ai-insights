import pandas as pd

df = pd.read_csv("finance_dataset.csv")

summary = (
    df.groupby("department")
      .agg(
          budget_kes=("budget_kes", "sum"),
          actual_spend_kes=("actual_spend_kes", "sum"),
          revenue_kes=("revenue_kes", "sum"),
          profit_after_spend_kes=("profit_after_spend_kes", "sum")
      )
      .reset_index()
)

summary["variance_kes"] = summary["budget_kes"] - summary["actual_spend_kes"]
summary["variance_pct"] = (
    summary["variance_kes"] / summary["budget_kes"] * 100
).round(2)

print("\nDepartment summary:")
print(summary.to_string(index=False))

print("\nLargest overspend:")
print(summary.loc[summary["variance_kes"].idxmin()].to_string())
