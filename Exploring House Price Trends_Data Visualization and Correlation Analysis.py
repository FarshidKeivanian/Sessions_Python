import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/house_price_dataset_ISY503.csv"
df = pd.read_csv(url)

# Display first few rows to check the dataset structure
print(df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df[['Size', 'Age', 'Price']].corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Scatter plot: Size vs Price
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Size'], y=df['Price'])
plt.title("House Size vs Price")
plt.xlabel("Size (sq ft)")
plt.ylabel("Price ($)")
plt.show()

# Scatter plot: Age vs Price
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df['Age'], y=df['Price'])
plt.title("House Age vs Price")
plt.xlabel("Age (years)")
plt.ylabel("Price ($)")
plt.show()
