import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Simulating data
np.random.seed(42)
heights = np.random.normal(170, 10, 200)  # Mean 170cm, SD 10cm
weights = np.random.normal(70, 15, 200)  # Mean 70kg, SD 15kg
data = np.column_stack((heights, weights))

# Applying K-means and using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

# Plotting the results
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
