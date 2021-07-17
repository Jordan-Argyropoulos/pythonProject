import random


# Class
class Jeu(list):
    def __int__(self):
        pass

    def shuffle(self):
        random.shuffle(self)  # Pour de mélanger le jeu.

    def generate(self):
        self.clear()  # permet de créer la liste avant de créer celle-ci.
        num = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']  # Les chiffres...
        genre = [' coeur', ' pique', ' carreau', ' trefle']  # ...et les couleurs
        for couleur in genre:  # La boucle permet de créer les cartes
            for chiffre in num:
                self.append(chiffre + couleur)

    def distribution(self):  # pour la distribution des cartes
        self.shuffle()
        sortie = self[0]
        del self[0]
        return sortie


class Personne(list):
    def __int__(self):
        self.nom = ""

    def __str__(self):
        sortie = "Voici la main du joueur {}  : ".format(self.nom)
        for i in range(len(self) - 1):  # -1 pour ne pas que ça se termnine par la ,
            sortie += self[i]  # on 'append' à la string la valeur de self[i]
            sortie += ", "  # rajout de la virgule, pour que ca soit plus propre.
        sortie += self[len(self) - 1]  # permet d'ajouter la derniere carte,
        sortie += ";"  # pour terminer la main du joueur
        return sortie


def affiche_main(jeu, j1, j2, j3, j4):  # permet d'afficher la main des joueurs
    for i in range(8):
        s = jeu.distribution()
        j1.append(s)
    for i in range(8):
        s = jeu.distribution()
        j2.append(s)
    for i in range(8):
        s = jeu.distribution()
        j3.append(s)
    for i in range(8):
        s = jeu.distribution()
        j4.append(s)


jeu = Jeu()
joueur1 = Personne()
joueur1.nom = "J1"
joueur2 = Personne()
joueur2.nom = "J2"
joueur3 = Personne()
joueur3.nom = "J3"
joueur4 = Personne()
joueur4.nom = "J4"

jeu.generate()
affiche_main(jeu, joueur1, joueur2, joueur3, joueur4)
print(joueur1)
print(joueur2)
print(joueur3)
print(joueur4)
