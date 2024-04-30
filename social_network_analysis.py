import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a sample graph
G = nx.DiGraph()  # Directed graph to capture directionality in interactions

# Adding nodes (representing users)
users = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
G.add_nodes_from(users)

# Adding edges (representing interactions: likes, comments, shares)
interactions = [("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Alice"), ("Diana", "Alice"),
                ("Alice", "Eve"), ("Eve", "Frank"), ("Frank", "Diana"), ("Bob", "Diana"),
                ("Charlie", "Eve"), ("Eve", "Alice")]

G.add_edges_from(interactions)

# Step 2: Apply centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

# Step 3: Visualize the graph with node size reflecting degree centrality
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # positions for all nodes

# nodes
node_sizes = [degree_centrality[node] * 1000 for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue')

# edges
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->')

# labels
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

plt.title("Social Network Analysis: Node Size Reflects Degree Centrality")
plt.axis('off')  # Turn off the axis
plt.show()
