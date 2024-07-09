# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Generating synthetic dataset
np.random.seed(0)
age = np.random.randint(20, 70, 100)
cholesterol = np.random.randint(150, 250, 100)
blood_pressure = 0.5 * age + 0.3 * cholesterol + np.random.normal(0, 10, 100)

data = pd.DataFrame({
    'age': age,
    'cholesterol': cholesterol,
    'blood_pressure': blood_pressure
})

# Data cleaning
data.dropna(inplace=True)

# Exploratory Data Analysis
plt.scatter(data['age'], data['blood_pressure'])
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.show()

# Feature selection
X = data[['age', 'cholesterol']]
y = data['blood_pressure']

# Model building
model = LinearRegression()
model.fit(X, y)

# Model evaluation
print(f'R-squared: {model.score(X, y)}')
