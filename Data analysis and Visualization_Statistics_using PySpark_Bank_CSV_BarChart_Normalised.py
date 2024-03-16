from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
from pyspark.sql.functions import col, avg, stddev

# Initialize Spark session
spark = SparkSession.builder.appName("DescriptiveStatistics").getOrCreate()

# Load the dataset
df = spark.read.csv('D:\\bank.csv', header=True, sep=';', inferSchema=True)

# Calculate mean and standard deviation for the specified columns
stats_pyspark = df.select(
    [avg(c).alias(c + '_Mean') for c in ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']] +
    [stddev(c).alias(c + '_StdDev') for c in ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']]
).collect()[0].asDict()

# For median, PySpark does not have a direct function like Pandas. We need to use approxQuantile.
medians = {c: df.approxQuantile(c, [0.5], 0.001)[0] for c in ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']}

# Combine the results
for c in ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']:
    stats_pyspark[c + '_Median'] = medians[c]

print(stats_pyspark)

# Total count of the dataset
total_count = df.count()

# Convert Spark DataFrame to Pandas DataFrame for plotting
# Note: This step is necessary since matplotlib works with Pandas DataFrames or similar structures
previous_counts = df.groupBy('previous').count().withColumn('normalized', col('count') / total_count).toPandas()

# Sort the DataFrame by the 'previous' column to ensure the bars are in order
previous_counts.sort_values('previous', inplace=True)

# Plotting the normalized bar graph
plt.bar(previous_counts['previous'], previous_counts['normalized'])
plt.title('Normalized Bar Graph of Previous')
plt.xlabel('Previous')
plt.ylabel('Normalized Count')
plt.show()
