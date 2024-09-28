import pandas as pd
import numpy as np

# Sample dataset to demonstrate data cleaning
data = {
    'Name': ['John Doe', 'Jane Smith', 'John Doe', 'Alice Johnson', np.nan],
    'Date_of_Birth': ['1985-05-20', '1990-07-15', '1985-05-20', '08/12/1988', '1995-10-01'],
    'Credit_Card_Number': ['1234-5678-9012-3456', '9876-5432-1098-7654', np.nan, '4567-8901-2345-6789', '1234-5678-9012-3456']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the original data
print("=== Original Data ===")
print(df)

# Step 1: Identify Missing Values (Before)
print("\n=== Step 1: Identifying Missing Values (Before Cleaning) ===")
print(df.isnull().sum())

# Step 1 Action: Display the data after identifying missing values
# (No data change here, just identified missing values)

# Step 2: Remove Duplicates (Before)
print("\n=== Data Before Removing Duplicates ===")
print(df)

# Remove duplicates
df_no_duplicates = df.drop_duplicates()

# Step 2: Display the data after removing duplicates
print("\n=== Step 2: Data After Removing Duplicates ===")
print(df_no_duplicates)

# Step 3: Standardize Data Formats (Before)
print("\n=== Data Before Standardizing Date Formats ===")
print(df_no_duplicates)

# Standardizing the date format to YYYY-MM-DD
df_no_duplicates['Date_of_Birth'] = pd.to_datetime(df_no_duplicates['Date_of_Birth'], errors='coerce').dt.strftime('%Y-%m-%d')

# Step 3: Display the cleaned data with standardized date format
print("\n=== Step 3: Data After Standardizing Date Format ===")
print(df_no_duplicates)
