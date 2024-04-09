import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Sample Data Creation
data = {'Size': [1500, 1800, 2400, 3000, 3500], 'Price': [400000, 500000, 600000, 650000, 700000]}
df = pd.DataFrame(data)

# Data Cleaning: Removing outliers or errors in the data (assuming none for this example)
# df = df[df['Size'] < some_threshold]

# Model Selection and Feature Selection
X = df[['Size']]  # Independent variable
y = df['Price']  # Dependent variable

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model Training
model = LinearRegression()
model.fit(X_train, y_train)

# Model Validation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualization
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('House Price Prediction')
plt.xlabel('Size (sq ft)')
plt.ylabel('Price ($)')
plt.show()
