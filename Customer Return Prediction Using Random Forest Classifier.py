import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Sample data creation (this should be replaced with actual data loading)
data = {
    'Total Spend': [100, 50, 300, 200, 30],
    'Number of Visits': [4, 2, 7, 5, 1],
    'Time Since Last Visit': [7, 30, 3, 15, 60],
    'Purchased On Sale Items': [1, 0, 1, 0, 0],
    'Returned': [1, 0, 1, 0, 0]
}
df = pd.DataFrame(data)

# Features and target variable
X = df.drop('Returned', axis=1)
y = df['Returned']

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predicting test results
y_pred = model.predict(X_test)

# Evaluating the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
