
# %matplotlib inline
import matplotlib.pyplot as plt
import networkx as nx


def generate(m, t):
    graph = nx.Graph()
    graph.add_nodes_from([1, 2])
    graph.add_edge(1, 2)

    n = 2

    for i in range(t - 1):
        edges = list(graph.edges())
        for e in edges:
            print(e)
            for k in range(m):
                n += 1
                graph.add_node(n)
                nx.add_path(graph, [e[0], n, e[1]])
            graph.remove_edge(e[0], e[1])

    return graph


my_graph = generate(2, 4)
plt.figure(1)
nx.draw(my_graph, node_size=15)
plt.show()
