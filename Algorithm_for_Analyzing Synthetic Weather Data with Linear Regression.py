import pandas as pd
import numpy as np

# Load the dataset
weather_data = pd.read_csv('D:\Synthetic_Weather_Data.csv')

# Check for missing values
print(weather_data.isnull().sum())

# Drop rows with missing 'Temperature' values
weather_data = weather_data.dropna(subset=['Temperature'])

# You may want to convert date strings to datetime objects
weather_data['Date'] = pd.to_datetime(weather_data['Date'])

# We'll use 'Date' as our feature for simplicity
weather_data['Year'] = weather_data['Date'].dt.year

# Optionally, add more features relevant to temperature, such as 'Month' or 'Day'
weather_data['Month'] = weather_data['Date'].dt.month

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Select features and target
X = weather_data[['Year', 'Month']]
y = weather_data['Temperature']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
