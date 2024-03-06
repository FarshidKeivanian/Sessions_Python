#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Make sure you have pymongo installed in your environment
# You can install it using: pip install pymongo

from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('localhost', 27017)

# Select the database you want to use with MongoDB
db = client['BigData']

# Select the collection within the database
collection = db['example_collection']

# Insert a document into the collection
insert_result = collection.insert_one({'name': 'Alice', 'age': 30})

# Output the ID of the inserted document
print(f"Inserted document ID: {insert_result.inserted_id}")

# Retrieve a document from the collection
retrieved_document = collection.find_one({'name': 'Alice'})

# Output the retrieved document
print(f"Retrieved document: {retrieved_document}")

