from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("KMeansExample").getOrCreate()
data = spark.read.csv("Customer_Data.csv", header=True, inferSchema=True)

from pyspark.ml.feature import VectorAssembler
assembler = VectorAssembler(inputCols=["Age", "AnnualIncome", "SpendingScore"], outputCol="features")
data = assembler.transform(data)

from pyspark.ml.clustering import KMeans
kmeans = KMeans().setK(3).setSeed(1)


model = kmeans.fit(data)


centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

transformed = model.transform(data)
transformed.show()


