import pandas as pd
import json

# 1. Load JSON file
with open("sydney_trains.json") as f:
    data = json.load(f)

# 2. Normalize nested JSON (flatten 'details' and 'extra')
df = pd.json_normalize(data["trains"])

# 3. Select relevant columns
df_clean = df[["details.station", "details.arrival_time", "details.status", 
               "extra.platform", "extra.delay_min"]]

# 4. Rename columns for clarity
df_clean = df_clean.rename(columns={
    "details.station": "Station",
    "details.arrival_time": "ArrivalTime",
    "details.status": "Status",
    "extra.platform": "Platform",
    "extra.delay_min": "DelayMinutes"
})

# 5. Save to Excel
import os
os.makedirs("output", exist_ok=True)
df_clean.to_excel("output/trains_report.xlsx", index=False)

# 6. Preview the cleaned DataFrame
print(df_clean)
