from pyspark.sql import SparkSession
from pyspark.ml.feature import Bucketizer
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder.appName("AgeBinning").getOrCreate()

# Load the dataset
df = spark.read.csv('D:\\bank.csv', header=True, sep=';', inferSchema=True)

# Define the bins with the Bucketizer
bucketizer = Bucketizer(splits=[0, 20, 30, 40, 50, 60, 70, 80, float('Inf')], inputCol="age", outputCol="age_bucket")

# Transform the DataFrame to include the binned ages
df_binned = bucketizer.transform(df)

# Group by the binned ages and count the occurrences
binned_data = df_binned.groupBy("age_bucket").count().orderBy("age_bucket")

# Collect the grouped data
binned_data_collect = binned_data.collect()

# Extract the bin labels and counts
bins_labels = [row['age_bucket'] for row in binned_data_collect]
counts = [row['count'] for row in binned_data_collect]

# Plot the resulting data as a bar chart
plt.bar(bins_labels, counts, align='center')
plt.xlabel('Age Bins')
plt.ylabel('Count')
plt.title('Bar Chart of Binned Age')
plt.xticks(bins_labels, ['0-20', '21-30', '31-40', '41-50', '51-60', '61-70', '71-80', '80+'])
plt.show()