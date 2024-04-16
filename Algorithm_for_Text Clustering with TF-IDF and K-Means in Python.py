#pip install nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Sample documents
documents = [
    "The sky is blue and beautiful.",
    "Love this blue and beautiful sky!",
    "The quick brown fox jumps over the lazy dog.",
    "A king's breakfast has sausages, ham, bacon, eggs, toast, and beans",
    "I love green eggs, ham, sausages, and bacon!",
    "The brown fox is quick and the blue dog is lazy!",
    "The sky is very blue and the sky is very beautiful today",
    "The dog is lazy but the brown fox is quick!"
]

# Step 1: Preprocessing
def preprocess(text):
    # Tokenization and removing stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in text.lower().split() if word not in stop_words and word.isalpha()]
    return ' '.join(tokens)

# Applying preprocessing to each document
processed_docs = [preprocess(doc) for doc in documents]

# Step 2: TF-IDF Vectorization
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_docs)

# Step 3: Clustering
kmeans = KMeans(n_clusters=2, random_state=0).fit(tfidf_matrix)

# Assigning clusters to documents
document_clusters = pd.DataFrame(documents, columns=['Document'])
document_clusters['Cluster'] = kmeans.labels_

# Step 4: Analysis
print(document_clusters)

# To visualize the top terms per cluster
def get_top_features_cluster(tfidf_matrix, prediction, n_feats):
    labels = np.unique(prediction)
    dfs = []
    for label in labels:
        id_temp = np.where(prediction == label)  # indices for each cluster
        x_means = np.mean(tfidf_matrix[id_temp], axis=0).tolist()[0]  # mean tf-idf and flatten the matrix
        sorted_means = np.argsort(x_means)[::-1][:n_feats]  # top features
        features = vectorizer.get_feature_names_out()
        best_features = [(features[i], x_means[i]) if i < len(features) else ("N/A", 0) for i in sorted_means]
        df = pd.DataFrame(best_features, columns=['features', 'score'])
        dfs.append(df)
    return dfs

top_features_per_cluster = get_top_features_cluster(tfidf_matrix, kmeans.labels_, 5)
for num, df in enumerate(top_features_per_cluster):
    print(f"Top terms at cluster {num}:\n{df}")
