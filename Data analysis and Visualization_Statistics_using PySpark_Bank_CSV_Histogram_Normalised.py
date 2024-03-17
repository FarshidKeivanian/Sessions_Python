from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import numpy as np

# Initialize Spark session
spark = SparkSession.builder.appName("NormalizedHistogram").getOrCreate()

# Load the dataset
df = spark.read.csv('D:\\bank.csv', header=True, sep=';', inferSchema=True)

# Collect the 'age' data
age_data = df.select("age").collect()

# Extract ages into a list
ages = [row['age'] for row in age_data]

# Normalize the ages using z-score normalization
ages_mean = np.mean(ages)
ages_std = np.std(ages)
ages_normalized = [(age - ages_mean) / ages_std for age in ages]

# Create a histogram of the normalized 'age' data
plt.hist(ages_normalized, bins=20)
plt.xlabel('Normalized Age')
plt.ylabel('Count')
plt.title('Histogram of Normalized Age')
plt.show()