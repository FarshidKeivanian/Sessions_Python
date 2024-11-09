# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (update the path if using a local file)
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/boston_house_prices_corrected.csv"
data = pd.read_csv(url)

# Display the column names to verify target variable's name
print("Column names in the dataset:", data.columns)

# Basic data cleaning (if necessary)
data = data.dropna()  # Dropping rows with missing values, if any

# Verify and update target column name based on actual data
target_column = 'PRICE' if 'PRICE' in data.columns else data.columns[-1]  # Assuming last column if PRICE isn't found

# Plotting the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Features")
plt.show()

# Visualize relationship of key features with the target (Price)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x="RM", y=target_column, hue=target_column, palette="viridis")
plt.title("Relationship between Number of Rooms (RM) and House Price (PRICE)")
plt.xlabel("Average Number of Rooms")
plt.ylabel("House Price")
plt.show()

# Define features and target variable using the correct column name
X = data[['RM', 'LSTAT', 'PTRATIO']]  # Using RM, LSTAT, PTRATIO as features
y = data[target_column]  # Target variable

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predicting house prices on the test set
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Plotting actual vs predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=3)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
