import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Sales data over a year
data = {
 'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
 'Sales': [1500, 1600, 1700, 1400, 1800, 1900, 2000, 2100, 1800, 2200, 2300, 2500]
}

# Create a DataFrame
df = pd. DataFrame(data)

# Plotting the sales data
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()