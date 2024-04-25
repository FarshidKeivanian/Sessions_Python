import numpy as np
import pandas as pd

np.random.seed(0)  # For reproducibility

# Generating synthetic data
house_size = np.random.normal(1500, 500, 1000).astype(int)  # Average size 1500 sqft
bedrooms = np.random.choice([2, 3, 4, 5], 1000, p=[0.1, 0.5, 0.3, 0.1])  # Mostly 3-4 bedrooms
bathrooms = bedrooms - np.random.choice([0, 1], 1000, p=[0.7, 0.3])  # Bedrooms minus 0 or 1
house_age = np.random.normal(20, 15, 1000).astype(int)  # Average age 20 years
distance_city_center = np.random.normal(10, 5, 1000)  # Average 10 km from city center
sale_price = (house_size * 100) - (house_age * 1000) + (bedrooms * 5000) + (bathrooms * 2000) - (distance_city_center * 2000)

# Creating a DataFrame
df = pd.DataFrame({
    'house_size': house_size,
    'bedrooms': bedrooms,
    'bathrooms': bathrooms,
    'house_age': house_age,
    'distance_city_center': distance_city_center,
    'sale_price': sale_price
})

# Display the first few rows of the dataset
df.head()
