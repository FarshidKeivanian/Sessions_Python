# Link to download Traffic Crashes - Crashes is https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/about_data
# Link to download Traffic Crashes - Vehicles is https://data.cityofchicago.org/Transportation/Traffic-Crashes-Vehicles/68nd-jvt3/data
# Link to download Traffic Crashes - People is https://catalog.data.gov/dataset/traffic-crashes-people


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, count, desc, month, sum, to_timestamp, to_date
from pyspark.sql.window import Window

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Traffic Crash Analysis") \
    .getOrCreate()

# Load the data
crashes_df = spark.read.csv('D:\\Traffic_Crashes_-_Crashes_20240312.csv', header=True, inferSchema=True)
vehicles_df = spark.read.csv('D:\\Traffic_Crashes_-_Vehicles.csv', header=True, inferSchema=True)
people_df = spark.read.csv('D:\\Traffic_Crashes_-_People.csv', header=True, inferSchema=True)

# Updated Analysis a: Ratio of Crashes Involving Cell Phone Use
cell_phone_usage = people_df.withColumn(
    "Cell_Phone_Use", 
    when(col("CELL_PHONE_USE") == 'Y', 'Yes')
    .when(col("CELL_PHONE_USE") == '', 'No')  # Handling empty values as 'No'
    .otherwise('No')
)
usage_ratio = cell_phone_usage.groupBy("Cell_Phone_Use").count()\
    .withColumn("Ratio", col("count") / sum("count").over(Window.partitionBy()))\
    .select("Cell_Phone_Use", "Ratio")
usage_ratio.show()

# Updated Analysis b: Three Age Groups with Highest Number of Crashes
people_df_filtered = people_df.filter(people_df.AGE.isNotNull())
age_group_crashes = people_df_filtered.groupBy("AGE").count().orderBy(desc("count")).limit(3)
age_group_crashes.show()

# Updated Analysis c: Month with Highest Crashes
date_format = "MM/dd/yyyy hh:mm:ss a"
crashes_df = crashes_df.withColumn("CRASH_DATE", to_timestamp("CRASH_DATE", date_format))
month_crashes = crashes_df.withColumn("Month", month("CRASH_DATE")) \
                          .groupBy("Month") \
                          .count() \
                          .orderBy(desc("count")) \
                          .limit(1)
month_crashes.show()

# Updated Analysis d: Day of the Week with Least Crashes
crashes_df = crashes_df.withColumn("CRASH_DATE", to_date("CRASH_DATE", "MM/dd/yyyy HH:mm:ss"))
crashes_df = crashes_df.filter(col("CRASH_DATE").isNotNull())
weekday_crashes = crashes_df.groupBy("CRASH_DAY_OF_WEEK").count().orderBy("count").limit(1)
weekday_crashes.show()
