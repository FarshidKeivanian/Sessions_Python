from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, FloatType, IntegerType
from pyspark.ml.feature import VectorAssembler, PolynomialExpansion
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark session
spark = SparkSession.builder.appName("Boston Housing Analysis").getOrCreate()

# Define schema for the dataset
schema = StructType([
    StructField("CRIM", FloatType()),
    StructField("ZN", FloatType()),
    StructField("INDUS", FloatType()),
    StructField("CHAS", IntegerType()),
    StructField("NOX", FloatType()),
    StructField("RM", FloatType()),
    StructField("AGE", FloatType()),
    StructField("DIS", FloatType()),
    StructField("RAD", IntegerType()),
    StructField("TAX", FloatType()),
    StructField("PTRATIO", FloatType()),
    StructField("B", FloatType()),
    StructField("LSTAT", FloatType()),
    StructField("MEDV", FloatType())
])

# Load dataset
df = spark.read.csv("D:/boston_house_prices_corrected.csv", schema=schema, sep=",")

# Handle NULL values
df = df.na.drop()  # This line removes rows containing any NULL values. Alternatively, use df.na.fill() to fill NULLs

# Show the data (for verification)
df.show()

# Compute pairwise correlations and find top 3 correlated variables with 'MEDV'
correlations = {col: df.stat.corr('MEDV', col) for col in df.columns if col != 'MEDV'}
top_three = sorted(correlations, key=correlations.get, reverse=True)[:3]
print("Top three correlated variables with MEDV:", top_three)

# Setup the data processing and modeling pipeline
assembler = VectorAssembler(inputCols=top_three, outputCol="features")
polyExpansion = PolynomialExpansion(degree=2, inputCol="features", outputCol="polyFeatures")
lr = LinearRegression(featuresCol="polyFeatures", labelCol="MEDV")
pipeline = Pipeline(stages=[assembler, polyExpansion, lr])

# Split data, fit the model, and evaluate
train_data, test_data = df.randomSplit([0.7, 0.3])
model = pipeline.fit(train_data)
predictions = model.transform(test_data)
evaluator = RegressionEvaluator(predictionCol="prediction", labelCol="MEDV", metricName="r2")
print(f"R-squared on test data = {evaluator.evaluate(predictions)}")
