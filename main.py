import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

edge_list = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 6),
             (6, 7), (2, 8), (8, 9), (9, 4)]
# G = nx.from_numpy_array(np.array([[0, 1, 0],
#                                   [1, 0, 1],
#                                   [1, 0, 0]]))

G = nx.Graph()
G.add_edges_from(edge_list)
# G = nx.complete_graph(5)

print(nx.degree_centrality(G))

# print(dict(G.degree)[5])
# print(nx.shortest_path(G, 2, 4))
nx.draw_planar(G, with_labels=True)
plt.show()

# nx.draw_planar(G, with_labels=True)
# plt.show()
