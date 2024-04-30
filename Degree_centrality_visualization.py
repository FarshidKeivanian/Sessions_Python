import networkx as nx

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
# Calculate degree centrality for all nodes
degree_centrality = nx.degree_centrality(G)

# Display the degree centrality of each node
print("Degree Centrality of Each Node:")
for node, centrality in degree_centrality.items():
    print(f"Node {node}: {centrality:.2f}")

# Specifically for node D
print(f"\nDegree Centrality of node D: {degree_centrality['D']:.2f}")
