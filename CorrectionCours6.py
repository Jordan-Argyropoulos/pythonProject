#
# Excerice sur les menus
#
import os
import csv


def afficher():
    print('Fonction Afficher ')


def sauvegarder():
    print('Fonction Sauvegarder ')


def modifier():
    print('Fonction Modifier ')


def quitter():
    print('Fonction quitter ')

'''
# dictionnaire
menu = {'1': ('Afficher', afficher),    # Numero, menu et fonction associée
        '2': ('sauvegarder', sauvegarder),
        '3': ('modifier', modifier),
        'q': ('Quitter', quitter)
        }
c = '1'
while c != 'q':
    for c, l in menu.items():
        v, funct = l
        print('{} - {}'.format(c, v))
    c = input('Votre choix:')
    if c in menu:  # test appartenance
        print('votre choix : {}'.format(menu[c][0]))
        menu[c][1]() #execution de la fonction associée au choix du dictionnaire
'''
class Menu:
    """ Classe Menu"""
    def __init__(self):
        self.menu = {}
    def add(self, num, txt, func):
        self.menu[num] = (txt, func)
    def run(self):
        """ Affichage et execution du menu """
        c = '1'
        while c != 'q':
            # Affichage du menu
            for c, l in self.menu.items():
                print('{} - {}'.format(c, l[0]))
            # demander le choix
            c = input('Votre choix:')
            if c in self.menu:  # test appartenance
                print('votre choix : {}'.format(self.menu[c][0]))
                self.menu[c][1]()  # execution de la fonction associée au choix du dictionnaire

print( os.getcwd())
# déclarer un objet Menu
menu = Menu()
# initialiser les différentes options
menu.add('1', 'Afficher', afficher)
menu.add('2', 'Sauvegarder', sauvegarder)
menu.add('3', 'Modifier', modifier)
menu.add('q', 'Quitter', quitter)
# Execution du menu
menu.run()


'''
path = 'C:\\Users\\egof\\Documents\\Personnel\\PY\\'
print(path)
file = "matheux.tx1"
fileName = path + file
print(fileName)
# fonctions OS ...
if os.path.exists(fileName):
    print(fileName + ' ok')
else:
    print(filename + ' not ok')
f = open(fileName, 'r')
from pathlib import Path
home = str(Path.home())
print(home)
dic = {}
fichier = csv.reader(f)
for line in fichier:
    print(line)
    k, v = line
    dic[k] = v
print(dic)
f.close()
print(fileName)
f = open('matheux.tx1', 'w')
for k, v in dic.items():
    f.write('{},{}\n'.format(k, v))
    e = k+','+v+'\n'
    f.write(e)
f.close()
print(os.getcwd())
'''
'''
Exercice 3.2 
Créer un programme qui construit un dictionnaire Français Anglais
Afficher le dictionnaire
Ajouter un mot
Modifier un mot
Supprimer un mot
Sauver le dictionnaire sur un fichier
Charger le dictionnaire à partir d’un fichier
'''
'''
Exercice 4.1
Créer une application qui offre les fonctions suivantes 
Gestion Article, Réception Encodage, Reception Validation 
- Encodage des article 
    Code article, intitulé, prix, inventaire
    Ajout-Modification-suppression
    Sauvegarde dans un fichier
- Encodage des receptions d'inventaire de la journée
    Ajout reception 
        article quantité
    Modifciation
    Suppression
    Sauvegarde
- Validation reception
    Mettre à jour l'inventaire avec les receptions du jour
'''