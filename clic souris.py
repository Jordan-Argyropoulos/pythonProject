[21:32] emmanuel_goffaux (Invité)
 Affichage x - y sur clic souris

[21:33] emmanuel_goffaux (Invité)
#! /usr/bin/env python
# -*- coding:Utf8 -*-
# Détection et positionnement d'un clic de souris dans une fenêtre :
from tkinter import *

def pointeur(event):
    chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
                            ", Y =" + str(event.y))

fen = Tk()
cadre = Frame(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine = Label(fen)
chaine.pack()

fen.mainloop()

