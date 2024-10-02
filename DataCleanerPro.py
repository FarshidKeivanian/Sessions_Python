import pandas as pd
import numpy as np

# Use the Same Folder for data and code
# Load the dataset
df = pd.read_csv('Dataset_BeforeCleaning.csv')

# Display the original data
print("=== Original Data ===")
print(df)

# Step 1: Identifying Missing Values (Before Cleaning)
print("\n=== Step 1: Identifying Missing Values (Before Cleaning) ===")
print(df.isnull().sum())

# Step 1: Display the data before removing duplicates
print("\n=== Data Before Removing Duplicates ===")
print(df)

# Step 2: Remove duplicates
df_no_duplicates = df.drop_duplicates()

# Step 2: Display the data after removing duplicates
print("\n=== Step 2: Data After Removing Duplicates ===")
print(df_no_duplicates)

# Step 3: Display the data before standardizing date formats
print("\n=== Data Before Standardizing Date Formats ===")
print(df_no_duplicates)

# Step 3: Standardizing the date format to YYYY-MM-DD
df_no_duplicates['Date_of_Birth'] = pd.to_datetime(df_no_duplicates['Date_of_Birth'], format='%m/%d/%Y', errors='coerce').fillna(
    pd.to_datetime(df_no_duplicates['Date_of_Birth'], errors='coerce')).dt.strftime('%Y-%m-%d')

# Step 3: Display the data after standardizing the date format
print("\n=== Step 3: Data After Standardizing Date Format ===")
print(df_no_duplicates)

# Step 4: Display the data before removing NaN values
print("\n=== Step 4: Data Before Removing NaN Values ===")
print(df_no_duplicates)

# Step 4: Remove rows where 'Name' or 'Date_of_Birth' is NaN
df_no_duplicates = df_no_duplicates.dropna(subset=['Name', 'Date_of_Birth'])

# Step 4: Display the data after removing NaN values
print("\n=== Step 4: Data After Removing NaN Values ===")
print(df_no_duplicates)

# Save the cleaned data to a new CSV file
df_no_duplicates.to_csv('Dataset_AfterCleaning.csv', index=False)
