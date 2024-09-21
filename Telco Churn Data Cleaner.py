import pandas as pd
df = pd.read_csv(r'C:\IDS201\Telco_Customer_Churn_Dataset_with_Missing_Values.csv')

print(df.head())
print(df.info())
print(df.describe())

# Identify and handle missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

df.dropna(inplace=True)  # Example of dropping rows with missing values
