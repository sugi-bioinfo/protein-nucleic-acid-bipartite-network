import sys
import math

input_file = sys.argv[1]
output_file = sys.argv[2]

edges = []

Ni = {}
Nj = {}

with open(input_file) as f:
    header = f.readline()
    for line in f:
        p, n, nij = line.split()
        nij = int(nij)

        edges.append((p, n, nij))

        Ni[p] = Ni.get(p, 0) + nij
        Nj[n] = Nj.get(n, 0) + nij

with open(output_file, "w") as out:
    out.write("Protein NucleicAcid Nij Ni Nj I\n")

    for p, n, nij in edges:
        ni = Ni[p]
        nj = Nj[n]

        I = nij / math.sqrt(ni * nj)

        out.write(f"{p} {n} {nij} {ni} {nj} {I:.4f}\n")
