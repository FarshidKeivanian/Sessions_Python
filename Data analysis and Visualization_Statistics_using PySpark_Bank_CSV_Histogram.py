from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder.appName("Histogram").getOrCreate()

# Load the dataset
df = spark.read.csv('D:\\bank.csv', header=True, sep=';', inferSchema=True)

# Collect the 'age' data
age_data = df.select("age").collect()

# Extract ages into a list
ages = [row['age'] for row in age_data]

# Create a histogram of the 'age' data
plt.hist(ages, bins=20)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Histogram of Age')
plt.show()
