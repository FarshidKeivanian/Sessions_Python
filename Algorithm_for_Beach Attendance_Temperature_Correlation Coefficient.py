import pandas as pd
import numpy as np

# Let's assume you have a DataFrame with two columns: 'temperature' and 'beach_attendance'.
# This DataFrame is a simplified representation of a dataset.
data = {
    'temperature': [20, 22, 24, 26, 28, 30],
    'beach_attendance': [50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Calculate the correlation coefficient.
correlation_coefficient = df['temperature'].corr(df['beach_attendance'])

print(f"The correlation coefficient between temperature and beach attendance is: {correlation_coefficient}")
