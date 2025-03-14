import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset from GitHub
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/house_price_dataset_ISY503.csv"
df = pd.read_csv(url)

# Display first few rows
print(df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

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

# Predictions for Linear Regression
y_pred_linear = lr.predict(X_test)

# Evaluate Linear Regression
mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

print(f"Linear Regression - MSE: {mse_linear:.2f}, R² Score: {r2_linear:.4f}")

# Train Polynomial Regression model (Degree 2)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_lr = LinearRegression()
poly_lr.fit(X_train_poly, y_train)

# Predictions for Polynomial Regression
y_pred_poly = poly_lr.predict(X_test_poly)

# Evaluate Polynomial Regression
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"Polynomial Regression (Degree 2) - MSE: {mse_poly:.2f}, R² Score: {r2_poly:.4f}")

# Compare model performance
models = ['Linear Regression', 'Polynomial Regression (Degree 2)']
mse_values = [mse_linear, mse_poly]
r2_values = [r2_linear, r2_poly]

# Plot Model Performance Comparison
plt.figure(figsize=(6, 4))
plt.bar(models, mse_values, color=['blue', 'orange'])
plt.title("Mean Squared Error Comparison")
plt.ylabel("MSE")
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(models, r2_values, color=['blue', 'orange'])
plt.title("R² Score Comparison")
plt.ylabel("R² Score")
plt.ylim(0, 1)  # R² Score range
plt.show()
