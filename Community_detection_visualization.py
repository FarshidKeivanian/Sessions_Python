#pip install networkx python-louvain matplotlib

import networkx as nx
import community as community_louvain
import matplotlib.pyplot as plt

def setup_graph():
    # Create a graph
    G = nx.Graph()
    
    # Add nodes which represent users
    users = range(10)  # 10 users, labeled 0 to 9
    G.add_nodes_from(users)
    
    # Add edges which represent friendships
    friendships = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (4, 5), 
                   (5, 6), (5, 7), (6, 7), (7, 8), (8, 9)]
    G.add_edges_from(friendships)
    
    return G

def detect_communities(G):
    # Compute the best partition using the Louvain method
    partition = community_louvain.best_partition(G)
    return partition

def visualize_communities(G, partition):
    # Draw the graph
    pos = nx.spring_layout(G)  # positions for all nodes
    cmap = plt.get_cmap('viridis')
    colors = [partition[i] for i in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, node_size=700, cmap=cmap, node_color=colors)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos)
    plt.show()

# Setup the graph
graph = setup_graph()

# Detect communities
communities = detect_communities(graph)

# Print the community of each user
for user, community in communities.items():
    print(f"User {user} is in community {community}")

# Visualize the communities
visualize_communities(graph, communities)
