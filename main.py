import networkx as nx
import matplotlib.pyplot as plt
import random


def create_2d_lattice_graph(nodes, edges):
    graph = nx.Graph()

    for i in range(nodes):
        for j in range(edges):
            graph.add_node((i, j))

    for i in range(nodes):
        for j in range(edges):
            if i < nodes - 1:
                graph.add_edge((i, j), (i + 1, j))
            if j < edges - 1:
                graph.add_edge((i, j), (i, j + 1))

    return graph


def label_graph(graph, min_val, max_val):
    labels = {}

    for node in graph.nodes():
        labels[node] = random.randint(min_val, max_val)
    return labels


def count_conflicts(graph, labels):
    num_conflicts = 0

    for node in graph.nodes():
        neighbors = graph.neighbors(node)
        for neighbor in neighbors:
            if labels[node] == labels[neighbor]:
                num_conflicts += 1
    return num_conflicts


m = 8
n = 8
p = 1
q = 25

G = create_2d_lattice_graph(m, n)
labels = label_graph(G, p, q)

conflicts = count_conflicts(G, labels)
print("Number of Conflicts:", conflicts)

nx.draw(G, labels=labels, with_labels=True)
plt.show()
