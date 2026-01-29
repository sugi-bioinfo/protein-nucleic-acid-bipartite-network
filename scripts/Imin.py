import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
Imin = float(sys.argv[3])

with open(input_file) as f, open(output_file, "w") as out:
    header = f.readline()
    out.write("Protein NucleicAcid I\n")

    for line in f:
        p, n, nij, ni, nj, I = line.split()
        I = float(I)

        if I >= Imin:
            out.write(f"{p} {n} {I:.4f}\n")
