import pandas as pd
from scipy.stats import pearsonr

# Example dataset of average temperatures and tourist numbers
data = {
    'average_temp': [22, 25, 28, 30, 33, 35],  # Average temperature (°C)
    'tourist_numbers': [1500, 1800, 2100, 2500, 3000, 3200]  # Number of tourists
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the Pearson correlation coefficient
correlation, _ = pearsonr(df['average_temp'], df['tourist_numbers'])

print(f'The correlation coefficient is {correlation:.2f}')
