import networkx as nx
import matplotlib.pyplot as plt


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


m = 2
n = 2
G = create_2d_lattice_graph(m, n)

print("Nodes:", G.nodes())
print("Edges:", G.edges())

nx.draw(G)
plt.show()
