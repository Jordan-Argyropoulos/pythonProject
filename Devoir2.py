'''
•TP2 :

•Ecrire un programme qui offre les fonctions suivantes :

•Menu avec 4 fonctions :

•1 Afficher une liste

•2 Ajouter un élément à une liste
Si l’élément existe déjà : demander confirmation pour l’ajouter

•3 Retirer le premier élément d’une liste (FIFO)

•4 Retirer le dernier élément d’une liste (LIFO)

•Q : quitter

•

•Input  tester que la valeur est dans un ensemble ( ‘1’, …. ‘4’, ‘Q’)
'''
from collections import deque


def afficher(listeChoix):
    for i in listeChoix:
        print(i, end=' ')
    print('\n')



def ajouter(listeChoix):
    listeChoix.append(input())


def retirerFirst(listeChoix):
    listeChoix.popleft()


def retirerLast(listeChoix):
    listeChoix.pop()


listeChoix = deque(['Balle', 'Portable', 'Vélo', 'Champagne'])


while True:  # this is the main loop
    print(" Sélectionner votre opération")
    print("1. Afficher la liste")
    print("2. Ajouter un élément à la liste")
    print("3. Retirer le premier élément")
    print("4. Retirer le dernier élément")
    choix = input("Enter votre choix (1/2/3/4): ")
    if choix == '1':
        print("Votre liste est ")
        afficher(listeChoix)

    elif choix == '2':
        print("Veuillez entrer un élément :")
        ajouter(listeChoix)
        afficher(listeChoix)

    elif choix == '3':
        print("L'élément de gauche à été supprimé ")
        retirerFirst(listeChoix)
        afficher(listeChoix)

    elif choix == '4':
        print("L'élément de droite à été supprimé ")
        retirerLast(listeChoix)
        afficher(listeChoix)

    else:
        print("Erreur !")

    while True:
        answer = input('Recommencez? (y/n): ')
        if answer not in ('y', 'n'):
            print('Invalid input.')
        elif answer == 'y':
            break
        else:
            print('Goodbye')
            exit()
