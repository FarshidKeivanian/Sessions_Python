import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Existing Sample Data
data = {'Keywords': [0, 1, 0, 2, 1], 'Length': [200, 800, 300, 1000, 700], 'Links': [1, 3, 0, 5, 2], 'Spam': [0, 1, 0, 1, 1]}
df = pd.DataFrame(data)

# Increase the dataset size by generating more samples
additional_data = df.sample(20, replace=True, random_state=42)  # Increase the number here as needed
enlarged_df = pd.concat([df, additional_data]).reset_index(drop=True)

# Model Selection and Feature Selection
X = enlarged_df[['Keywords', 'Length', 'Links']]  # Independent variables
y = enlarged_df['Spam']  # Dependent variable

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Model Training
model = LogisticRegression()
model.fit(X_train, y_train)

# Model Validation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
