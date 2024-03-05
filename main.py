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
    graph_labels = {}

    for node in graph.nodes():
        graph_labels[node] = random.randint(min_val, max_val)
    return graph_labels


def count_conflicts(graph, graph_labels):
    num_conflicts = 0

    for node in graph.nodes():
        neighbors = graph.neighbors(node)

        for neighbor in neighbors:
            if graph_labels[node] == graph_labels[neighbor]:
                num_conflicts += 1
    return num_conflicts


def update_labels(graph, graph_labels, num_labels, max_iter):
    iter_count = 0

    while iter_count < max_iter:
        num_conflicts = count_conflicts(G, graph_labels)
        print(f"Iteration {iter_count}, Number of Conflicts: {num_conflicts}")

        if num_conflicts == 0:
            break

        node_to_change = random.choice(list(graph.nodes()))
        new_label = random.choice([label for label in range(num_labels) if label != graph_labels[node_to_change]])
        graph_labels[node_to_change] = new_label

        iter_count += 1
    return graph_labels


m = 8
n = 8
p = 1
q = 25
max_iterations = 1000

G = create_2d_lattice_graph(m, n)
labels = label_graph(G, p, q)

init_conflicts = count_conflicts(G, labels)
print("Initial Number of Conflicts:", init_conflicts)

final_labels = update_labels(G, labels, q, max_iterations)
final_conflicts = count_conflicts(G, final_labels)
print("Final Number of Conflicts:", final_conflicts)

nx.draw(G, labels=labels, with_labels=True)
plt.show()
