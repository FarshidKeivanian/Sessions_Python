import matplotlib.pyplot as plt
import numpy as np

# Hypothetical data
months = np.arange(1, 13)  # 12 months
sales_before_erp = np.random.normal(loc=50000, scale=5000, size=12)
sales_after_erp = sales_before_erp * (1 + np.random.normal(loc=0.1, scale=0.05, size=12))  # 10% increase on average

plt.figure(figsize=(10, 6))
plt.plot(months, sales_before_erp, label='Sales Before ERP', marker='o')
plt.plot(months, sales_after_erp, label='Sales After ERP', marker='o')
plt.title('Impact of ERP on Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True)
plt.show()
