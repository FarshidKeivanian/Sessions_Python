import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set random seed for reproducibility
np.random.seed(42)

# Number of users
num_users = 100

# Generate random connections
user1 = np.random.randint(1, num_users + 1, size=1000)
user2 = np.random.randint(1, num_users + 1, size=1000)

# Ensure no self-connections
indices = user1 != user2
user1 = user1[indices]
user2 = user2[indices]

# Shuffle the connections
indices = np.random.permutation(len(user1))
user1 = user1[indices]
user2 = user2[indices]

# Label connections as connected or not connected
connected = np.random.randint(0, 2, size=len(user1))

# Create a DataFrame
data = pd.DataFrame({'user1': user1, 'user2': user2, 'connected': connected})

# Load the dataset
data = pd.read_csv('synthetic_social_network.csv')

# Split the data into training and testing sets
X = data.drop('connected', axis=1)
y = data['connected']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reset index for X_test
X_test = X_test.reset_index(drop=True)

# Train the Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Visualize the predicted connections
G = nx.Graph()

# Add edges
for index, row in X_test.iterrows():
    if y_pred[index] == 1:
        G.add_edge(row['user1'], row['user2'])

# Set up graph layout
pos = nx.kamada_kawai_layout(G)

# Draw the graph
plt.figure(figsize=(12, 12))  # Increase figure size
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='black', linewidths=1, font_size=10)

# Show plot
plt.show()
