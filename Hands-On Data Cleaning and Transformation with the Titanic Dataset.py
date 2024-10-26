import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset directly from GitHub
url = 'https://github.com/datasciencedojo/datasets/raw/master/titanic.csv'
df = pd.read_csv(url)

# Display the first few rows to understand the dataset structure
print("First few rows of the dataset:")
print(df.head())

# Step 1: Data Cleaning
# Remove rows with missing values in critical columns ('Age' and 'Fare')
df_cleaned = df.dropna(subset=['Age', 'Fare']).copy()

# Fill missing values in the 'Embarked' column with the most common value
most_common_embarked = df_cleaned['Embarked'].mode()[0]
df_cleaned.loc[:, 'Embarked'] = df_cleaned['Embarked'].fillna(most_common_embarked)

# Fill missing values in 'Age' with the average age
average_age = df_cleaned['Age'].mean()
df_cleaned.loc[:, 'Age'] = df_cleaned['Age'].fillna(average_age)

print("\nData after cleaning:")
print(df_cleaned.head())

# Step 2: Data Transformation
# Convert categorical columns like 'Sex' and 'Embarked' to numerical format
df_cleaned.loc[:, 'Sex'] = df_cleaned['Sex'].map({'male': 1, 'female': 0})
df_cleaned = pd.get_dummies(df_cleaned, columns=['Embarked'], drop_first=True)

# Create a new column 'FamilySize' as the sum of 'SibSp' and 'Parch'
df_cleaned.loc[:, 'FamilySize'] = df_cleaned['SibSp'] + df_cleaned['Parch']

print("\nData after transformation:")
print(df_cleaned[['Sex', 'FamilySize', 'Embarked_Q', 'Embarked_S']].head())

# Step 3: Data Aggregation
# Calculate the average fare per passenger class and display it
avg_fare_per_class = df_cleaned.groupby('Pclass')['Fare'].mean()
print("\nAverage Fare per Passenger Class:")
print(avg_fare_per_class)

# Plotting the average fare per passenger class
avg_fare_per_class.plot(kind='bar', title='Average Fare per Passenger Class', ylabel='Average Fare')
plt.show()
