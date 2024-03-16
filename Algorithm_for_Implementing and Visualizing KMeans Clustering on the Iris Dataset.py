# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Part 1: Prepare the Data
# Load the Iris dataset
iris = load_iris()
X = iris.data  # We only use the features for clustering, not the labels

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Part 2: Cluster the Data
# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Part 3: Analyze the Clusters
# Visualize the clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
for i in range(3):
    plt.scatter(X_scaled[kmeans.labels_ == i, 0], X_scaled[kmeans.labels_ == i, 1], 
                color=colors[i], label=f'Cluster {i+1}', edgecolor='k', s=50)
    
plt.title('KMeans Clustering of Iris Dataset')
plt.xlabel('Scaled Sepal Length')
plt.ylabel('Scaled Sepal Width')
plt.legend()
plt.show()
