#!/usr/bin/env python
# coding: utf-8

# In[6]:


# A basic data analysis example
#pip install --upgrade numexpr
#pip install --upgrade bottleneck
# Basic data analysis with Pandas
import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}
# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("DataFrame:")
print(df)

# Calculate average age and salary
avg_age = df['Age'].mean()
avg_salary = df['Salary'].mean()

print("\nAverage Age:", avg_age)
print("Average Salary:", avg_salary)


# In[ ]:




