from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Initialize SparkSession
spark = SparkSession.builder.appName("decision_tree").getOrCreate()

# Sample data
data = [
    (1, 0, 'mammal'),
    (1, 0, 'mammal'),
    (0, 1, 'reptile'),
    (0, 1, 'reptile'),
    (1, 0, 'mammal')
]
columns = ['warm_blooded', 'lays_eggs', 'label']

# Create a DataFrame
df = spark.createDataFrame(data, schema=columns)

# Assemble features
assembler = VectorAssembler(inputCols=['warm_blooded', 'lays_eggs'], outputCol='features')

# Convert string labels to indices
labelIndexer = StringIndexer(inputCol='label', outputCol='indexedLabel').fit(df)

# Decision Tree model, now using the indexed label
dt = DecisionTreeClassifier(labelCol='indexedLabel', featuresCol='features')

# Pipeline, including the label indexer
pipeline = Pipeline(stages=[assembler, labelIndexer, dt])

# Split the data
(train, test) = df.randomSplit([0.7, 0.3])

# Train the model
model = pipeline.fit(train)

# Make predictions
predictions = model.transform(test)

# Evaluate the model using the indexed labels
evaluator = MulticlassClassificationEvaluator(labelCol='indexedLabel', predictionCol='prediction', metricName='accuracy')
accuracy = evaluator.evaluate(predictions)
print("Test set accuracy = " + str(accuracy))
