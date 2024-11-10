import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset from the provided URL
url = 'https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/student_scores.csv'
data = pd.read_csv(url)

# Feature selection
X = data[['StudyHours', 'PreviousScores']]
y = data['Score']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2}")
