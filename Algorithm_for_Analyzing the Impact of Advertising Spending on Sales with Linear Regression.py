import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
advertising_spending = np.array([1.2, 1.5, 1.9, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5]).reshape(-1, 1)  # Reshape for sklearn
sales = np.array([58, 62, 67, 72, 77, 80, 82, 85, 88, 90, 95, 99])

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(advertising_spending, sales, color='blue', label='Data')
plt.xlabel('Advertising Spending ($K)')
plt.ylabel('Sales (K units)')
plt.title('Advertising Spending vs Sales')
plt.grid(True)

# Linear regression
regressor = LinearRegression()
regressor.fit(advertising_spending, sales)
predicted_sales = regressor.predict(advertising_spending)

# Plotting the regression line
plt.plot(advertising_spending, predicted_sales, color='red', label='Regression Line')
plt.legend()

# Show plot
plt.show()

# Coefficients
print('Intercept:', regressor.intercept_)
print('Coefficient:', regressor.coef_[0])
