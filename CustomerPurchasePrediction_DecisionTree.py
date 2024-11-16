import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Step 1: Generate a synthetic dataset
np.random.seed(42)
data = {
    "PreviousPurchases": np.random.randint(1, 50, 200),  # Random number of previous purchases
    "Age": np.random.randint(18, 70, 200),              # Random age between 18 and 70
    "Purchase": np.random.choice([0, 1], size=200, p=[0.6, 0.4])  # Binary target variable
}
df = pd.DataFrame(data)

# Step 2: Prepare the data
X = df[['PreviousPurchases', 'Age']]
y = df['Purchase']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the decision tree classifier
model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 5: Visualize the decision tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=X.columns, class_names=["No Purchase", "Purchase"], filled=True)
plt.title("Decision Tree for Customer Purchasing Behavior")
plt.show()

# Step 6: Interpret the decision tree
decision_tree_rules = export_text(model, feature_names=list(X.columns))
print("Decision Tree Rules:")
print(decision_tree_rules)

# Step 7: Predict for a new customer
new_customer = pd.DataFrame([[10, 30]], columns=["PreviousPurchases", "Age"])
prediction = model.predict(new_customer)
print(f"Prediction for new customer: {'Purchase' if prediction[0] == 1 else 'No Purchase'}")
