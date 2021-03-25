#
#   Gestion articles et réceptions
#
import os
import csv
import json
'''
Exercice 4.1
Créer une application qui offre les fonctions suivantes
Gestion Article, Réception Encodage, Reception Validation
- Encodage des articles
    Code article, intitulé, prix, inventaire
    Ajout-Modification-suppression
    Sauvegarde dans un fichier articles.csv (dico1)
- Encodage des receptions d'inventaire de la journée
    Ajout reception
        article quantité
    Modification
    Suppression
    Sauvegarde dans un fichier reception.csv ( dico2 )
- Validation reception
    Mettre à jour l'inventaire avec les receptions du jour

'''

from menu import Menu
def valide(msg, choice):
    """ Fonction d'affichage de message et de confirmation """
    c = ''
    #  saisie caractère autorisé
    while c not in choice:
        c = input(msg)
    return c
def ecritureC ( fichier, dico):
    """ Ecriture fichier """
    with open(fichier, 'w') as f:
        for k, v in dico.items():
            f.write('{},{}\n'.format(k, v))
    return
def ecriture( fichier, dico):
    """ Ecriture JSON"""
    with open( fichier, 'w') as f:
        json.dump(f, dico)

def lecture (fichier):
    """ Lecture ficheir JSON """
    dict = {}
    # nested dico
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            dict = json.load(f)
    else:
        print('Fichier:', fichier, ' inexistant')
    return dict

# Fonctions de gestion des articles

# Fonctions de gestion receptions

# Effectuer la réceptions des articles
def effectuerReception(articles, receptions):
    """ reception des arciles : mise à jour des qty"""
    for r, q in receptions.items():
        if r in articles:
            articles[r]['qty'] += q # increment de la quantité
            print('Add q', q, '->', articles[r])
        else:
            print('Article ', r, ' inexistant, reception impossible')
            if valide("Ajouter article", ('o','n')) =='o':
                print('Ajout articles', r) #  ajoute un article ...
menu = Menu()
# article, clé, nom, prix, qté
articles ={'art1':{'nom':'Ecran','prix':200, 'qty':12},
           'art2':{'nom':'Clavier','prix': 23, 'qty':9}}
fileArticles = 'article.csv'
receptions = {'art1':4,
            'art2':7,
            'art3':10}
fileRecept ='receptions.csv'
#ecriture(fileArticles, articles)
#art = lecture(fileArticles)
#print(art)

if valide('Msg a afficher <o,n>:', ('o','O','n','N')) == 'o':
    print('Ok')
else:
    print('not ok')

if valide('Réception des articles ?<o n>', ('o','n')) == 'o':
    effectuerReception(articles, receptions)
print(menu)