import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset from the provided URL
url = 'https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/Synthetic%20Customer%20Churn.csv'
data = pd.read_csv(url)

# Feature selection
X = data[['Age', 'Income', 'ContractType']]
y = data['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction on test set and evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Prompt user for input values
age = float(input("Enter the customer's age: "))
income = float(input("Enter the customer's income: "))
contract_type = int(input("Enter the contract type (e.g., 0 for Monthly, 1 for Annual, 2 for Two-year): "))

# Predict churn for the new customer based on user input
new_customer_data = [[age, income, contract_type]]
predicted_churn = model.predict(new_customer_data)

# Display the result
if predicted_churn[0] == 1:
    print("The model predicts that this customer is likely to churn.")
else:
    print("The model predicts that this customer is not likely to churn.")
