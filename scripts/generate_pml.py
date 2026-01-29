import sys
import re

deg_file = sys.argv[1]
str_file = sys.argv[2]
clus_file = sys.argv[3]
pdb_file = sys.argv[4]

cluster_colors=["red","green","blue","yellow","cyan","magenta","orange","purple","teal","lime"]

# ---------------- FILE READERS ----------------

def read_simple(file):
    arr=[]
    with open(file) as f:
        for l in f:
            if l.strip():
                arr.append(l.split()[0])
    return arr

def read_clusters(file):
    clusters=[]
    with open(file) as f:
        for l in f:
            if ":" in l:
                clusters.append(l.split(":")[1].strip().split())
    return clusters

degree_hubs = read_simple(deg_file)
strength_hubs = read_simple(str_file)
clusters = read_clusters(clus_file)

# ---------------- NODE PARSER ----------------

def parse_node(node):
    chain,res=node.split("_")
    m=re.match(r"([A-Z]+)([0-9]+)",res)
    return chain,m.group(1),m.group(2)

def sel_from_node(node):
    c,rn,ri=parse_node(node)
    return f"chain {c} and resn {rn} and resi {ri}"

def label_cmd(node):
    c,rn,ri=parse_node(node)
    if rn in ["DA","DT","DG","DC"]:
        return f"label chain {c} and resi {ri} and name C1', \"{node}\""
    else:
        return f"label chain {c} and resi {ri} and name CA, \"{node}\""

# ---------------- COMMON HEADER ----------------

def header(pml):
    pml.write(f"load {pdb_file}\n")
    pml.write("bg_color white\n")
    pml.write("hide everything\n")
    pml.write("show cartoon, polymer.protein\n")
    pml.write("show cartoon, polymer.nucleic\n")
    pml.write("color lightgrey, polymer.protein\n")
    pml.write("color lightblue, polymer.nucleic\n")
    pml.write("set cartoon_transparency,0.7\n")
    pml.write("set label_size,16\n")
    pml.write("set label_color,black\n")

# ================= HUB DEGREE =================

with open("hub_degree.pml","w") as pml:
    header(pml)
    for h in degree_hubs:
        sel=sel_from_node(h)
        pml.write(f"select hub_{h}, {sel}\n")
        pml.write(f"show sticks, hub_{h}\n")
        pml.write(f"color black, hub_{h}\n")
        pml.write(label_cmd(h)+"\n")
    # Removed zoom

# ================= HUB STRENGTH =================

with open("hub_strength.pml","w") as pml:
    header(pml)
    for h in strength_hubs:
        sel=sel_from_node(h)
        pml.write(f"select hub_{h}, {sel}\n")
        pml.write(f"show sticks, hub_{h}\n")
        pml.write(f"color hotpink, hub_{h}\n")
        pml.write(label_cmd(h)+"\n")
    # Removed zoom

# ================= CLUSTERS + INTERACTIONS =================

with open("clusters.pml","w") as pml:
    header(pml)

    for c,cluster in enumerate(clusters):
        sels=[]
        for n in cluster:
            sels.append("("+sel_from_node(n)+")")

        pml.write(f"select clus{c+1}, "+" or ".join(sels)+"\n")
        pml.write(f"show sticks, clus{c+1}\n")
        pml.write(f"color {cluster_colors[c%10]}, clus{c+1}\n")

        for n in cluster:
            pml.write(label_cmd(n)+"\n")

        # ---- Hydrogen Bonds ----
        pml.write(f"dist hb{c+1}, clus{c+1} and donors, clus{c+1} and acceptors, 3.5\n")
        pml.write(f"set dash_color, cyan, hb{c+1}\n")

        # ---- Salt Bridges ----
        pml.write(f"dist sb{c+1}, clus{c+1} and resn ARG+LYS+HIS, clus{c+1} and resn ASP+GLU, 4.0\n")
        pml.write(f"set dash_color, red, sb{c+1}\n")

        # ---- Cation–Pi ----
        pml.write(f"dist cp{c+1}, clus{c+1} and resn ARG+LYS+HIS, clus{c+1} and resn PHE+TYR+TRP, 6.0\n")
        pml.write(f"set dash_color, orange, cp{c+1}\n")

        # ---- Pi–Pi stacking ----
        pml.write(f"dist pp{c+1}, clus{c+1} and resn PHE+TYR+TRP, clus{c+1} and resn PHE+TYR+TRP, 6.0\n")
        pml.write(f"set dash_color, purple, pp{c+1}\n")

    

print("Generated:")
print(" hub_degree.pml")
print(" hub_strength.pml")
print(" clusters.pml")
