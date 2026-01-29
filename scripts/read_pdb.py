from Bio.PDB import PDBParser
import sys

pdb_file = sys.argv[1]

parser = PDBParser(QUIET=True)
structure = parser.get_structure("complex", pdb_file)
model = structure[0]

protein = []
nucleic_acid = []

PROTEIN_NAMES = {
    "ALA","ARG","ASN","ASP","CYS","GLU","GLN","GLY","HIS","ILE",
    "LEU","LYS","MET","PHE","PRO","SER","THR","TRP","TYR","VAL"
}

NUCLEIC_NAMES = {
    "DA","DT","DG","DC",   # DNA
    "A","U","G","C",       # RNA
    "RA","RU","RG","RC"    # alternate RNA naming
}

for chain in model:
    for res in chain:

        # Skip hetero atoms, water, ions
        if res.id[0] != " ":
            continue

        resname = res.get_resname()

        if resname in PROTEIN_NAMES:
            protein.append(res)

        elif resname in NUCLEIC_NAMES:
            nucleic_acid.append(res)

# Output
print("Protein residues:", len(protein))
print("Nucleic acid residues:", len(nucleic_acid))

