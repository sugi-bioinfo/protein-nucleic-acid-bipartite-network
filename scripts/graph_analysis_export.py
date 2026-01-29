import sys
import networkx as nx

edge_file = sys.argv[1]
prefix = sys.argv[2]   # output prefix

G = nx.Graph()

with open(edge_file) as f:
    f.readline()
    for line in f:
        p, d, I = line.split()
        G.add_edge(p, d, weight=float(I))

print("Total nodes:", G.number_of_nodes())
print("Total edges:", G.number_of_edges())

# ----- Degree hubs -----
deg_hubs = sorted(G.degree(), key=lambda x:x[1], reverse=True)[:10]

with open(prefix+"_hubs_degree.txt","w") as f:
    for n,deg in deg_hubs:
        f.write(f"{n} {deg}\n")

# ----- Strength hubs -----
str_hubs = sorted(G.degree(weight="weight"), key=lambda x:x[1], reverse=True)[:10]

with open(prefix+"_hubs_strength.txt","w") as f:
    for n,s in str_hubs:
        f.write(f"{n} {s:.4f}\n")

# ----- Clusters -----
clusters = list(nx.connected_components(G))

with open(prefix+"_clusters.txt","w") as f:
    for i,c in enumerate(clusters,1):
        f.write("Cluster_"+str(i)+": "+" ".join(c)+"\n")

print("Clusters:", len(clusters))
print("Largest cluster size:", len(max(clusters, key=len)))
