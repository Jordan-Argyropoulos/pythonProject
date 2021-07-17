#
# Imprégnation objet

import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.ajouter_boutons()

    def ajout_cnt(self):
    def ajouter_boutons(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.buton = tk.Button(self, text="Quitter", command=self.quit)

        self.label.pack()
        self.bouton.pack()
        self.geometry('400x300')
        self.cadre = tk.Frame(self, widh=200, height=150, bg="light yellow")
        self.cadre.pack()

# Astuce pour lancer un programme main quand c'est le programme qui est lancé <> d'une librairie
if __name__ == "__main__":
    app = Application()
    app.title("Ma premiere App :-)")
    app.mainloop()

    print("Fin de partie")

# # Imprégnation objet # import tkint... par emmanuel_goffaux (Invité)

emmanuel_goffaux (Invité)21:34
#
#   Imprégnation objet
#
import tkinter as tk

class Application(tk.Tk):  # classe qui hérite de tk.Tk()
    def __init__(self):
        tk.Tk.__init__(self)
        self.ajouter_boutons()
        self.cnt = 0
    def ajout_cnt(self):
        self.cnt += 1
        self.msg = 'Cnt = {}'.format(self.cnt)
        self.label.text = self.msg

    def ajouter_boutons(self):
        self.label = tk.Label(self, text="J'adore Python !")
        self.quit = tk.Button(self, text="Quitter", command=self.quit)
        self.ajout = tk.Button(self, text="Incrementer cnt ", command=self.ajout_cnt)
        self.label.pack()
        self.ajout.pack()
        self.quit.pack()
        self.geometry('400x300')
        self.cadre = tk.Frame(self, width=200, height=150, bg="light yellow")
        self.cadre.pack()

#  Astuce pour lancer un programme main quand c'est le programme qui est lancé <> d'une librairie
if __name__ == "__main__":
    app = Application()
    app.title("Ma Première App :-)")
    app.mainloop()

    print('Fin de partie ... ;-) ')

# -*- coding: utf-8 -*-
from tkinter import *
#
#
# utilisation tkinter"
#
#
#  Affichage d'un Label
#
'''
fenetre = Tk()
etiquette = Label(fenetre, text="Bonjour fan de python!")
etiquette.pack()
fenetre.mainloop()
print('Fin de partie')
'''
#   Label & Button
#  Afficher un message suite à une action
#
def action():
    print("Aprés sélection du bouton ...")

f = Tk()

l = Label(f, text="Label : Bonjour le monde !")
l['bg'] = 'black'
l['fg'] = 'yellow'
b = Button(f, text="Bouton : Click here !", command=action)
b['fg'] = 'red'
quit = Button(f, text="Bouton : Quitter", command=f.destroy)
quit['fg'] = 'blue'
b.pack()
l.pack()
quit.pack()
f.title('Une fenetre en python')
f.geometry('400x300')

f.mainloop()

print('Fin de partie s''affiche à la fermeture de la fenetre ')
'''
import tkinter as tk
racine = tk.Tk()
label = tk.Label(racine, text="J'adore Python !")
bouton = tk.Button(racine, text="Quitter", fg="red", command=racine.destroy)
label.pack()
cadre = Frame(racine, width =200, height =150, bg="light yellow")
cadre.pack()
bouton.pack()
racine.mainloop()
# affichage d'un texte et validation action
from tkinter import *
def action():
    print("Yes, we can !")
# impression de la valeur du champ
    val = champ.get()
    print(val)
root = Tk()
w = Label(root, text="Bonjour!")
w.grid(row=0)
champ = Entry(root)
champ.grid(row=1)
b = Button(root,text="Click here !",command=action)
b.grid(row=2)
c = Button(root,text="Quit",command=root.quit)
c.grid(row=3)
root.mainloop()
# éliminer la fenêtre :
root.destroy()
#  Affichage de la factorielle
def factorielle(argu):
    # calcul de la factorielle de argu
    a = 1 # a contient une valeur qui va être incrémentée d'une unité à la fois
    b = 1 # contient la factorielle de a-1
    while a<=argu: # on arrêtera lorsque a sera > argu
        b = b * a
        a = a + 1
    return b
def action():
    texte_n = champ.get()
    n = int(texte_n)
    affichefacto.configure(text =str(factorielle(n)))
root=Tk()
champ = Entry(root)
champ.grid(row=0)
b = Button(root,text="Calcule la factorielle",command=action)
b.grid(row=1)
affichefacto = Label(root)
affichefacto.grid(row=2)
bfin = Button(root,text="Terminer",command=root.quit)
bfin.grid(row=3)
root.mainloop()
# éliminer la fenêtre après avoir quitté :
root.destroy()
'''
