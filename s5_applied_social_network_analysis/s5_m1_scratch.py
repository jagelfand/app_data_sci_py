# %%
import networkx as nx
from networkx.algorithms import bipartite

# %%
G=nx.MultiDiGraph()

G.add_edge('John', 'Ana', weight= 3, relation = 'siblings')
G.add_edge('Ana', 'David', weight= 4, relation = 'cousins')
G.add_edge('Ana', 'Bob', weight= 1, relation = 'friends')
G.add_edge('Ana', 'Bob', weight= 1, relation = 'neighbors')

print( G.adj['Bob']['Ana'][1]['relation'] )

# %%
B = nx.Graph()
B.add_edges_from([('A', 'G'),('A','I'), ('B','H'), ('C', 'G'), ('C', 'I'),('D', 'H'), ('E', 'I'), ('F', 'G'), ('F', 'J')])
X1 = set(['A', 'B', 'C', 'D', 'E', 'F'])

G = bipartite.weighted_projected_graph(B, X1)
list(G.edges(data=True))

# %%
