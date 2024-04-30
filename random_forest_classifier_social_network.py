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

# Save the dataset to CSV
data.to_csv('synthetic_social_network.csv', index=False)

# Step 1: Load the dataset
data = pd.read_csv('synthetic_social_network.csv')

# Step 2: Data Preprocessing (if necessary)

# Step 3: Feature Engineering

# Step 4: Split the data into training and testing sets
X = data.drop('connected', axis=1)  # Assuming 'connected' is the target variable
y = data['connected']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Algorithm Selection
model = RandomForestClassifier()

# Step 6: Train the algorithm
model.fit(X_train, y_train)

# Step 7: Evaluate Performance
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Tune Hyperparameters (if necessary)

# Step 9: Make Predictions (on new data, if available)
# Assuming you want to visualize the predicted connections on a graph
# Create a graph
G = nx.Graph()

# Add edges from the test set
for index, row in X_test.iterrows():
    if y_pred[index] == 1:  # If the prediction is a connection
        G.add_edge(row['user1'], row['user2'])

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=15)

# Show plot
plt.show()
