from pyspark.sql import SparkSession
from pyspark.ml.feature import Tokenizer, CountVectorizer, StringIndexer
from pyspark.ml import Pipeline
from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.sql.functions import col
from pyspark.ml.feature import IndexToString

# Initialize Spark Session
spark = SparkSession.builder.appName("EmailSpamFilter").getOrCreate()

# Step 1: Mock dataset
data = [("free viagra now", 1), ("meeting schedule", 0), ("cheap watches", 1), 
        ("project deadline", 0), ("increase your income", 1), ("happy birthday", 0)]
df = spark.createDataFrame(data, ["email", "label"])

# Step 2: Split dataset into training and testing
(trainingData, testData) = df.randomSplit([0.7, 0.3], seed=42)

# Pipeline stages
tokenizer = Tokenizer(inputCol="email", outputCol="words")
vectorizer = CountVectorizer(inputCol=tokenizer.getOutputCol(), outputCol="features")
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(df)
nb = NaiveBayes(modelType="multinomial", labelCol="indexedLabel", featuresCol="features")
labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel", labels=labelIndexer.labels)

# Pipeline
pipeline = Pipeline(stages=[tokenizer, vectorizer, labelIndexer, nb, labelConverter])

# Train model
model = pipeline.fit(trainingData)

# Make predictions
predictions = model.transform(testData)

# Evaluate model
evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print(f"Accuracy: {accuracy}")

# Show some prediction results
predictions.select("email", "label", "predictedLabel").show()

# Predicting new emails (example)
newEmails = spark.createDataFrame([("free lottery tickets",), ("weekly meeting agenda",)], ["email"])
newPredictions = model.transform(newEmails)
newPredictions.select("email", "predictedLabel").show()
