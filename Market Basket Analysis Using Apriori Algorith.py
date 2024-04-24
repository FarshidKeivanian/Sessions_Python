# Importing necessary libraries
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# List of transactions, where each transaction is a list of items
transactions = [
    ['Bread', 'Milk'],
    ['Bread', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Diaper', 'Beer', 'Cola'],
    ['Bread', 'Milk', 'Diaper', 'Beer'],
    ['Bread', 'Milk', 'Diaper', 'Cola']
]

# Initializing TransactionEncoder to transform the list format into an array format suitable for the Apriori algorithm
encoder = TransactionEncoder()
transaction_array = encoder.fit_transform(transactions)

# Creating a pandas DataFrame from the encoded array, where columns correspond to items
df = pd.DataFrame(transaction_array, columns=encoder.columns_)

# Applying the Apriori algorithm with a minimum support of 0.6 (3 out of 5 transactions)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# Displaying the frequent itemsets found
print(frequent_itemsets)
