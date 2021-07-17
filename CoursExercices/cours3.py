# import Library

import random


#
# Fonctions
#
def carre(n):
    return n * n


def parabole(a, b, c, x):
    return a * x * x + b * x + c


def voiture(marque, model, transmission='Manuelle'):
    print('Voiture :', marque, model, transmission)
    return 'Voiture :' + marque + model + transmission


# Fonction qui retourne la valeur de 2 lancés de dés
def dés_lancé():
    l1 = random.randint(1, 6)
    l2 = random.randint(1, 6)
    return l1, l2


def jeuDeCartes():
    cartes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
    random.shuffle(cartes)
    return cartes


def couleursCartes():
    couleurs = ['pique', 'coeur', 'trefle', 'carreaux']
    random.shuffle(couleurs)
    return couleurs


# Ecrire une fonction qui effectue la somme des 3 paramètres qui lui sont passés
def somme(a, b, c):
    ''' Somme effectue la somme de 3 paramètres'''
    a = 3
    print('Variable globale', a)
    return a + b + c


'''
print('Exercice somme de 3 paramètres ##########')
for x in range(10):
    print(somme(2, 2, 3))
print('Exercice somme de 3 paramètres ##########')
# fin exercise
# ---------------------------------

print('####Carré######')
for a in range(10):
    print('Le carré de', a, 'vaut', carre(a))
print('####Carré V2######')
a = carre(2)
print(a)
print('#####Parabole#####')
for x in range(-10, 10):
    print('Parabole pour = ', x, 'vaut', parabole(1, 2, 1, x))  # x²+2x+1
print('#####Voiture#####')
print((voiture('Fiat', '500', 'Manuelle')))
print((voiture('VW', 'Polo', 'Automatique')))
print((voiture('Audi', '5')))
print('#####Voiture bis#####')
voiture(transmission='4x4', model='A5', marque='Audi')
print('##########')
'''

# for i in range(20):
#    print(random.randint(1, 6))

'''
for i in range(20):
    d1, d2 = dés_lancé()
    print('lancé de 2 dés', d1, '+', d2, '=', d1+d2)
'''
# Construire un jeu de 52 cartes
# Le mélanger
# Tirer au sort 2 ensembles de 10 cartes
# Comparer et afficher les cartes communes aux 2 ensembles

randCarte = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi']
randCouleur = ['pique', 'coeur', 'trefle', 'carreaux']
indexCarte [0, 12] = random.randint(randCarte[0, 12])
print(indexCarte)



