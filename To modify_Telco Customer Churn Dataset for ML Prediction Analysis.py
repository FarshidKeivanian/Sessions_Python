import pandas as pd

# Load the dataset from a specified path
file_path = 'D:\\Telco_Customer_Churn_Dataset_for_ML_Prediction_Analysis.csv'
df = pd.read_csv(file_path)

# Remove the specified attributes
df_modified = df.drop(columns=['MonthlyCharges', 'OnlineSecurity', 'StreamingTV', 'InternetService', 'Partner'])

# Specify the path where you want to save the modified dataset
save_path = 'D:\\Modified_Telco_Customer_Churn_Dataset_for_ML_Prediction_Analysis.csv'

# Save the modified dataset
df_modified.to_csv(save_path, index=False)
