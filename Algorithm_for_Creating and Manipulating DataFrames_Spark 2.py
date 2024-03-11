from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Spark Example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Sample data
data = [("John", 28), ("Jane", 30), ("Doe", 26)]
columns = ["Name", "Age"]

# Create a DataFrame
df = spark.createDataFrame(data, schema=columns)


filtered_df = df.filter(df.Age >= 28)


filtered_df.show()


