import pandas as pd

df = pd.read_csv("water_procurement_scores.csv")

#kEEPING ONLY THE COLUMNS WE NEED
df = df[["PWS_NAME", "STATE_CODE", "SYSTEM_AGE_YEARS", "POPULATION_SERVED_COUNT", "PROCUREMENT_SCORE"]]


# state summary BEFORE renaming columns
state_summary = df.groupby("STATE_CODE")["PROCUREMENT_SCORE"].mean().round(1).reset_index()
state_summary.columns = ["State", "Avg Procurement Score"]
state_summary = state_summary.sort_values("Avg Procurement Score", ascending=False)

# rename columns so they look clean in Excel
df.columns = ["Utility Name", "State", "Age (Years)",
              "Population Served", "Procurement Score"]

with pd.ExcelWriter("water_intel_report.xlsx", engine="openpyxl") as write:
    # Sheet 1: Top 100 utilities
    df.head(100).to_excel(write, sheet_name="Top 100 Utilities", index=False)
    # Sheet 2: State Summary
    state_summary.to_excel(write, sheet_name="State Summary", index=False)

print("Done! water_intel_report.xlsx created")

                          