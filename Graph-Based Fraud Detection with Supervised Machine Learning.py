import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load the dataset from GitHub
url = "https://raw.githubusercontent.com/FarshidKeivanian/Sessions_Python/main/Synthetic_bank_transactions.csv"
data = pd.read_csv(url)  # Read the dataset directly from the raw GitHub link

# Step 1: Graph Representation
# Build the graph: Nodes are Account_IDs and Transaction_IDs, edges are between them if fraudulent
G = nx.Graph()
for _, row in data.iterrows():
    if row["Is_Fraud"] == 1:  # Only include fraudulent transactions
        G.add_edge(row["Account_ID"], row["Transaction_ID"], weight=row["Amount"])

# Separate fraudulent and non-fraudulent transactions
fraudulent_nodes = set(data[data["Is_Fraud"] == 1]["Account_ID"]).union(
    set(data[data["Is_Fraud"] == 1]["Transaction_ID"])
)

# Visualize the graph with fraudulent nodes in red
plt.figure(figsize=(10, 7))
pos = nx.spring_layout(G, seed=42)  # Layout for positioning the nodes
node_colors = ["red" if node in fraudulent_nodes else "lightblue" for node in G.nodes()]

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=700,
    font_size=10,
    font_color="darkblue",
)
plt.title("Graph of Fraudulent Transactions and Accounts (Fraud in Red)")
plt.show()

# Step 2: Supervised Learning for Fraud Detection
# Prepare the data
features = data[["Amount", "Time"]]  # Use Amount and Time as features
labels = data["Is_Fraud"]  # Target is Is_Fraud column

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Train a Decision Tree Classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print(classification_report(y_test, y_pred))
