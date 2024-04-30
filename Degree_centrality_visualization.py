import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a Graph
G = nx.Graph()
nodes = ["A", "B", "C", "D", "E"]
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Step 2: Calculate Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Plotting the graph with node labels and their degree centrality
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # uses a spring layout for aesthetically pleasing node placement

# Adjust node size based on degree centrality (scaled by 5000 for visibility)
node_size = [5000 * centrality for centrality in degree_centrality.values()]
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=node_size, edge_color='gray', linewidths=1, font_size=15)

# Annotating nodes with their degree centrality
labels = {node: f"{node}\nDC: {centrality:.2f}" for node, centrality in degree_centrality.items()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=12)

plt.title('Social Network with Degree Centrality')
plt.show()
