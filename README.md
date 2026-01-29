Protein–Nucleic Acid Bipartite Network

This repository contains algorithm developed to construct
a bipartite network representation of protein–nucleic acid
complex (Experimentally validated structures) along with example data (including results)

The algorithm identifies protein–nucleic acid atom-atom contacts,
computes interaction strength, applies a threshold (Imin),
and performs cluster analysis.

Author: Sugirtha, Project Associate, IISC.

# Protein–Nucleic Acid Bipartite Network Algorithm

## Description
This repository contains scripts to analyze protein–nucleic acid interactions and build bipartite networks based on structural data. The workflow includes parsing PDB files, computing raw contacts, calculating interaction strengths, building bipartite graphs, and visualizing results in PyMOL.

## Requirements
- Python 3.x  
- Packages: sys, re, math, numpy, networkx, Bio.PDB (PDBParser)  
- PyMOL (for visualization)

## How to Run

1. **Parse PDB file**
```
python scripts/read_pdb.py ../pdb_files/xyz.pdb
```
Output in terminal:
```
Protein residues: XXX
DNA nucleotides: YY
```

2. **Compute raw contacts**
```
python scripts/raw_contacts.py ../pdb_files/xyz.pdb
```
Output in terminal:
```
Protein residues: xxx  DNA nucleotides: yy
Protein-DNA raw contacts: 
A_xxxx B_yyyy 11
A_xxxx B_yyyy 22
```

3. **Save raw contacts to a file**
```
python scripts/save_raw_contacts.py ../pdb_files/xyz.pdb ../results/xyz_raw_contacts.txt
```
- Results are saved in `../results/xyz_raw_contacts.txt`

4. **Compute interaction strength**
```
python scripts/interaction_strength.py ../results/xyz_raw_contacts.txt ../results/xyz_interaction_strength.txt
```
- Results are saved in `../results/xyz_interaction_strength.txt`

5. **Apply Imin to build bipartite edges**
```
python scripts/Imin.py ../results/xyz_interaction_strength.txt ../results/xyz_edges_Imin_0.1.txt 0.1
python scripts/Imin.py ../results/xyz_interaction_strength.txt ../results/xyz_edges_Imin_0.2.txt 0.2
python scripts/Imin.py ../results/xyz_interaction_strength.txt ../results/xyz_edges_Imin_0.3.txt 0.3
```
- Results are saved as separate `xyz_edges_Imin_0x.txt` files        (0x ~ For diff Imin)

6. **Build Bipartite Graph (using edges)**
```
python scripts/graph_analysis.py ../results/xyz_edges_Imin_0.x.txt
```
- Results appear in the terminal

7. **Export graph analysis results**
```
python scripts/graph_analysis_export.py ../results/xyz_edges_Imin_0.x.txt ../results/xyz_Imin0x
```
- Generates text files for hubs (degree, strength) and clusters

8. **Generate PyMOL visualization**
```
python scripts/generate_pml.py ../results/xyz_Imin0x_hubs_degree.txt ../results/xyz_Imin0x_hubs_strength.txt ../results/xyz_Imin0x_clusters.txt ../pdb_files/xyz.pdb
```
Generated PyMOL scripts:
```
hub_degree.pml
hub_strength.pml
clusters.pml
```

## Notes
- Replace `xyz` with the actual PDB ID of the structure you want to analyze.  
- Make sure all input/output directories exist (`../pdb_files/`, `../results/`).
- The results (for given example structureI is also displayed for your reference.
