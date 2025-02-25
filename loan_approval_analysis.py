import pandas as pd
import matplotlib.pyplot as plt

# URL of the dataset
url = "https://github.com/FarshidKeivanian/Sessions_Python/raw/main/Loan_Dataset.csv"

# Load the dataset directly from the URL
df = pd.read_csv(url)

# Display the first few rows
print(df.head())

# Select only numerical features
numerical_features = df.select_dtypes(include=['int64', 'float64'])

# Compute correlation with Loan Approval
correlation_with_target = numerical_features.corr()["Loan_Approval"].drop("Loan_Approval").sort_values(ascending=False)

# Display correlation ranking
print(correlation_with_target)

# Convert categorical columns into numerical codes
df_encoded = df.copy()
categorical_columns = ["Employment_Status", "Marital_Status", "Home_Ownership"]

for col in categorical_columns:
    df_encoded[col] = df_encoded[col].astype("category").cat.codes

# Compute correlation again including encoded categorical variables
correlation_with_target = df_encoded.corr()["Loan_Approval"].drop("Loan_Approval").sort_values(ascending=False)

# Display correlation ranking
print(correlation_with_target)

# Plot correlation ranking
plt.figure(figsize=(8, 6))
correlation_with_target.plot(kind='bar', color='blue')
plt.title("Feature Correlation with Loan Approval")
plt.xlabel("Features")
plt.ylabel("Correlation")
plt.xticks(rotation=45)
plt.show()
