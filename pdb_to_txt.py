#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 20:06:10 2020

@author: andyjiang
"""

pdbFile = open("6qlt.pdb", "r")

txtFile = open("6qlt_coordinates.txt", "w")

pdb_lines = pdbFile.readlines()

atom_lines = []

for i in range(len(pdb_lines)):
    if pdb_lines[i][0:6] == "ATOM  ":
        atom_lines.append(pdb_lines[i])

for j in range(len(atom_lines)):
    l = atom_lines[j]
    txtFile.write(l[76:78] + " " + l[30:38] + " " + l[38:46] + " " + l[46:54] + "\n")
    
pdbFile.close()
txtFile.close()