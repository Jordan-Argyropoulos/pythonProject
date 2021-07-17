"""
Nom: Argyropoulos Prénom: Jordan
Adresse: argyropoulosjordan@gmail.com

Cours: Programmation Orienté Objet
Année scolaire: 2020-2021
Ecole: IETC - Condorcet Charleroi - Promotion social
"""

import random

choix = ["casserole", "cuillere", "patate", "souris"]
solution = random.choice(choix)

tentatives = 7
affichage = ""
lettres_trouvees = ""
lettres_rate = ""

for l in solution:
    affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ").lower()
    if len(proposition) > 1:
        print("Veuillez introduire une seul lettre à la fois!")
        continue
    if not proposition.isalpha():
        print("Seul les lettres sont autorisée!")
        continue

    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")
    else:
        lettres_rate = lettres_rate + proposition
        tentatives = tentatives - 1
        print("-> Raté!\n")
        print("Lettre(s) proposée :", lettres_rate)
        if tentatives == 0:
            print(" ==========Y= ")
        if tentatives <= 1:
            print(" ||/       |  ")
        if tentatives <= 2:
            print(" ||        0  ")
        if tentatives <= 3:
            print(" ||       /|\ ")
        if tentatives <= 4:
            print(" ||       /|  ")
        if tentatives <= 5:
            print("/||           ")
        if tentatives <= 6:
            print("==============\n")


    affichage = ""
    for x in solution:
        if x in lettres_trouvees:
            affichage += x + " "
        else:
            affichage += "_ "

    if "_" not in affichage:
        print(">>> Gagné! <<<")
        break

print("\n    * Fin de la partie *    ")
