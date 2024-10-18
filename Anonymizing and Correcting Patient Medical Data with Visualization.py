import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create a sample dataset with sensitive information
data = {
    'Patient_ID': ['P001', 'P002', 'P003', 'P004', 'P005'],
    'Name': ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob Clark', 'Eve Davis'],
    'Age': [45, 34, 29, 40, 51],
    'Diagnosis': ['Diabetes', 'Hypertension', 'Asthma', 'Diabetes', 'Hypertension'],
    'Medical_Bill': [1500, 2500, 1200, 1800, 2200]
}

df = pd.DataFrame(data)

# Step 2: Print the original dataset (for visualization)
print("Original Dataset:")
print(df)

# Step 3: Anonymize sensitive data (replace names with unique IDs)
df['Name'] = df['Patient_ID']  # Replace names with anonymized Patient IDs

# Step 4: Introduce data correction (Fixing inaccurate records)
# Let's assume we discovered a billing error for the second patient
df.loc[df['Patient_ID'] == 'P002', 'Medical_Bill'] = 2600  # Correct the billing error

# Step 5: Visualize the corrected and anonymized dataset
print("\nAnonymized and Corrected Dataset:")
print(df)

# Step 6: Data visualization: Bar plot for Medical Bills by Diagnosis
plt.figure(figsize=(8, 5))
df.groupby('Diagnosis')['Medical_Bill'].mean().plot(kind='bar', color=['#4CAF50', '#FF9800', '#2196F3'])
plt.title('Average Medical Bill by Diagnosis (Anonymized Data)')
plt.xlabel('Diagnosis')
plt.ylabel('Average Medical Bill (USD)')
plt.show()
