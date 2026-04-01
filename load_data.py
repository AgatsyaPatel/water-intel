import pandas as pd

print("Loading EPA water systems data...")

df = pd.read_csv("SDWA_PUB_WATER_SYSTEMS.csv", encoding="latin1", low_memory=False)

print(f"Loaded {len(df):,} rows")

COLUMNS_WE_NEED = ["PWSID","PWS_NAME","STATE_CODE","PWS_ACTIVITY_CODE","PWS_TYPE_CODE","POPULATION_SERVED_COUNT","PRIMARY_SOURCE_CODE","FIRST_REPORTED_DATE"]

df = df[COLUMNS_WE_NEED]
df = df[df["PWS_ACTIVITY_CODE"] == "A"]
df = df[df["PWS_TYPE_CODE"] == "CWS"]
df = df.dropna(subset=["POPULATION_SERVED_COUNT","FIRST_REPORTED_DATE"])
df["FIRST_REPORTED_DATE"] = pd.to_datetime(df["FIRST_REPORTED_DATE"], errors="coerce")
df["YEAR_ESTABLISHED"] = df["FIRST_REPORTED_DATE"].dt.year
df["SYSTEM_AGE_YEARS"] = 2026 - df["YEAR_ESTABLISHED"]
df = df[(df["SYSTEM_AGE_YEARS"] > 0) & (df["SYSTEM_AGE_YEARS"] < 150)]
df.to_csv("water_systems_clean.csv", index=False)

print(f"Done! {len(df):,} active community water systems saved.")
