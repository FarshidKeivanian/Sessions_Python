import networkx as nx
import matplotlib.pyplot as plt

def setup_graph():
    G = nx.Graph()
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    G.add_nodes_from(cities)
    flights = [("New York", "Los Angeles"), ("New York", "Chicago"), 
               ("Chicago", "Los Angeles"), ("Houston", "Los Angeles"), 
               ("Miami", "New York"), ("Chicago", "Miami")]
    G.add_edges_from(flights)
    return G

def find_shortest_path(G, source, target):
    return nx.shortest_path(G, source=source, target=target)

def plot_graph(G, path):
    pos = nx.spring_layout(G)  # positions for all nodes

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # Draw the edges
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6, alpha=0.5, edge_color="gray")
    # Highlight the path edges
    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=6, alpha=0.7, edge_color="blue")

    # Draw the node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

    plt.axis("off")  # Turn off the axis
    plt.show()

# Main execution
graph = setup_graph()
source_city = "New York"
destination_city = "Los Angeles"
shortest_path = find_shortest_path(graph, source=source_city, target=destination_city)
print("Shortest path from", source_city, "to", destination_city, ":", shortest_path)
plot_graph(graph, shortest_path)
