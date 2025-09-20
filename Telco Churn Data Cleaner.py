# === Telco Churn: Upload, Inspect, Clean, Download (Colab) ===

import pandas as pd
from google.colab import files
import os, io

# 1) Upload the CSV from your computer
print("Upload your CSV (e.g., Telco_Customer_Churn_Dataset_with_Missing_Values.csv)")
uploaded = files.upload()
filename = next(iter(uploaded))  # first uploaded file name

# 2) Read the CSV (treat common placeholders as missing)
df = pd.read_csv(
    filename,
    na_values=["", "NA", "N/A", "na", "?", "null", "None"]
)

# 3) Quick look at the data
print("\nFirst 5 rows:")
print(df.head())

print("\nInfo about columns & types:")
buf = io.StringIO()
df.info(buf=buf)       # df.info() prints to a buffer; we show it nicely
print(buf.getvalue())

print("\nDescriptive statistics (numeric columns):")
print(df.describe())

# 4) Show missing values per column
missing_values = df.isna().sum().sort_values(ascending=False)
print("\nMissing values in each column:")
print(missing_values)

# 5) Drop rows that contain ANY missing values
rows_before = len(df)
df_clean = df.dropna().copy()
rows_after = len(df_clean)
print(f"\nRows before: {rows_before} | Rows after dropna: {rows_after} | Removed: {rows_before - rows_after}")

# 6) Save cleaned file and offer it for download
out_name = f"{os.path.splitext(filename)[0]}_Cleaned.csv"
df_clean.to_csv(out_name, index=False)
print(f"\nSaved cleaned dataset as: {out_name}")

# 7) Download to your computer
files.download(out_name)
