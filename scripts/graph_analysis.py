import sys
import networkx as nx

edge_file = sys.argv[1]

G = nx.Graph()

with open(edge_file) as f:
    header = f.readline()
    for line in f:
        p, n, I = line.split()
        I = float(I)

        G.add_node(p, bipartite=0)   # Protein node
        G.add_node(n, bipartite=1)   # Nucleic acid node
        G.add_edge(p, n, weight=I)

print("Total nodes:", G.number_of_nodes())
print("Total edges:", G.number_of_edges())

# Degree hubs
print("\nTop hubs by degree:")
for n,deg in sorted(G.degree(), key=lambda x:x[1], reverse=True)[:10]:
    print(n, deg)

# Weighted hubs
print("\nTop hubs by interaction strength:")
for n,stren in sorted(G.degree(weight="weight"), key=lambda x:x[1], reverse=True)[:10]:
    print(n, f"{stren:.3f}")

# Clusters
components = list(nx.connected_components(G))
print("\nNumber of clusters:", len(components))
print("Largest cluster size:", len(max(components, key=len)))
