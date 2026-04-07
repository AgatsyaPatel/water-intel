import pandas as pd

df = pd.read_csv("water_systems_clean.csv")
cols = ["PWSID", "IS_HEALTH_BASED_IND", "IS_MAJOR_VIOL_IND"]

chunks = []
for chunk in pd.read_csv("SDWA_VIOLATIONS_ENFORCEMENT.csv",
                          encoding="latin1",
                          usecols=cols,
                          chunksize=50000):
    chunks.append(chunk)

viol = pd.concat(chunks, ignore_index=True)
viol = viol[viol["IS_HEALTH_BASED_IND"] == "Y"]

viol_count = viol.groupby("PWSID").size().reset_index()
viol_count.columns = ["PWSID", "VIOLATION_COUNT"]

df =df.merge(viol_count, on="PWSID", how="left")

df["VIOLATION_COUNT"] = df["VIOLATION_COUNT"].fillna(0)

def violation_score(count):
    if count >= 10:
        return 100
    elif count >= 5:
        return 75
    elif count >= 1:
        return 50
    else:
        return 0
    
df["VIOLATION_SCORE"] = df["VIOLATION_COUNT"].apply(violation_score)
df["AGE_SCORE"] = df["SYSTEM_AGE_YEARS"].apply(
    lambda x: 100 if x > 50 else (75 if x > 30 else (50 if x > 20 else 25)))
df["SIZE_SCORE"] = df["POPULATION_SERVED_COUNT"].apply(
    lambda x: 100 if x > 100000 else (75 if x > 10000 else (50 if x > 3000 else 25)))

#age 50%, Size 30%, violation 20%
df["PROCUREMENT_SCORE_V2"] = (df["AGE_SCORE"] * 0.5) + (df["SIZE_SCORE"] * 0.3) + (df["VIOLATION_SCORE"] * 0.2)
df = df.sort_values("PROCUREMENT_SCORE_V2", ascending=False)
df.to_csv("water_procurement_scores.csv", index=False)
print("TOP 20 UTILITIES MOST LIKELY TO BUY EQUIPMENT:")
print(df[["PWS_NAME","STATE_CODE","VIOLATION_COUNT","PROCUREMENT_SCORE_V2"]].head(20).to_string())
