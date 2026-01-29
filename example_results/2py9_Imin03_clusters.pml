load ..\pdb_files\2py9.pdb
hide everything
show cartoon, all
color lightpink, protein
color lightgreen, nucleic
set cartoon_transparency, 0.75, protein
set cartoon_transparency, 0.75, nucleic
bg_color white
set ray_opaque_background, 0
set specular, 0.1
set cartoon_quality, 20
set cartoon_smooth_loops, 1

select Cluster_1, (chain B and resn GLY and resi 30) or (chain B and resn SER and resi 27) or (chain B and resn GLY and resi 26) or (chain E and resn C and resi 9)
show spheres, Cluster_1
color red, Cluster_1
set sphere_scale, 0.55, Cluster_1

select Cluster_2, (chain B and resn ILE and resi 49) or (chain E and resn C and resi 10) or (chain B and resn GLY and resi 33) or (chain B and resn ARG and resi 57) or (chain B and resn ILE and resi 29) or (chain E and resn C and resi 11)
show spheres, Cluster_2
color green, Cluster_2
set sphere_scale, 0.55, Cluster_2

select Cluster_3, (chain E and resn A and resi 7) or (chain B and resn LYS and resi 31)
show spheres, Cluster_3
color blue, Cluster_3
set sphere_scale, 0.55, Cluster_3

select Cluster_4, (chain B and resn ASN and resi 48) or (chain E and resn U and resi 12) or (chain B and resn ARG and resi 40) or (chain B and resn GLU and resi 51)
show spheres, Cluster_4
color yellow, Cluster_4
set sphere_scale, 0.55, Cluster_4

show cartoon, all