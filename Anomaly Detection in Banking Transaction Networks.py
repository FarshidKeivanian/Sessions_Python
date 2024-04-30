import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Create a sample graph of transactions
G = nx.DiGraph()  # Directed graph for directed transactions

# Adding nodes (representing bank accounts)
accounts = range(1, 11)  # Let's assume we have 10 bank accounts
G.add_nodes_from(accounts)

# Adding edges (representing transactions between accounts)
transactions = [(1, 2), (2, 3), (3, 4), (4, 1), (1, 5), (5, 6), (6, 1), (7, 8),
                (8, 9), (9, 10), (10, 7), (3, 7), (1, 8)]
G.add_edges_from(transactions)

# Step 2: Detect anomalies
# We will define an anomaly as any account with unusually high transaction volume or loops
degree_centrality = nx.degree_centrality(G)
# Finding loops (cycles in the graph that may indicate round-tripping)
cycles = list(nx.simple_cycles(G))

# Step 3: Visualize the graph
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)  # positions for all nodes

# Highlight nodes with high degree centrality or part of a cycle
high_degree_accounts = [node for node, deg in degree_centrality.items() if deg > 0.2]
cycle_nodes = set(node for cycle in cycles for node in cycle)
highlight = list(set(high_degree_accounts) | cycle_nodes)

nx.draw_networkx_nodes(G, pos, nodelist=highlight, node_color='red', label='Potential Fraud')
nx.draw_networkx_nodes(G, pos, nodelist=[n for n in G if n not in highlight], node_color='skyblue', label='Normal')
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), arrowstyle='->')
nx.draw_networkx_labels(G, pos, font_size=12)

plt.title("Banking Transactions: Anomaly Detection in Network")
plt.legend()
plt.axis('off')  # Turn off the axis
plt.show()
