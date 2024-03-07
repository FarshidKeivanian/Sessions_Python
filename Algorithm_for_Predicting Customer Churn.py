#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load dataset
df = pd.read_csv('telecom_customer_churn.csv')

# Data Preprocessing
# Handling missing values
df.dropna(inplace=True)

# Encoding categorical variables
df = pd.get_dummies(df, columns=['contract', 'internet_service', 'payment_method'])

# Scaling numerical features
scaler = StandardScaler()
numerical_cols = ['tenure', 'monthly_charges', 'total_charges']
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Exploratory Data Analysis (EDA)
# Visualizing distributions
sns.histplot(data=df, x='tenure', hue='churn', kde=True)
plt.title('Distribution of Tenure by Churn Status')
plt.show()

# Correlation matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Feature Engineering (if applicable)
# No feature engineering in this simplified example

# Model Building
# Splitting the data into training and testing sets
X = df.drop('churn', axis=1)
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting Logistic Regression model
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Model Evaluation
# Predicting on test set
y_pred = log_reg.predict(X_test)

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()


# In[ ]:




