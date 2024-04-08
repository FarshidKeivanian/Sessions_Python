import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
for i in range(5):
    G.add_node(i)

# Add edges
edges = [(0, 1), (1, 2), (2, 3), (3, 4), (1, 3)]
G.add_edges_from(edges)

# Display the graph
print("Nodes:", G.nodes())
print("Edges:", G.edges())

# BFS and DFS
print("BFS from node 0:", list(nx.bfs_edges(G, 0)))
print("DFS from node 0:", list(nx.dfs_edges(G, 0)))

# Remove a node and an edge
G.remove_node(4)
G.remove_edge(1, 3)

# Display the graph after removal
print("Nodes after removal:", G.nodes())
print("Edges after removal:", G.edges())
