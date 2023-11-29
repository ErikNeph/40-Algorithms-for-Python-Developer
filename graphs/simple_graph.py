import networkx as nx

g = nx.Graph()
g.add_node("Mike")
g.add_nodes_from(["Amina", "Nick", "Jax"])
g.add_edge("Mike", "Amina")
g.add_edge("Amina", "Erik")
