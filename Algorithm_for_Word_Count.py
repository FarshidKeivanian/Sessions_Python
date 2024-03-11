from pyspark import SparkContext, SparkConf

# Configure and initialize the SparkContext
conf = SparkConf().setAppName("WordCount").setMaster("local")
sc = SparkContext.getOrCreate(conf=conf)

# Your existing code with SparkContext `sc` now defined
textFile = sc.textFile('C:\\example.txt')
wordCounts = textFile.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
print(wordCounts.collect())
