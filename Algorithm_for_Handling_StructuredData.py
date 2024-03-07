#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Sample structured data: Customer transaction data
data = {
    'TransactionID': [1, 2, 3, 4],
    'CustomerID': ['C001', 'C002', 'C003', 'C001'],
    'TransactionAmount': [150.00, 200.00, 120.00, 300.00],
    'TransactionDate': ['2024-03-01', '2024-03-02', '2024-03-02', '2024-03-03']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Basic operation: Sum of all transaction amounts
total_transaction_amount = df['TransactionAmount'].sum()
print(f'Total Transaction Amount: {total_transaction_amount}')


# In[ ]:




