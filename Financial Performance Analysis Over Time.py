import pandas as pd
import matplotlib.pyplot as plt

# Sample financial data
data = {
    'Year': [2021, 2022, 2023],
    'Revenue': [100000, 150000, 200000],
    'Expenses': [50000, 70000, 90000],
    'Profit': [50000, 80000, 110000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot Revenue, Expenses, and Profit
plt.plot(df['Year'], df['Revenue'], marker='o', label='Revenue')
plt.plot(df['Year'], df['Expenses'], marker='o', label='Expenses')
plt.plot(df['Year'], df['Profit'], marker='o', label='Profit')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Financial Performance Analysis Over Time')
plt.legend()
plt.grid(True)
plt.show()
