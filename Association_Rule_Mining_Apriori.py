import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Step 1: Data Collection
# This is a hypothetical example of transactional data
dataset = [
    ['Milk', 'Onions', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
    ['Dill', 'Onions', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
    ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
    ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
    ['Corn', 'Onions', 'Onions', 'Kidney Beans', 'Ice cream', 'Eggs']
]

# Step 2: Data Preparation
encoder = TransactionEncoder()
transaction_matrix = encoder.fit_transform(dataset)
df = pd.DataFrame(transaction_matrix, columns=encoder.columns_)

# Step 3: Setting Parameters
# Support at least 3% of the transactions
# Adjust the min_support accordingly (0.03 in this example as a placeholder)
min_support = 0.03
min_confidence = 0.5

# Step 4: Rule Generation
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)

# Step 5: Rule Evaluation
# Filtering rules based on a confidence level and lift
rules = rules[(rules['lift'] >= 1) & (rules['confidence'] >= min_confidence)]

print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
