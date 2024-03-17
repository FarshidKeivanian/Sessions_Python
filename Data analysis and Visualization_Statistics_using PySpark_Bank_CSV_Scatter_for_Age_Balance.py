from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, stddev, col

# Initialize Spark session
spark = SparkSession.builder.appName("DescriptiveStatistics").getOrCreate()

# Load the dataset
#df = spark.read.csv('/path/to/your/bank-full.csv', header=True, sep=';', inferSchema=True)
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