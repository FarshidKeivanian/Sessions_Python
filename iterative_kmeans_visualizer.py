import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time  # Import time module to add delay

# Generate some random data points
np.random.seed(42)
data = np.random.rand(50, 2) * 10  # 50 points in 2D space

# Number of clusters
k = 3

# Function to calculate the distance between points
def distance(a, b):
    return np.linalg.norm(a - b)

# Real-time K-means clustering
def kmeans_real_time(data, k, iterations=10):
    # Step 1: Initialize centroids randomly from the dataset
    centroids = data[np.random.choice(data.shape[0], k, replace=False)]
    
    # Initialize plot
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    scatters = [ax.scatter([], [], c=colors[i], s=30) for i in range(k)]
    centroid_scatters = [ax.scatter([], [], c='black', marker='x', s=100) for i in range(k)]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    def update(frame):
        nonlocal centroids

        # Step 2: Assign each data point to the nearest centroid
        clusters = {i: [] for i in range(k)}
        for point in data:
            distances = [distance(point, centroid) for centroid in centroids]
            closest_centroid = np.argmin(distances)
            clusters[closest_centroid].append(point)
        
        # Step 3: Recompute centroids
        new_centroids = []
        for i in range(k):
            if clusters[i]:
                new_centroid = np.mean(clusters[i], axis=0)
            else:
                new_centroid = centroids[i]
            new_centroids.append(new_centroid)
        
        centroids = np.array(new_centroids)
        
        # Update scatter plots
        for i in range(k):
            cluster_points = np.array(clusters[i])
            scatters[i].set_offsets(cluster_points)
            centroid_scatters[i].set_offsets(centroids[i])
        
        ax.set_title(f'Iteration {frame + 1}')
        
        # Pause for 1 second to visualize the change
        time.sleep(1)
        
        return scatters + centroid_scatters

    ani = FuncAnimation(fig, update, frames=range(iterations), blit=False, repeat=False)
    plt.show()

# Run K-means with real-time visualization for 10 iterations
kmeans_real_time(data, k, iterations=100)
