#!/usr/bin/python3
# -*- coding: utf8 -*-

import os

# demande a l'utilisateur de saisir une chaine de caractere
votreChaine=input("Entrez votre chaine de caractère : ")

# enleve les espaces de la phrase
votreChaine=votreChaine.replace(' ','')

# calcul de la longueur de la chaine
# puis savoir ou est la moitie de la chaine pour comparer
# le premier avec le dernier caractere puis le 2eme caractere avec
# l'avant dernier
longueur=len(votreChaine)
moitie=longueur//2

#initialisation de la variable dbt pour le debut de la chaine
#et fin pour la derniere lettre
dbt=0
fin=-1

#boucle sur la moitie de la longueur
#car on teste la 1ere moitie avec la derniere moitie
for cpt in range (moitie):
    #test si meme premiere et derniere lettre
    if (votreChaine[dbt]==votreChaine[fin]):
        #print ("caractere",dbt+1,":",votreChaine[dbt]," et caractere",longueur+fin+1,":",votreChaine[fin])
        print ("caractere %d : %s et caractere %d : %s"%(dbt+1,votreChaine[dbt],longueur+fin+1,votreChaine[fin]))
        dbt=dbt+1
        fin=fin-1
        palyndrome=True
    else:
        palyndrome=False

if (palyndrome):
    print ("C'est un palyndrome")
else:
    print("Ce n'est pas un palyndrome")

os.system("pause")