#pip install statsmodels matplotlib seaborn

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Sales': [20000, 25000, 23000, 27000, 30000, 32000, 28000, 29000, 31000, 33000, 34000, 36000,
              38000, 39000, 37000, 40000, 42000, 43000, 45000, 47000, 48000, 49000, 51000, 53000],
    'Advertising_Spend': [5000, 5500, 5200, 5800, 6000, 6200, 5900, 6100, 6300, 6500, 6700, 6900,
                          7100, 7200, 7000, 7300, 7500, 7600, 7800, 8000, 8200, 8300, 8500, 8700],
    'Number_of_Promotions': [2, 3, 3, 4, 5, 5, 4, 5, 5, 6, 6, 7, 8, 8, 7, 9, 10, 10, 9, 11, 12, 12, 11, 13],
    'Temperature': [20, 22, 21, 23, 25, 27, 26, 28, 29, 30, 31, 32, 33, 34, 33, 35, 36, 37, 36, 38, 39, 40, 41, 42],
    'Foot_Traffic': [500, 550, 520, 580, 600, 620, 590, 610, 630, 650, 670, 690, 710, 720, 700, 730, 750, 760, 780, 800, 820, 830, 850, 870],
    'Season': [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
}
df = pd.DataFrame(data)

X = df[['Advertising_Spend', 'Number_of_Promotions', 'Temperature', 'Foot_Traffic', 'Season']]
X = sm.add_constant(X)
y = df['Sales']

model = sm.OLS(y, X).fit()
print(model.summary())

# Predicted values
df['Predicted_Sales'] = model.predict(X)

# Plotting actual vs predicted
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Predicted_Sales', data=df)
plt.plot([df['Sales'].min(), df['Sales'].max()], [df['Sales'].min(), df['Sales'].max()], 'r--')
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.show()
