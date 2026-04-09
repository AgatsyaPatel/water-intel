import pandas as pd

df = pd.read_csv("water_procurement_scores.csv")
df = df[["PWS_NAME", "STATE_CODE", "SYSTEM_AGE_YEARS", "POPULATION_SERVED_COUNT", "PROCUREMENT_SCORE_V2"]]


# state summary of renaming columns
US_STATES = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
df = df[df["STATE_CODE"].isin(US_STATES)]
state_summary = df.groupby("STATE_CODE")["PROCUREMENT_SCORE_V2"].mean().round(1).reset_index()
state_summary.columns = ["State", "Avg Procurement Score"]
state_summary = state_summary.sort_values("Avg Procurement Score", ascending=False)


# renaming columns for Excel
df.columns = ["Utility Name", "State", "Age (Years)", 
              "Population Served", "Procurement Score"]

with pd.ExcelWriter("water_intel_report.xlsx", engine="openpyxl") as write:
    df.to_excel(write, sheet_name="All Utilities", index=False)
    state_summary.to_excel(write, sheet_name="State Summary", index=False)

print("Done! water_intel_report.xlsx created")

                          