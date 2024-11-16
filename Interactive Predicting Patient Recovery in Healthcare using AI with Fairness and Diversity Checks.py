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
