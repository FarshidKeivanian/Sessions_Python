# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D  # This is needed for 3D plotting
import matplotlib.pyplot as plt
import numpy as np

# Part 1: Prepare the Data
# Load the Iris dataset
iris = load_iris()
X = iris.data[:, :3]  # Use the first three features for clustering

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Part 2: Cluster the Data
# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Part 3: Analyze the Clusters
# Visualize the clusters in 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')  # Create a 3D plot

colors = ['red', 'green', 'blue']
for i in range(3):
    ax.scatter(X_scaled[kmeans.labels_ == i, 0], X_scaled[kmeans.labels_ == i, 1], X_scaled[kmeans.labels_ == i, 2],
               color=colors[i], label=f'Cluster {i+1}', edgecolor='k', s=50)

ax.set_title('KMeans Clustering of Iris Dataset')
ax.set_xlabel('Scaled Feature 1')
ax.set_ylabel('Scaled Feature 2')
ax.set_zlabel('Scaled Feature 3')
plt.legend()
plt.show()
