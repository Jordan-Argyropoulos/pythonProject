from collections import deque

'''
print('entrer un chiffre entre 1 à 3 ou zero pour terminer')
a = eval(input())
while a:
    if a == 1:
        print("Message valeur = 1")
    elif a == 2:
        print("Message valeur = 2")
    elif a == 3:
        print("Message valeur = 3")
else:
    print("un nbr entre 1 et 3 svp")
    a = eval(input())
'''
'''
semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']  # tableaux
print("## Les listes ##\n")
print(semaine)
print(semaine[-3:-2])
for j in semaine[:5]:
    print(j)

print(semaine[3])
jour = semaine[0]
semaine[0], semaine[-1] = semaine[-1], semaine[0]

print(semaine)

print(semaine[-1] * 12)

h = 'hello '
w = "world "
l = (h + w) * 4

phrase = 'une belle phrase bien construite'

for i in phrase:
    print(i, end=' ')

print("# Liste et les piles # \n")

pile = deque([0, 2, 5])  # depuis libraries

print(pile)
pile.append(6)
print(pile)
pile.append(7)
file = [pile]
for i in pile:
    print(i, end=' ')
print('\n', pile)
i = 1


voyelles = 'aeiouy'

z = 'i'

if z in voyelles: #appartenance à une liste ( z.in( voyelles )
    print(z, ' est une voyelle \n')
else:
    print(z, 'n''est pas une voyelle')


while True:
    mot = input('Entrez un mot : ')
    if mot == '':
        break
    elif mot < 'eau':
        place = ' précéde '
    elif mot > 'eau':
        place = ' suit '
    else:
        place = ' identique '
# afficher la précédence du mot saisi // à 'eau'
    print('Le mot saisi : ', mot, place, 'eau')
'''

liste = ['Un message', 250, '3.14159', ['Albert', 'Einstein', 1905]]
liste1 = ['Monsieur', 'Eddy', 'Dupont', ['rue haute', '16', '6000', 'Charleroi']]

print('Liste complète')
print(liste)
print('Sous liste')
print(liste[3])
print('Element sous liste')
print(liste[3][1])

matrice = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(matrice[0], '\n', matrice[1], '\n', matrice[2], '\n')

for row in matrice:
    for elem in row:
        print(elem, end=' ')
    print()

for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j], end=' ')
    print()



print('correction_____________________________________________')

'''
'''
#
#   Mercredi 10 Mars
#
# Les listes, des piles et des files
#
from collections import deque
# déclarartoins
liste = []
'''
liste.append(1)
print('Liste : ', liste)
liste.append(2)
print('Liste : ', liste)
liste = range(15)
liste = []
print(liste)
for i in range(15):
    liste.append(i)
    print(i)
print(liste)
print(liste[2])
print('Jusqu\'à 2', liste[:2])
print(liste[2:])
semaine = ["lundi", "Mardi", "Mercredi",
           "Jeudi", "Vendredi", "Samedi", "Dimanche"
           ]
print(semaine)
print(semaine[-3:-1])
for j in semaine[:5]:
    print(j)
print('les 5 premiers ...')
for i in range(5):
    print(semaine[i])
# echange de valeur .. on peut modifier les listes ...
print(semaine[3])
semaine[0], semaine[-1] = semaine[-1], semaine[0]
print(semaine)
print(semaine[-1] * 12)
h = 'hello '
w = "world "
l = (h + w)*4
print('l:', l, 'Sous string 13..20', l[12:23])
# afficher un espace => 'a f f i c h e r   u n ...
phrase = 'On gouverne mieux les hommes par leurs vices que par leurs vertus'
# afficher la phrase avec un espace entre chaque lettre
i = 0
print(phrase)
while i < len(phrase):
    print(phrase[i], end=' ')
    i += 1
print('')
for c in phrase:
    print(c, end=' ')
# liste utilisée en pile ..
pile = deque([0, 2, 5]) # Librairie
print(pile)
pile.append(6)
print(pile)
pile.append(7)
file = deque([0, 2, 5, 7, 79, 87])
for i in pile:
    print(i, end=' ')
print('\n', pile)
i = 1
while len(pile) > 0:
    i = pile.pop()  #lifo
    print(pile)
print(file)
a = 1
while len(file) > 0:
    i = file.popleft() #fifo
    if a:
        a = 0
        file.append(pile.pop())
    else:
        a = 1
    print(file)
voyelles = 'aeiouy'
z ='i'
if z in voyelles:  #appartenance à une liste  ( z.in( voyelles )
    print( z, ' est une voyelle' )
while True:
    mot = input('Entrez un mot : ')
    if mot == '':
        break
    elif mot < 'eau':
        place = ' précéde '
    elif mot > 'eau':
        place = ' suit '
    else:
        place =' est identique '
    # afficher la précédence du mot saisi // à 'eau'
    print('Le mot ', mot, place, 'eau')
'''

liste1 = ['Monsieur', 'Eddy', 'Dupont', ['rue haute', '16', '6000', 'Charleroi']]
liste2 = ['Madame', 'Louise', 'Santé', ['rue haute', '16', '6000', 'Charleroi']]
print('Liste compléte')
print(liste1)
print('sous liste')
print(liste2[3])
print('element sous liste')
print(liste2[3][1])

matrice = [[0,1,2],[3,4,5],[6,7,8]]
print(matrice)
# Impression sur 3 lignes
# 0,1,2
# 3,4,5
# 6,7,8
for row in matrice:
    for elem in row:
        print(elem, end='  ')
    print()
    
for i in range(len(matrice)):
    for j in range(len(matrice[i])):
        print(matrice[i][j], end=' ')
    print()

'''
'''