import networkx as nx
import matplotlib.pyplot as plt

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
g = nx.Graph()
g.add_nodes_from(vertices)
g.add_edges_from(edges)
nx.draw(g, with_labels=True, node_color="y", node_size=800)

print(nx.degree_centrality(g))
print(nx.betweenness_centrality(g))
print(nx.closeness_centrality(g))

centrality = nx.eigenvector_centrality(g)
sorted((v, "{:0.2f}".format(c)) for v, c in centrality.items())
