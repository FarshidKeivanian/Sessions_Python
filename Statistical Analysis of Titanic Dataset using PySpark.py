# pip install requests
# The data from this url has been saved as a csv file
# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

# Step 1: Write a Python code to read the URL and save it as a CSV file on drive D

import requests

# URL of the dataset
data_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
local_file_path = "D:/titanic.csv"  # Change this to your desired location

# Download the dataset
response = requests.get(data_url)
with open(local_file_path, 'wb') as f:
    f.write(response.content)

print(f"Dataset downloaded and saved as {local_file_path}")

# Step 2: Main code to read the saved CSV file and perform data analysis with PySpark

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, stddev
import os

# Initialize Spark session
spark = SparkSession.builder.appName("DataAnalysis").getOrCreate()

# Load the dataset
df = spark.read.csv(local_file_path, header=True, inferSchema=True)

# Calculate mean and standard deviation for specified columns
numeric_columns = [c for c in df.columns if df.schema[c].dataType.typeName() in ['double', 'int']]
stats_pyspark = df.select(
    [avg(c).alias(c + '_Mean') for c in numeric_columns] +
    [stddev(c).alias(c + '_StdDev') for c in numeric_columns]
).collect()[0].asDict()

# Display the results
print(stats_pyspark)

# Stop the Spark session
spark.stop()

# Optional: Clean up the downloaded file
# Uncomment the next line if you want to remove the file after analysis
# os.remove(local_file_path)
