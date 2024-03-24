import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'warm_blooded': [1, 1, 0, 0, 1],  # 1: Yes, 0: No
    'lays_eggs': [0, 0, 1, 1, 0],  # 1: Yes, 0: No
    'label': ['mammal', 'mammal', 'reptile', 'reptile', 'mammal']  # Target variable
}
df = pd.DataFrame(data)

# Features and target variable
X = df[['warm_blooded', 'lays_eggs']]
y = df['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
predictions = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, predictions))
