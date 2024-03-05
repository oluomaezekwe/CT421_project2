import networkx as nx
import matplotlib.pyplot as plt
import random

def create_2d_lattice_graph(a, b):
    graph = nx.Graph()

    # Add nodes
    for i in range(a):
        for j in range(b):
            graph.add_node((i, j))

    # Add edges
    for i in range(a):
        for j in range(b):
            if i < a - 1:
                graph.add_edge((i, j), (i + 1, j))
            if j < b - 1:
                graph.add_edge((i, j), (i, j + 1))

    return graph

def label_graph(graph):
    labels = {}
    for node in graph.nodes():
        labels[node] = random.randint(1, 5)  # Assigning random labels
    return labels

m = 5
n = 5
G = create_2d_lattice_graph(m, n)
labels = label_graph(G)

print("Nodes:", G.nodes())
print("Edges:", G.edges())

nx.draw(G, labels=labels, with_labels=True)
plt.show()
