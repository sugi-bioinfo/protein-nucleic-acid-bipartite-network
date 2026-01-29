import sys, os

pdb_file = sys.argv[1]
cluster_file = sys.argv[2]

base = os.path.splitext(os.path.basename(cluster_file))[0]
output_pml = base + ".pml"

cluster_colors = [
    "red","green","blue","yellow","magenta",
    "purple","teal","salmon","lime","violet",
    "marine","orange","pink","forest"
]

pml = []

# --- Load structure ---
pml.append(f"load {pdb_file}")
pml.append("hide everything")

# --- Base faint cartoon ---
pml.append("show cartoon, all")
pml.append("color lightpink, protein")
pml.append("color lightgreen, nucleic")

pml.append("set cartoon_transparency, 0.75, protein")
pml.append("set cartoon_transparency, 0.75, nucleic")

# --- Clean look ---
pml.append("bg_color white")
pml.append("set ray_opaque_background, 0")
pml.append("set specular, 0.1")
pml.append("set cartoon_quality, 20")
pml.append("set cartoon_smooth_loops, 1\n")

# --- Cluster spheres only ---
with open(cluster_file) as f:
    for i, line in enumerate(f):
        if not line.strip():
            continue

        cname, residues = line.strip().split(":")
        cname = cname.strip()
        residues = residues.split()

        parts = []
        for r in residues:
            p = r.split("_")
            chain = p[0]
            res = p[1]

            resn = "".join(c for c in res if c.isalpha())
            resi = "".join(c for c in res if c.isdigit())

            parts.append(f"(chain {chain} and resn {resn} and resi {resi})")

        sel = " or ".join(parts)
        color = cluster_colors[i % len(cluster_colors)]

        pml.append(f"select {cname}, {sel}")
        pml.append(f"show spheres, {cname}")
        pml.append(f"color {color}, {cname}")
        pml.append(f"set sphere_scale, 0.55, {cname}\n")

# --- Important: ensure cartoon stays visible ---
pml.append("show cartoon, all")

with open(output_pml, "w") as out:
    out.write("\n".join(pml))

print("PML generated:", output_pml)
