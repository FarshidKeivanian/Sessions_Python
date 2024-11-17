import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset from the provided URL
url = 'https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/synthetic_healthcare_data.csv'
df = pd.read_csv(url)

# Prepare data for modeling
X = df.drop(columns=["recovery_rate"])
y = df["recovery_rate"]

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print model performance
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)

# Check for data diversity to ensure fairness
demographics_counts = df[['gender_Male', 'gender_Female']].sum()
print("Demographics Diversity:")
print(demographics_counts)

treatment_counts = df[['treatment_type_Standard', 'treatment_type_Intensive']].sum()
print("\nTreatment Diversity:")
print(treatment_counts)

# Interactive Prediction with Detailed Prompts
def interactive_prediction(model, feature_columns):
    print("\nEnter the required information for each feature below:")
    user_input = {}

    # Feature descriptions and valid inputs
    feature_descriptions = {
        "age": "Age of the patient (Enter an integer between 0 and 120): ",
        "gender_Female": "Is the patient female? (Enter 1 for Yes, 0 for No): ",
        "gender_Male": "Is the patient male? (Enter 1 for Yes, 0 for No): ",
        "prior_conditions_Both": "Does the patient have both diabetes and hypertension? (Enter 1 for Yes, 0 for No): ",
        "prior_conditions_Diabetes": "Does the patient have diabetes only? (Enter 1 for Yes, 0 for No): ",
        "prior_conditions_Hypertension": "Does the patient have hypertension only? (Enter 1 for Yes, 0 for No): ",
        "prior_conditions_None": "Does the patient have no prior medical conditions? (Enter 1 for Yes, 0 for No): ",
        "treatment_type_Intensive": "Did the patient receive intensive treatment? (Enter 1 for Yes, 0 for No): ",
        "treatment_type_Standard": "Did the patient receive standard treatment? (Enter 1 for Yes, 0 for No): ",
        "lifestyle_indicator_Active": "Is the patient's lifestyle active? (Enter 1 for Yes, 0 for No): ",
        "lifestyle_indicator_Moderate": "Is the patient's lifestyle moderately active? (Enter 1 for Yes, 0 for No): ",
        "lifestyle_indicator_Sedentary": "Is the patient's lifestyle sedentary? (Enter 1 for Yes, 0 for No): "
    }

    # Collect input for each feature with a hint
    for feature in feature_columns:
        while True:
            try:
                user_input[feature] = float(input(feature_descriptions[feature]))
                break
            except ValueError:
                print(f"Invalid input. Please enter a valid value for {feature}.")

    # Convert input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Predict the output
    prediction = model.predict(input_df)[0]

    # Explain the prediction
    print("\nPrediction Result:")
    print(f"The predicted recovery rate is: {prediction}")
    print("This prediction is based on the input features you provided, "
          "using patterns learned from the training data.")

# Interactive input features
print("\nReady to make a prediction? Provide the following information:")
interactive_features = list(X.columns)
interactive_prediction(model, interactive_features)
