import pandas as pd
import pyodbc
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np

# Step 1: Define connection parameters
server = 'DESKTOP-2UAHBMR\\SQLSERVER2022'  # Replace with your actual server name
database = 'TestDB'  # Your database name
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure the correct ODBC driver is installed

# Step 2: Establish the connection using Windows Authentication (Trusted Connection)
connection = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)
cursor = connection.cursor()

# Step 3: Query the cleaned data directly from the database
query = """
SELECT *
FROM Book_Reviews
WHERE Rating IS NOT NULL AND Review_Text != '';
"""
data = pd.read_sql_query(query, connection)

# Step 4: Add a new column for review length
data['Review_Length'] = data['Review_Text'].apply(len)

# Step 5: Create labels for popularity (1 for 'Yes', 0 for 'No')
data['Popular'] = data['Rating'].apply(lambda x: 1 if x >= 4 else 0)

# Step 6: Prepare data for training
X = data[['Rating', 'Review_Length']]  # Features: Rating and Review_Length
y = data['Popular']  # Target variable: Popular

# Optional: Normalize features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 8: Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)

# Step 9: Save the predictions back to the database
# Adding predictions to the test set for saving
test_data = pd.DataFrame(X_test, columns=['Rating', 'Review_Length'])
test_data['Popular_Predicted'] = predictions
test_data['Popular_Actual'] = y_test.values

# Insert predictions back into the database
cursor.execute("IF OBJECT_ID('Predictions', 'U') IS NOT NULL DROP TABLE Predictions;")
cursor.execute("""
CREATE TABLE Predictions (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    Rating FLOAT,
    Review_Length INT,
    Popular_Predicted INT,
    Popular_Actual INT
);
""")
for _, row in test_data.iterrows():
    cursor.execute(
        """
        INSERT INTO Predictions (Rating, Review_Length, Popular_Predicted, Popular_Actual)
        VALUES (?, ?, ?, ?);
        """,
        float(row['Rating']), int(row['Review_Length']),
        int(row['Popular_Predicted']), int(row['Popular_Actual'])
    )

connection.commit()

# Step 10: Close the connection
cursor.close()
connection.close()

# Optional: Display the predictions
print(test_data)
