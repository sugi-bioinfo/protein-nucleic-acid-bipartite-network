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
select clus1, (chain B and resn GLY and resi 30) or (chain B and resn SER and resi 27) or (chain B and resn GLY and resi 26) or (chain E and resn C and resi 9)
show sticks, clus1
color red, clus1
label chain B and resi 30 and name CA, "B_GLY30"
label chain B and resi 27 and name CA, "B_SER27"
label chain B and resi 26 and name CA, "B_GLY26"
label chain E and resi 9 and name CA, "E_C9"
dist hb1, clus1 and donors, clus1 and acceptors, 3.5
set dash_color, cyan, hb1
dist sb1, clus1 and resn ARG+LYS+HIS, clus1 and resn ASP+GLU, 4.0
set dash_color, red, sb1
dist cp1, clus1 and resn ARG+LYS+HIS, clus1 and resn PHE+TYR+TRP, 6.0
set dash_color, orange, cp1
dist pp1, clus1 and resn PHE+TYR+TRP, clus1 and resn PHE+TYR+TRP, 6.0
set dash_color, purple, pp1
select clus2, (chain B and resn ILE and resi 49) or (chain E and resn C and resi 10) or (chain B and resn GLY and resi 33) or (chain B and resn ARG and resi 57) or (chain B and resn ILE and resi 29) or (chain E and resn C and resi 11)
show sticks, clus2
color green, clus2
label chain B and resi 49 and name CA, "B_ILE49"
label chain E and resi 10 and name CA, "E_C10"
label chain B and resi 33 and name CA, "B_GLY33"
label chain B and resi 57 and name CA, "B_ARG57"
label chain B and resi 29 and name CA, "B_ILE29"
label chain E and resi 11 and name CA, "E_C11"
dist hb2, clus2 and donors, clus2 and acceptors, 3.5
set dash_color, cyan, hb2
dist sb2, clus2 and resn ARG+LYS+HIS, clus2 and resn ASP+GLU, 4.0
set dash_color, red, sb2
dist cp2, clus2 and resn ARG+LYS+HIS, clus2 and resn PHE+TYR+TRP, 6.0
set dash_color, orange, cp2
dist pp2, clus2 and resn PHE+TYR+TRP, clus2 and resn PHE+TYR+TRP, 6.0
set dash_color, purple, pp2
select clus3, (chain E and resn A and resi 7) or (chain B and resn LYS and resi 31)
show sticks, clus3
color blue, clus3
label chain E and resi 7 and name CA, "E_A7"
label chain B and resi 31 and name CA, "B_LYS31"
dist hb3, clus3 and donors, clus3 and acceptors, 3.5
set dash_color, cyan, hb3
dist sb3, clus3 and resn ARG+LYS+HIS, clus3 and resn ASP+GLU, 4.0
set dash_color, red, sb3
dist cp3, clus3 and resn ARG+LYS+HIS, clus3 and resn PHE+TYR+TRP, 6.0
set dash_color, orange, cp3
dist pp3, clus3 and resn PHE+TYR+TRP, clus3 and resn PHE+TYR+TRP, 6.0
set dash_color, purple, pp3
select clus4, (chain B and resn ASN and resi 48) or (chain E and resn U and resi 12) or (chain B and resn ARG and resi 40) or (chain B and resn GLU and resi 51)
show sticks, clus4
color yellow, clus4
label chain B and resi 48 and name CA, "B_ASN48"
label chain E and resi 12 and name CA, "E_U12"
label chain B and resi 40 and name CA, "B_ARG40"
label chain B and resi 51 and name CA, "B_GLU51"
dist hb4, clus4 and donors, clus4 and acceptors, 3.5
set dash_color, cyan, hb4
dist sb4, clus4 and resn ARG+LYS+HIS, clus4 and resn ASP+GLU, 4.0
set dash_color, red, sb4
dist cp4, clus4 and resn ARG+LYS+HIS, clus4 and resn PHE+TYR+TRP, 6.0
set dash_color, orange, cp4
dist pp4, clus4 and resn PHE+TYR+TRP, clus4 and resn PHE+TYR+TRP, 6.0
set dash_color, purple, pp4
