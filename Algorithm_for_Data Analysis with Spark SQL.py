from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark SQL Example").getOrCreate()

# Example DataFrame
df = spark.createDataFrame([("John Doe", 30), ("Jane Doe", 25)], ["Name", "Age"])

df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people WHERE Age > 25")
sqlDF.show()
