from pyspark import SparkContext, SparkConf

# Configure and initialize the SparkContext
conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext.getOrCreate(conf=conf)

# Your existing code with SparkContext `sc` now defined
# textFile = sc.textFile("hdfs://path/to/text/file")
# This line tells Spark to create an RDD by reading a text file from HDFS (Hadoop Distributed File System).
# The path "hdfs://path/to/text/file" is where your text file is located on the HDFS.
textFile = sc.textFile('C:\\example.txt')
wordCounts = textFile.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print(wordCounts.collect())
