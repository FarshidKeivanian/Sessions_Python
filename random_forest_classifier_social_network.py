import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv('social_network.csv')

# Step 2: Data Preprocessing (if necessary)

# Step 3: Feature Engineering

# Step 4: Split the data into training and testing sets
X = data.drop('connected', axis=1)  # Assuming 'connected' is the target variable
y = data['connected']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Algorithm Selection
model = RandomForestClassifier()

# Step 6: Train the algorithm
model.fit(X_train, y_train)

# Step 7: Evaluate Performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Tune Hyperparameters (if necessary)

# Step 9: Make Predictions (on new data, if available)
