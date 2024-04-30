import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a Graph
G = nx.Graph()  # Create an empty graph

# Add nodes
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# Add edges
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
G.add_edges_from(edges)

# Step 2: Calculate Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Visualization
pos = nx.spring_layout(G)  # positions for all nodes
node_colors = [degree_centrality[node] for node in G.nodes()]

# Draw the nodes and edges
nx.draw(G, pos, with_labels=True, node_size=3000, node_color=node_colors, cmap=plt.cm.Blues, edge_color='gray', linewidths=2, font_size=15)
# Draw the degree centrality labels
labels = {node: f'{centrality:.2f}' for node, centrality in degree_centrality.items()}
nx.draw_networkx_labels(G, pos, labels=labels, font_color='red')

# Add color bar
sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label('Degree Centrality', rotation=270, labelpad=20)

plt.title('Network Graph with Degree Centrality')
plt.show()

# Display the degree centrality of each node
print("Degree Centrality of Each Node:")
for node, centrality in degree_centrality.items():
    print(f"Node {node}: {centrality:.2f}")

# Specifically for node D
print(f"\nDegree Centrality of node D: {degree_centrality['D']:.2f}")
