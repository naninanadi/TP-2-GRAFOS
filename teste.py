import networkx as nx
import matplotlib.pyplot as plt
import gcol

G = nx.dodecahedral_graph()
c = gcol.node_coloring(G)
print("Here is a node coloring of graph G:", c)
nx.draw_networkx(G, node_color=gcol.get_node_colors(G, c))
plt.show()