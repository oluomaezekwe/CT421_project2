import networkx as nx
import matplotlib.pyplot as plt
import random
import time

def create_preferential_attachment_graph(num_nodes, num_edges_to_attach):
    return nx.barabasi_albert_graph(num_nodes, num_edges_to_attach)

def label_graph(graph, min, max):
    graph_labels = {}
    for node in graph.nodes():
        graph_labels[node] = random.randint(min, max)
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
        num_conflicts = count_conflicts(graph, graph_labels)
        print(f"Iteration {iter_count}, Number of Conflicts: {num_conflicts}")
        if num_conflicts == 0:
            break
        node_to_change = random.choice(list(graph.nodes()))
        neighbors = list(graph.neighbors(node_to_change))
        if any(graph_labels[node_to_change] == graph_labels[neighbor] for neighbor in neighbors):
            new_label = random.choice([label for label in range(num_labels) if label != graph_labels[node_to_change]])
            graph_labels[node_to_change] = new_label
        iter_count += 1
    return graph_labels

num_nodes = 10
num_edges_to_attach = 2  # Number of edges to attach from a new node to existing nodes
min_colours = 1
max_colours = 8
max_iterations = 1000
start_time = time.time()

G = create_preferential_attachment_graph(num_nodes, num_edges_to_attach)
labels = label_graph(G, min_colours, max_colours)

init_conflicts = count_conflicts(G, labels)
print("Initial Number of Conflicts:", init_conflicts)

final_labels = update_labels(G, labels, max_colours, max_iterations)
final_conflicts = count_conflicts(G, final_labels)
print("Final Number of Conflicts:", final_conflicts)

end_time = time.time()
runtime_ms = (end_time - start_time) * 1000
print("Runtime: {:.2f} ms".format(runtime_ms))

nx.draw(G, labels=labels, with_labels=True)
plt.show()
