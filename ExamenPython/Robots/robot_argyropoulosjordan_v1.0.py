"""
Nom: Argyropoulos Prénom: Jordan
Adresse: argyropoulosjordan@gmail.com

Cours: Programmation Orienté Objet
Année scolaire: 2020-2021
Ecole: IETC - Condorcet Charleroi - Promotion social

"""

import time
from tkinter import *
import random
from random import randint

# Fenetre 400X400
largeur = 500
hauteur = 500

# Fenetre Tkinter configuration
root = Tk()
label_zone = Label(root, text="Les Robots")
label_zone.config(font=("Courier", 14))
text_zone = Text(root, height=5, width=52)
text_zone.tag_configure('hors', background='red')
canvas = Canvas(root, width=largeur, height=hauteur, background="white")
canvas.pack(fill="both", expand=True)
label_zone.pack()
text_zone.pack()

# Coordonnées + pas des robots
x1, y1 = 10, 10  # coordonnées initiales
dx, dy = 10, 0  # 'pas' du déplacement

# Formatage du gif en image
imgfile = "rob.gif"
gifsdict = {}
img = PhotoImage(file=imgfile)
gifsdict[imgfile] = img
img_2 = img.subsample(2, 2)


class Robot:
    def __init__(self, x1, y1, nom_rob, type_rob, statut_rob, orientation):
        self.nom_rob = nom_rob
        self.type_rob = type_rob
        self.statut_rob = statut_rob
        self.orientation = orientation
        self.x1 = x1
        self.y1 = y1
        self.canvas = canvas
        self.w_image = canvas.create_image(self.x1, self.y1, image=img_2)  # fonction create_image (argument + image)

    def tourner_droite(self):
        self.orientation = "Sud"
        self.canvas.move(self.w_image, 0, 10)
        root.after(50, self.tourner_droite)
        self.bord()

    def tourner_gauche(self):
        self.orientation = "Nord"
        self.canvas.move(self.w_image, 0, -10)
        root.after(50, self.tourner_gauche)
        self.bord()

    def avancer(self):
        """ Avancer d'une case dans la direction. """
        self.orientation = "Est"
        self.canvas.move(self.w_image, 10, 0)
        root.after(50, self.avancer)
        self.bord()

    def reculer(self):
        """ Reculer d'une case"""
        self.orientation = "Ouest"
        self.canvas.move(self.w_image, -10, 0)
        root.after(50, self.reculer)
        self.bord()

    def bord(self):
        rebond = canvas.bbox(self.w_image)
        if rebond[0] < 0:
            canvas.move(self.w_image, 10, 0)  # gauche
        elif rebond[1] < 0:
            canvas.move(self.w_image, 0, 10)  # haut
        elif rebond[2] > 400:
            canvas.move(self.w_image, -10, 0)  # droite
        elif rebond[3] > 400:
            canvas.move(self.w_image, 0, -10)  # bas

    def test(self):
        if self.statut_rob == " Hors service ":
            text_zone.tag_configure("### HORS SERVICE ###")
            return text_zone.insert(END, "### HORS SERVICE ###")
        elif self.statut_rob == " En maintenance ":
            return text_zone.insert(END, "### EN MAINTENANCE ###")
        else:
            for i in range(1):
                self.afficher()
                test = random.choice([self.avancer, self.reculer, self.tourner_gauche, self.tourner_droite])
                test()

    def __str__(self):
        return '{}, {}, {}, {}, {}, {}'.format(self.x1, self.y1, self.nom_rob, self.type_rob, self.statut_rob,
                                               self.orientation)

    def afficher(self):
        text_zone.insert(END, (x1, y1, self.nom_rob, self.type_rob, self.statut_rob,
                         self.orientation))


# main
# Position de depart des robots
robot1 = Robot(50, 180, " Bob ", " Industriel ", " En service ", " A déterminer ")
robot2 = Robot(300, 30, " Luc ", " Humanoide ", " En maintenance ", " A déterminer ")
robot3 = Robot(400, 50, " Mickael ", " Mobile ", " En service ", " A déterminer ")
robot4 = Robot(60, 350, " Marie ", " Industriel ", " Hors service ", " A déterminer ")

# Boutons pour lancer les robots
bouton_couleur = Button(root, text="Déplacer robot 1", width=20, command=robot1.test)
bouton_couleur.pack(pady=10)
bouton_couleur = Button(root, text="Déplacer robot 2", width=20, command=robot2.test)
bouton_couleur.pack(side=LEFT, pady=10)
bouton_couleur = Button(root, text="Déplacer robot 3", width=20, command=robot3.test)
bouton_couleur.pack(side=RIGHT, pady=10)
bouton_couleur = Button(root, text="Déplacer robot 4", width=20, command=robot4.test)
bouton_couleur.pack(side=BOTTOM, pady=10)
# Bouton quitter
bouton_quitter = Button(root, text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()
