"""
Exercice 4.1
Créer une application qui offre les fonctions suivantes
Gestion Article, Réception Encodage, Reception Validation
- Encodage des article
    Code article, intitulé, prix, inventaire
    Ajout-Modification-suppression
    Sauvegarde dans un fichier articles.csv

- Encodage des receptions d'inventaire de la journée
    Ajout reception
        article quantité
    Modifciation
    Suppression
    Sauvegarde

- Validation reception
    Mettre à jour l'inventaire avec les receptions du jour


"""

#
# Gestion articles et receptions
#
import csv


from menu import Menu


# def valide(msg, choice):
# ''' Fonction d'affichage de message de confirmation '''
#   c = ''
# saisie caractère autorisé
#   while c not in choice:
#       c = input(msg)
#   return c

# def ecriture ( fichier, dico):

# def lecture ( fichier, dico):

#    return dico

# Fonctions de gestion des articles
# 3 fonctions  Encodage des article
#     Code article, intitulé, prix, inventaire
#     Ajout-Modification-suppression
#     Sauvegarde dans un fichier articles.csv

def ajout():
    pass


def modification():
    pass


def suppression():
    pass


dico = {'article1': ('Pâtes', 2.0, 5), 'article2': ('Tomate', 1.5, 3), 'article3': ('Fromage', 3.0, 1),
        'article4': ('Vin', 15.0, 0)}
csv_file = "articles.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=dico)
        writer.writeheader()
        for data in dico:
            writer.writerow(data)
except IOError:
    print("I/O error")

# Fonctions de gestion receptions
"""
menu = Menu()

if (valide('Msg a afficher', ('o','O','n','N'))) =='o':
    print('Ok')
else:
    print('not ok')

print(menu)"""
