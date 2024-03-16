import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\\bank.csv', delimiter=';')

# Calculate the mean, median, and standard deviation for the specified columns
stats_pandas = df[['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']].agg(['mean', 'median', 'std'])

# Rename the index to match the required output format
stats_pandas.rename(index={'mean': 'Mean', 'median': 'Median', 'std': 'StdDev'}, inplace=True)

print(stats_pandas.T)

# Plotting the bar graph for the 'previous' variable
df['previous'].value_counts().plot(kind='bar')
plt.title('Bar Graph of Previous')
plt.xlabel('Previous')
plt.ylabel('Frequency')
plt.show()
