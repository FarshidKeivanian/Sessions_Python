# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

# Set the seed for reproducibility
np.random.seed(42)

# Generate a dataset of 30 student GPAs, with some randomness
gpas = np.random.normal(loc=3.0, scale=0.5, size=30).clip(0, 4)

# Calculate mean, median, mode, and standard deviation
mean_gpa = np.mean(gpas)
median_gpa = np.median(gpas)
mode_gpa = stats.mode(gpas)[0][0]
std_dev_gpa = np.std(gpas)

# Print the calculated values
print(f"Mean GPA: {mean_gpa:.2f}")
print(f"Median GPA: {median_gpa:.2f}")
print(f"Mode GPA (approx): {mode_gpa:.2f}")
print(f"Standard Deviation: {std_dev_gpa:.2f}")

# Visualization
plt.figure(figsize=(10, 5))

# Histogram for GPA distribution
plt.subplot(1, 2, 1)
sns.histplot(gpas, bins=10, kde=True)
plt.title("GPA Distribution")
plt.xlabel("GPA")
plt.ylabel("Frequency")

# Box plot for identifying outliers
plt.subplot(1, 2, 2)
sns.boxplot(y=gpas)
plt.title("GPA Box Plot")
plt.ylabel("GPA")

plt.tight_layout()
plt.show()
