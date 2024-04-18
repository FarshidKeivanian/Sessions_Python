import matplotlib.pyplot as plt
import numpy as np

# Days of the month
days = np.arange(1, 31)

# Random sales data generation
sales = np.random.randint(100, 500, size=30)  # Simulated daily sales in thousands
payments = np.random.randint(50, 450, size=30)  # Simulated daily payments received in thousands

# Cumulative cash flow calculation
cumulative_cash_flow = np.cumsum(payments - sales)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(days, cumulative_cash_flow, marker='o', linestyle='-', color='b')
plt.title('Simulated Daily Cash Flow for Global Bike Inc. Australia')
plt.xlabel('Day of the Month')
plt.ylabel('Cumulative Cash Flow (in thousands)')
plt.grid(True)
plt.show()
