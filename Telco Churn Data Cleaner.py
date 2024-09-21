import pandas as pd

# Load the dataset with missing values
df = pd.read_csv(r'C:\IDS201\Telco_Customer_Churn_Dataset_with_Missing_Values.csv')

print(df.head())
print(df.info())
print(df.describe())

# Identify and handle missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Drop rows with missing values
df.dropna(inplace=True)  

# Save the cleaned dataset to the same folder
df.to_csv(r'C:\IDS201\Telco_Customer_Churn_Dataset_Cleaned.csv', index=False)
