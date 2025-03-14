import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/house_price_dataset_ISY503.csv"
df = pd.read_csv(url)

# Display first few rows to check the dataset structure
print(df.head())

# One-hot encode categorical feature (Location)
df = pd.get_dummies(df, columns=['Location'], drop_first=True)

# Features and target variable
X = df.drop(columns=['Price'])
y = df['Price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Predictions
y_pred_linear = lr.predict(X_test)

# Evaluate Linear Regression
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print(f"Linear Regression - MSE: {mse_linear:.2f}, R² Score: {r2_linear:.4f}")
