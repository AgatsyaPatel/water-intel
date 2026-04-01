import pandas as pd

df = pd.read_csv("water_systems_clean.csv")

df["AGE_SCORE"] = df["SYSTEM_AGE_YEARS"].apply(lambda x: 100 if x > 50 else (75 if x > 30 else (50 if x > 20 else 25)))

df["SIZE_SCORE"] = df["POPULATION_SERVED_COUNT"].apply(lambda x: 100 if x > 100000 else (75 if x > 10000 else (50 if x > 3000 else 25)))

df["PROCUREMENT_SCORE"] = (df["AGE_SCORE"] * 0.6) + (df["SIZE_SCORE"] * 0.4)

df = df.sort_values("PROCUREMENT_SCORE", ascending=False)

df.to_csv("water_procurement_scores.csv", index=False)

print("TOP 20 UTILITIES MOST LIKELY TO BUY EQUIPMENT:")
print(df[["PWS_NAME","STATE_CODE","SYSTEM_AGE_YEARS","POPULATION_SERVED_COUNT","PROCUREMENT_SCORE"]].head(20).to_string())
