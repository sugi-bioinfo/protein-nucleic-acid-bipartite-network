load ..\pdb_files\2py9.pdb
bg_color white
hide everything
show cartoon, polymer.protein
show cartoon, polymer.nucleic
color lightgrey, polymer.protein
color lightblue, polymer.nucleic
set cartoon_transparency,0.7
set label_size,16
set label_color,black
select clus1, (chain B and resn LYS and resi 23) or (chain B and resn VAL and resi 36) or (chain B and resn ILE and resi 49) or (chain E and resn C and resi 10) or (chain E and resn U and resi 6) or (chain B and resn GLU and resi 51) or (chain E and resn C and resi 11) or (chain B and resn GLY and resi 22) or (chain B and resn ARG and resi 40) or (chain B and resn LYS and resi 32) or (chain B and resn SER and resi 50) or (chain B and resn LYS and resi 31) or (chain E and resn A and resi 8) or (chain B and resn SER and resi 27) or (chain E and resn U and resi 12) or (chain B and resn GLY and resi 26) or (chain B and resn GLY and resi 30) or (chain B and resn ASN and resi 48) or (chain E and resn C and resi 9) or (chain B and resn GLY and resi 33) or (chain B and resn ILE and resi 29) or (chain B and resn ARG and resi 57) or (chain E and resn A and resi 7) or (chain B and resn VAL and resi 25) or (chain B and resn GLY and resi 52)
show sticks, clus1
color red, clus1
label chain B and resi 23 and name CA, "B_LYS23"
label chain B and resi 36 and name CA, "B_VAL36"
label chain B and resi 49 and name CA, "B_ILE49"
label chain E and resi 10 and name CA, "E_C10"
label chain E and resi 6 and name CA, "E_U6"
label chain B and resi 51 and name CA, "B_GLU51"
label chain E and resi 11 and name CA, "E_C11"
label chain B and resi 22 and name CA, "B_GLY22"
label chain B and resi 40 and name CA, "B_ARG40"
label chain B and resi 32 and name CA, "B_LYS32"
label chain B and resi 50 and name CA, "B_SER50"
label chain B and resi 31 and name CA, "B_LYS31"
label chain E and resi 8 and name CA, "E_A8"
label chain B and resi 27 and name CA, "B_SER27"
label chain E and resi 12 and name CA, "E_U12"
label chain B and resi 26 and name CA, "B_GLY26"
label chain B and resi 30 and name CA, "B_GLY30"
label chain B and resi 48 and name CA, "B_ASN48"
label chain E and resi 9 and name CA, "E_C9"
label chain B and resi 33 and name CA, "B_GLY33"
label chain B and resi 29 and name CA, "B_ILE29"
label chain B and resi 57 and name CA, "B_ARG57"
label chain E and resi 7 and name CA, "E_A7"
label chain B and resi 25 and name CA, "B_VAL25"
label chain B and resi 52 and name CA, "B_GLY52"
dist hb1, clus1 and donors, clus1 and acceptors, 3.5
set dash_color, cyan, hb1
dist sb1, clus1 and resn ARG+LYS+HIS, clus1 and resn ASP+GLU, 4.0
set dash_color, red, sb1
dist cp1, clus1 and resn ARG+LYS+HIS, clus1 and resn PHE+TYR+TRP, 6.0
set dash_color, orange, cp1
dist pp1, clus1 and resn PHE+TYR+TRP, clus1 and resn PHE+TYR+TRP, 6.0
set dash_color, purple, pp1
