# pip install pandas matplotlib seaborn tkinter requests

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Label, Button, messagebox, Frame, BOTH
import numpy as np

# Create a synthetic dataset
np.random.seed(42)
data = {
    'CustomerID': range(1, 201),
    'Age': np.random.randint(18, 80, 200),
    'SatisfactionScore': np.random.randint(50, 150, 200)
}
df = pd.DataFrame(data)

# Perform customer segmentation based on age groups
bins = [0, 20, 40, 60, 80, 100]
labels = ['0-20', '21-40', '41-60', '61-80', '81-100']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Calculate average satisfaction score for each age group
avg_satisfaction_by_age_group = df.groupby('AgeGroup')['SatisfactionScore'].mean().reset_index()

# Calculate overall average satisfaction score
avg_satisfaction = df['SatisfactionScore'].mean()

def show_avg_satisfaction():
    messagebox.showinfo("Average Satisfaction Score", f"Overall Average Satisfaction Score: {avg_satisfaction:.2f}")

def plot_satisfaction_score_by_age_group():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='AgeGroup', y='SatisfactionScore', data=avg_satisfaction_by_age_group, palette='viridis')
    plt.title('Average Satisfaction Score by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Satisfaction Score')
    plt.grid(True)
    plt.show()

def show_segmentation_details():
    segmentation_details = df.groupby('AgeGroup').agg({'CustomerID': 'count', 'SatisfactionScore': 'mean'}).reset_index()
    details = segmentation_details.to_string(index=False)
    messagebox.showinfo("Customer Segmentation Details", details)

# Create the main window
root = Tk()
root.title("Customer Segmentation and CRM Data Analysis")
root.geometry("400x300")

# Create a frame for the widgets
frame = Frame(root)
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Create and place widgets
label = Label(frame, text="Customer Segmentation and CRM Data Analysis", font=("Helvetica", 16))
label.pack(pady=10)

avg_button = Button(frame, text="Show Overall Average Satisfaction Score", command=show_avg_satisfaction)
avg_button.pack(pady=5)

plot_button = Button(frame, text="Plot Satisfaction Score by Age Group", command=plot_satisfaction_score_by_age_group)
plot_button.pack(pady=5)

details_button = Button(frame, text="Show Segmentation Details", command=show_segmentation_details)
details_button.pack(pady=5)

# Run the application
root.mainloop()
