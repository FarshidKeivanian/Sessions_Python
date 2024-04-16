from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns

# Step 1: Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Step 2: Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

# Step 3: Compare with actual species
# Because cluster labels might not directly correspond with actual labels, we check correspondence
cm = confusion_matrix(y, clusters)
sns.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted Clusters')
plt.ylabel('True Labels')
plt.show()
