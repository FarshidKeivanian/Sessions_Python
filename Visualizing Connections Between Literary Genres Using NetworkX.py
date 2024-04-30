import matplotlib.pyplot as plt
import networkx as nx

# Create a graph object
G = nx.Graph()

# Add nodes (genres) with additional attributes for visualization
genres = {
    'Science Fiction': {'color': 'cyan'},
    'Fantasy': {'color': 'magenta'},
    'Romance': {'color': 'pink'},
    'Historical': {'color': 'orange'},
    'Thriller': {'color': 'red'},
    'Mystery': {'color': 'purple'}
}
for genre, attributes in genres.items():
    G.add_node(genre, **attributes)

# Add edges (books connecting genres)
edges = [
    ('Mystery', 'Thriller', {'book': 'Book A'}),
    ('Romance', 'Historical', {'book': 'Book D'}),
    ('Historical', 'Thriller', {'book': 'Book E'}),
    ('Science Fiction', 'Fantasy', {'book': 'Book B'}),
    ('Fantasy', 'Romance', {'book': 'Book C'})
]
for u, v, attributes in edges:
    G.add_edge(u, v, **attributes)

# Define node positions in a circular layout for clarity
pos = nx.circular_layout(G)

# Draw the nodes
colors = [data['color'] for node, data in G.nodes(data=True)]
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=3000)

# Draw the edges
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='black')

# Label the edges with book titles
edge_labels = {(u, v): d['book'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='green')

# Draw genre labels
nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')

# Show the graph
plt.title("Graph Model of Bookstore Genres")
plt.axis('off')  # Turn off the axis
plt.show()
