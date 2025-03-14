import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample dataset
np.random.seed(42)
size = np.random.randint(500, 4000, 100)  # House size (sq ft)
age = np.random.randint(1, 50, 100)  # Age of the house
location = np.random.choice(['Urban', 'Suburban', 'Rural'], 100)  # Location categories
price = 1000 + (size * 150) - (age * 200) + np.random.randint(-5000, 5000, 100)  # Price formula

# Create DataFrame
df = pd.DataFrame({'Size': size, 'Age': age, 'Location': location, 'Price': price})

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
