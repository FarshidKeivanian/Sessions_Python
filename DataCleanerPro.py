import pandas as pd
from google.colab import files

#  Step 1: Upload the dataset
uploaded = files.upload()

#  Step 2: Load the dataset
df = pd.read_csv("Dataset_BeforeCleaning.csv")

# Display the original data
print("=== Original Data ===")
print(df)

#  Step 3: Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("\n=== Data After Removing Duplicates ===")
print(df_no_duplicates)

#  Step 4: Display the data before fixing date format
print("\n=== Data Before Standardizing Date Formats ===")
print(df_no_duplicates)

#  Step 5: Standardize the date format to YYYY-MM-DD
df_no_duplicates['Date_of_Birth'] = pd.to_datetime(
    df_no_duplicates['Date_of_Birth'], 
    errors='coerce'   # handles inconsistent formats
).dt.strftime('%Y-%m-%d')

#  Step 6: Display the data after fixing date format
print("\n=== Data After Standardizing Date Formats ===")
print(df_no_duplicates)
