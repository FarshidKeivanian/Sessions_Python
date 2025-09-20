# Step 1: Install and import libraries
import pandas as pd
from google.colab import files

# Step 2: Upload Excel file
print("Please upload your Excel file:")
uploaded = files.upload()

# Step 3: Get the uploaded filename
filename = list(uploaded.keys())[0]

# Step 4: Load data from the uploaded Excel file
df = pd.read_excel(filename, sheet_name='Sheet1')

# Step 5: Display the first 5 rows of the DataFrame
print("First 5 rows of the dataset:")
print(df.head())

# Step 6: Calculate basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Step 7: Count the number of occurrences for a specific column
column_to_check = "Column_Name"  # <- Replace with actual column name
if column_to_check in df.columns:
    value_counts = df[column_to_check].value_counts()
    print(f"\nValue counts for '{column_to_check}':")
    print(value_counts)
else:
    print(f"\n'{column_to_check}' not found in the dataset.")
