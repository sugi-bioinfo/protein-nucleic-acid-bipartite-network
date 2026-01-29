from Bio.PDB import PDBParser
import sys
import numpy as np

pdb_file = sys.argv[1]
out_file = sys.argv[2]
cutoff = 4.5

parser = PDBParser(QUIET=True)
structure = parser.get_structure("complex", pdb_file)
model = structure[0]

PROTEIN_NAMES = {
    "ALA","ARG","ASN","ASP","CYS","GLU","GLN","GLY","HIS","ILE",
    "LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"
}

NUCLEIC_NAMES = {
    "DA","DT","DG","DC",   # DNA
    "A","U","G","C",       # RNA
    "RA","RU","RG","RC"
}

protein = []
nucleic = []

for chain in model:
    for res in chain:
        if res.id[0] != " ":
            continue

        resname = res.get_resname()

        if resname in PROTEIN_NAMES:
            protein.append(res)

        elif resname in NUCLEIC_NAMES:
            nucleic.append(res)

def residue_id(res):
    chain = res.get_full_id()[2]
    resnum = res.get_id()[1]
    resname = res.get_resname()
    return f"{chain}_{resname}{resnum}"

with open(out_file, "w") as f:
    f.write("Protein NucleicAcid RawContacts\n")
    for p in protein:
        for n in nucleic:
            count = 0
            for a1 in p:
                if a1.element == "H":
                    continue
                for a2 in n:
                    if a2.element == "H":
                        continue
                    dist = np.linalg.norm(a1.coord - a2.coord)
                    if dist <= cutoff:
                        count += 1
            
            if count > 0:
                f.write(f"{residue_id(p)} {residue_id(n)} {count}\n")
