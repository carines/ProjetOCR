#!/usr/bin/python3
# -*- coding: utf8 -*-

# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

# on importe le module os pour dialoguer avec notre systeme exploitation
import os

# On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = input("Saisissez une année : ")
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

os.system("pause")
