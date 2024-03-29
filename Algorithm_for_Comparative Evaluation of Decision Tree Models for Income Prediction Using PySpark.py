from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize Spark Session
spark = SparkSession.builder.appName("ModelEvaluation").getOrCreate()

# Load the training and test datasets
training_df = spark.read.csv('D:\\Socioeconomic_Factors_Income Prediction_Training_Data', header=True, inferSchema=True)
test_df = spark.read.csv('D:\\Socioeconomic_Factors_Income Prediction_Test_Data', header=True, inferSchema=True)

# Index the categorical columns (Marital status, Income)
indexers = [StringIndexer(inputCol=column, outputCol=column+"_index").fit(training_df) for column in ["Marital status", "Income"]]

# Assemble features
assembler = VectorAssembler(inputCols=["Marital status_index", "Cap_Gains_Losses"], outputCol="features")

# Initialize the Decision Tree Classifier for Model 1
dtc = DecisionTreeClassifier(labelCol="Income_index", featuresCol="features")

# Create the pipeline
pipeline = Pipeline(stages=indexers + [assembler, dtc])

# Train Model 1
model_1 = pipeline.fit(training_df)

# Predict on the test set
predictions = model_1.transform(test_df)

# Evaluate Model 1
evaluator = MulticlassClassificationEvaluator(labelCol="Income_index", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy of Model 1: {accuracy}")

# Construct a contingency table
predictions.groupBy('Income_index', 'prediction').count().show()