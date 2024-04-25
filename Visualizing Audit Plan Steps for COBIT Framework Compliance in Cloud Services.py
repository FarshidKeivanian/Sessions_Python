import matplotlib.pyplot as plt  # Importing the necessary library

# Steps in the Audit Plan
steps = [
    "Define Audit Objectives",
    "Identify Relevant COBIT Processes",
    "Prepare Audit Checklist",
    "Conduct Fieldwork",
    "Analyze Findings",
    "Report and Recommendations"
]

# Creating a pie chart for visual representation
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie([1]*len(steps), labels=steps, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(range(len(steps))))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title('Audit Plan Steps Based on COBIT for a Cloud Service Provider')
plt.show()
