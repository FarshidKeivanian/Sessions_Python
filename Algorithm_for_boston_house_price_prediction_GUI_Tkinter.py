import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import simpledialog, messagebox

# Load the dataset from the uploaded file path
data = pd.read_csv('D:/boston_house_prices_corrected.csv')

# Split data into features and target
features = data.columns[:-1]  # Extract feature names
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Split dataset into training and testing parts
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Function to display feature explanations
def show_feature_descriptions():
    descriptions = [
        "CRIM: Per capita crime rate by town",
        "ZN: Proportion of residential land zoned for lots over 25,000 sq.ft.",
        "INDUS: Proportion of non-retail business acres per town.",
        "CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise).",
        "NOX: Nitric oxides concentration (parts per 10 million).",
        "RM: Average number of rooms per dwelling.",
        "AGE: Proportion of owner-occupied units built prior to 1940.",
        "DIS: Weighted distances to five Boston employment centres.",
        "RAD: Index of accessibility to radial highways.",
        "TAX: Full-value property-tax rate per $10,000.",
        "PTRATIO: Pupil-teacher ratio by town.",
        "B: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town.",
        "LSTAT: % lower status of the population."
    ]
    messagebox.showinfo("Feature Descriptions", "\n".join(descriptions))

# Function to get user inputs and predict house price
def predict_price():
    # Display feature explanations to the user
    show_feature_descriptions()

    # Create input form using tkinter
    root = tk.Tk()
    root.title("House Price Prediction")
    
    # Get user inputs
    inputs = []
    for i, feature_name in enumerate(features):
        input_value = simpledialog.askfloat("Input Feature", f"Enter value for {feature_name} (Feature {i + 1}):")
        inputs.append(input_value)
    
    # Make a prediction
    prediction = lr.predict([inputs])
    
    # Display prediction
    result_label = tk.Label(root, text=f'Predicted House Price: ${prediction[0]:.2f}')
    result_label.pack()
    
    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.pack()

    root.mainloop()

# Start the function
predict_price()
