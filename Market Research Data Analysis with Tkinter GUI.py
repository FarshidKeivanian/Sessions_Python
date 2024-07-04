# pip install pandas matplotlib tkinter requests

import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, messagebox
import requests
from io import StringIO

# Function to fetch data from a URL
def fetch_data(url):
    response = requests.get(url)
    data = StringIO(response.text)
    return pd.read_csv(data)

# URL for sample dataset
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'

# Fetch and create a DataFrame
df = fetch_data(url)

# Check the columns in the DataFrame
print("Columns in the DataFrame:", df.columns)

# Clean column names by stripping extra spaces and quotes
df.columns = [col.strip().strip('"') for col in df.columns]

# Check the cleaned columns
print("Cleaned columns in the DataFrame:", df.columns)

# Rename and select columns if they exist
if 'Index' in df.columns and 'Height(Inches)' in df.columns and 'Weight(Pounds)' in df.columns:
    df = df[['Index', 'Height(Inches)', 'Weight(Pounds)']].rename(
        columns={'Index': 'CustomerID', 'Height(Inches)': 'Age', 'Weight(Pounds)': 'SatisfactionScore'}
    )
else:
    raise KeyError("Required columns are not found in the dataset")

# Calculate average satisfaction score
avg_satisfaction = df['SatisfactionScore'].mean()

def show_avg_satisfaction():
    messagebox.showinfo("Average Satisfaction Score", f"Average Satisfaction Score: {avg_satisfaction:.2f}")

def plot_satisfaction_score():
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Age'], df['SatisfactionScore'], color='blue')
    plt.title('Satisfaction Score by Age')
    plt.xlabel('Age')
    plt.ylabel('Satisfaction Score')
    plt.grid(True)
    plt.show()

# Create the main window
root = Tk()
root.title("Market Research Analysis")

# Create and place widgets
label = Label(root, text="Market Research Data Analysis", font=("Helvetica", 16))
label.pack(pady=10)

avg_button = Button(root, text="Show Average Satisfaction Score", command=show_avg_satisfaction)
avg_button.pack(pady=5)

plot_button = Button(root, text="Plot Satisfaction Score by Age", command=plot_satisfaction_score)
plot_button.pack(pady=5)

# Run the application
root.mainloop()
