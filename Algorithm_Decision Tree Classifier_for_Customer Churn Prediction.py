# Install required libraries (Colab usually has these pre-installed, but just in case)
!pip install pandas numpy matplotlib seaborn scikit-learn

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# Step 1: Upload the dataset
print(" Please upload Modified_Telco_Customer_Churn_Dataset_for_ML_Prediction_Analysis.csv")
uploaded = files.upload()

# Load the dataset
file_name = list(uploaded.keys())[0]
data = pd.read_csv(file_name)

# Step 2: Preprocess 'TotalCharges' and 'tenure'
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data.dropna(subset=['TotalCharges', 'tenure'], inplace=True)

# Create 'MonthlyCharges' if not present
data['MonthlyCharges'] = data['TotalCharges'] / (data['tenure'] + 1)  # Avoid divide-by-zero

# Convert 'Churn' to binary
data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})

# ------------------ Visualizations ------------------
plt.figure(figsize=(14, 6))

# Histogram for 'tenure'
plt.subplot(2, 2, 1)
sns.histplot(data['tenure'], kde=True, color='skyblue', bins=30)
plt.title('Tenure Distribution')

# Histogram for 'TotalCharges'
plt.subplot(2, 2, 2)
sns.histplot(data['TotalCharges'], kde=True, color='salmon', bins=30)
plt.title('TotalCharges Distribution')

# Count plot for 'Churn'
plt.subplot(2, 2, 3)
sns.countplot(x='Churn', data=data, palette='pastel')
plt.title('Churn Distribution')

# Count plot for 'SeniorCitizen'
plt.subplot(2, 2, 4)
sns.countplot(x='SeniorCitizen', data=data, palette='coolwarm')
plt.title('SeniorCitizen Distribution')

plt.tight_layout()
plt.show()

# MonthlyCharges histogram
plt.figure(figsize=(6, 4))
sns.histplot(data['MonthlyCharges'], kde=True, color='lightgreen', bins=30)
plt.title('MonthlyCharges Distribution')
plt.xlabel('MonthlyCharges')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Correlation Matrix
numeric_data = data.select_dtypes(include=[np.number])
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap='Reds')
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Box plot for 'tenure' vs 'Churn'
plt.figure(figsize=(14, 6))
plt.subplot(1, 2, 1)
sns.boxplot(x='Churn', y='tenure', data=data, palette='pastel')
plt.title('Tenure vs. Churn')

# Scatter plot for 'MonthlyCharges' vs 'Churn'
plt.subplot(1, 2, 2)
sns.scatterplot(x='MonthlyCharges', y='Churn', data=data, hue='Churn', alpha=0.5)
plt.title('MonthlyCharges vs. Churn')

plt.tight_layout()
plt.show()

# Extra: Box plot for 'MonthlyCharges' vs 'Churn'
plt.figure(figsize=(6, 4))
sns.boxplot(x='Churn', y='MonthlyCharges', data=data, palette='Set2')
plt.title('MonthlyCharges by Churn')
plt.tight_layout()
plt.show()

# ------------------ Machine Learning Model ------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Define features and target
X = data.drop('Churn', axis=1)
y = data['Churn']

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing pipeline
numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
numeric_transformer = StandardScaler()

categorical_features = ['SeniorCitizen']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Pipeline with Random Forest
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))
print("--- Confusion Matrix ---")
print(confusion_matrix(y_test, y_pred))
