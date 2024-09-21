import pandas as pd

# Load data from an Excel file
df = pd.read_excel(r'C:\IDS201\Customer_Satisfaction_Survey.xlsx', sheet_name='Sheet1')

# Display the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Calculate basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Count the number of occurrences for a specific column
if 'Column_Name' in df.columns:
    value_counts = df['Column_Name'].value_counts()
    print("\nValue counts for the selected column:")
    print(value_counts)
else:
    print("\nColumn_Name not found in the dataset.")