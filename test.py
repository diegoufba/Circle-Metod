import networkx as nx
import matplotlib.pyplot as plt

G=nx.cycle_graph(4)
H=nx.path_graph(4)

plt.figure(1)
nx.draw(G)
plt.figure(2)
nx.draw(H)

plt.show()