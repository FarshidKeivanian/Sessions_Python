from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Initialize Spark Session
spark = SparkSession.builder.appName("PySparkFunctionsTutorial").getOrCreate()

# Load Dataset
#df = spark.read.csv("nyc_parking_tickets.csv", header=True, inferSchema=True)
df = spark.read.csv('D:\\archive\parking-violations-issued-fiscal-year-2014-august-2013-june-2014.csv', header=True, inferSchema=True)

# Aggregation
result = df.groupBy("Violation Code").agg(count("*").alias("TotalTickets"))

result.show()
