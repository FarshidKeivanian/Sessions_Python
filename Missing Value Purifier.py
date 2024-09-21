import pandas as pd
import numpy as np

# Create data with missing values
data = {'A': [1, 4, np.nan], 'B': [np.nan, 5, 7], 'C': [3, np.nan, 9]}
df = pd.DataFrame(data)

# Show DataFrame before dropping rows
print("DataFrame before dropping missing values:")
print(df)

# Display missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Show DataFrame after dropping rows
print("\nDataFrame after dropping missing values:")
print(df)
