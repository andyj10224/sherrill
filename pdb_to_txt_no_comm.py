#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:06:10 2020

@author: andyjiang
"""

pdbFile = open("6qlt.pdb", "r")

txtFile = open("6qlt_coord_protein_no_comm.xyz", "w")

pdb_lines = pdbFile.readlines()

atom_lines = []
hetatm_lines = []

for i in range(len(pdb_lines)):
    if pdb_lines[i][0:6] == "ATOM  ":
        atom_lines.append(pdb_lines[i])

    elif pdb_lines[i][0:6] == "HETATM":
        hetatm_lines.append(pdb_lines[i])

for j in range(len(atom_lines)):
    l = atom_lines[j]
    txtFile.write(l[76:78] + " " + l[30:38] + " " + l[38:46] + " " + l[46:54] + "\n")

ligand_files = []

count = 0

temp = open("ligand0_no_comm.xyz", "w")

ligand_files.append(temp)

for k in range(len(hetatm_lines)):
    het = hetatm_lines[k]
    if k >= 1 and het[22:26] != hetatm_lines[k-1][22:26]:
        count = count + 1
        temp = open("ligand" + str(count) + "_no_comm.xyz", "w")
        ligand_files.append(temp)

    ligand_files[count].write(het[76:78] + " " + het[30:38] + " " + het[38:46] + " " + het[46:54] + "\n")
 

pdbFile.close()
txtFile.close()

for q in range(len(ligand_files)):
    ligand_files[q].close()


