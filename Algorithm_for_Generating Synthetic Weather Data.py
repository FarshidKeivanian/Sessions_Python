import pandas as pd
import numpy as np

# Set the seed for reproducibility
np.random.seed(0)

# Generate date range
dates = pd.date_range(start="2013-01-01", end="2022-12-31", freq='D')

# Generate synthetic temperature data: average temperature between 10°C and 30°C
temperatures = np.random.uniform(10, 30, size=len(dates))

# Generate synthetic humidity data: humidity between 40% and 90%
humidity = np.random.uniform(40, 90, size=len(dates))

# Generate synthetic precipitation data: precipitation between 0 mm and 20 mm
precipitation = np.random.uniform(0, 20, size=len(dates))

# Create DataFrame
weather_data = pd.DataFrame({
    'Date': dates,
    'Temperature': temperatures,
    'Humidity': humidity,
    'Precipitation': precipitation
})

# Save to CSV
csv_file_path = 'D:\Synthetic_Weather_Data.csv'
weather_data.to_csv(csv_file_path, index=False)

weather_data.head()
