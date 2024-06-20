#For Windows: pip install pandas numpy matplotlib seaborn scikit-learn
#For macOS package Python 3.x: pip3 install pandas numpy matplotlib seaborn scikit-learn

# Importing necessary libraries
import pandas as pd # For data manipulation and analysis
import numpy as np # For numerical operations
import matplotlib.pyplot as plt # For plotting graphs
import seaborn as sns # For statistical data visualization

# Load the dataset
file_path = 'D:\\Modified_Telco_Customer_Churn_Dataset_for_ML_Prediction_Analysis.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Preprocess 'TotalCharges': Convert to numeric and handle errors by setting invalid parsing as NaN, then dropping them
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data.dropna(subset=['TotalCharges'], inplace=True)

print(data)
# Convert the 'Churn' column to binary (1 for 'Yes' and 0 for 'No')
data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})
print(data)

# Visualizations
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

# Correlation Matrix for numerical features - exclude non-numeric data using select_dtypes()
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
if 'MonthlyCharges' not in data.columns:
    data['MonthlyCharges'] = data['TotalCharges'] / (data['tenure'] + 1)  # Adding 1 to avoid division by zero

plt.subplot(1, 2, 2)
sns.scatterplot(x='MonthlyCharges', y='Churn', data=data, hue='Churn', alpha=0.5)
plt.title('MonthlyCharges vs. Churn')
plt.tight_layout()
plt.show()


# Code: Machine Learning Model Development
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Define features and target
X = data.drop('Churn', axis=1)  # All other columns are features
y = data['Churn']  # Target is the Churn column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define preprocessing for numeric and categorical features
numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
numeric_transformer = StandardScaler()

categorical_features = ['SeniorCitizen']  # Add other categorical features here
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Create the model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('classifier', RandomForestClassifier(random_state=42))])

# Train the model
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
