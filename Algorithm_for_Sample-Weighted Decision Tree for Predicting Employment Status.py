import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# The modified dataset based on the uploaded data table
# Age and salary are represented as the midpoints of their respective ranges

data = [
    ['sales', 'senior', 33, 47500, 30],
    ['sales', 'junior', 28, 27500, 40],
    ['sales', 'junior', 33, 32500, 40],
    ['systems', 'junior', 23, 47500, 20],
    ['systems', 'senior', 33, 67500, 5],
    ['systems', 'junior', 28, 47500, 3],
    ['systems', 'senior', 43, 67500, 3],
    ['marketing', 'senior', 38, 47500, 10],
    ['marketing', 'junior', 33, 42500, 4],
    ['secretary', 'senior', 48, 37500, 4],
    ['secretary', 'junior', 28, 27500, 6]
]

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data, columns=['department', 'status', 'age', 'salary', 'count'])

# Convert categorical variables into numeric variables
df['department'] = df['department'].astype('category').cat.codes
df['status'] = df['status'].map({'junior': 0, 'senior': 1}).astype(int)

# Feature matrix and target array
X = df[['department', 'age', 'salary']].values
y = df['status'].values
sample_weight = df['count'].values  # The 'count' column as the sample weight for each instance

# Create the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
# Fit it to the data, using the 'count' as sample weight
clf.fit(X, y, sample_weight=sample_weight)

# Plot the decision tree
plt.figure(figsize=(20,10))
plot_tree(clf, filled=True, feature_names=['department', 'age', 'salary'], class_names=['junior', 'senior'])
plt.show()
