import networkx as nx

def setup_graph():
    # Create a graph
    G = nx.Graph()
    
    # Add nodes which represent cities
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
    G.add_nodes_from(cities)
    
    # Add edges which represent direct flights between cities
    # Each edge can optionally have a 'weight' if the distance or cost is considered
    flights = [("New York", "Los Angeles"), ("New York", "Chicago"), ("Chicago", "Los Angeles"),
               ("Houston", "Los Angeles"), ("Miami", "New York"), ("Chicago", "Miami")]
    G.add_edges_from(flights)
    
    return G

def find_shortest_path(G, source, target):
    # Find the shortest path using Dijkstra's algorithm
    path = nx.shortest_path(G, source=source, target=target)
    
    return path

# Setup the graph
graph = setup_graph()

# Define the source and destination
source_city = "New York"
destination_city = "Los Angeles"

# Find the shortest path
shortest_path = find_shortest_path(graph, source=source_city, target=destination_city)

print("Shortest path from", source_city, "to", destination_city, ":", shortest_path)
