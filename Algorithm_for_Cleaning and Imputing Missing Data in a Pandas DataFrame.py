import pandas as pd

# Sample data
data = {'Name': ['John Doe', 'Jane Smith', ''],
        'Age': [28, 34, None],
        'Salary': [50000, 60000, 45000]}
df = pd.DataFrame(data)

# Data Wrangling Steps
# 1. Cleaning: Removing rows with empty 'Name'.
df_cleaned = df[df['Name'] != ''].copy()  # Use .copy() to avoid SettingWithCopyWarning

# 2. Filling missing values in 'Age' with the average age.
average_age = df_cleaned['Age'].mean()  # Compute the average once to avoid recalculating
df_cleaned['Age'].fillna(average_age, inplace=True)

print(df_cleaned)