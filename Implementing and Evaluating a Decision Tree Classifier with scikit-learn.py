from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Example dataset
# Replace this with the actual dataset
X = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
y = [0, 1, 0, 1, 0]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(10, 8))
plot_tree(model, filled=True)
plt.title("Decision Tree")
plt.show()
