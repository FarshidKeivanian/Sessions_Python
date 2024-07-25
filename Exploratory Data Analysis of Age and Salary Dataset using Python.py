import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'James'],
    'Age': [28, 24, 35, 32, 29],
    'Salary': [50000, 62000, 75000, 58000, 62000]
}
df = pd.DataFrame(data)

# Data Cleaning: Checking for missing values
print("Missing values:\n", df.isnull().sum())

# Descriptive Statistics
mean_salary = df['Salary'].mean()
median_age = df['Age'].median()
print("Mean Salary:", mean_salary)
print("Median Age:", median_age)

# Data Visualization
plt.figure(figsize=(10, 5))

# Scatter plot
plt.subplot(1, 2, 1)
plt.scatter(df['Age'], df['Salary'], color='blue')
plt.title('Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

# Histogram
plt.subplot(1, 2, 2)
plt.hist(df['Salary'], bins=5, color='green')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
