#
# utilisation des menus
#
#
from tkinter import *
def ouvrir():
    print('Ouvrir')

def enregistrer():
    print('Enregistrer')

def enregisSous():
    print('Enregistrer saoul...')

def quitter():
    fenetre.quit()


fenetre = Tk()
menubar = Menu(fenetre)
fenetre.config(menu=menubar)

menufichier = Menu(menubar, tearoff=0)
menuEdit = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Fichier", menu=menufichier)
menubar.add_cascade(label="Edit", menu=menuEdit)


menufichier.add_command(label="Ouvrir ", command=ouvrir)
menufichier.add_separator()
menufichier.add_command(label="Enregistrer", command=enregistrer)
menufichier.add_command(label="Enregistrer sous", command=enregisSous)
menufichier.add_separator()
menufichier.add_command(label="Quitter", command=quitter)

fenetre.mainloop()


"""
Repartir encodage des articles, reception... + expedition
1) creer une structure de menu 3 x 4 actions ( 2 + 12 focntions ) ...
Fichier Article Reception Expedition
Ouvrir Affichage ...
Enregistrer Ajouter ..
Modifier
Supprimer
2) Encoder Article à partir d'une fenetre
'Article ...' 1 champs uniquement .. get
3) relier le tout
Menu <Article> Ajouter
Utilise la fenetre de saisie
...
4) Sauver dans un fichier ..
Mercredi 7-04 de 18h à 20h
mercredi 14-04 de 18h à 20 h
emmanuel_goffaux@hotmail.com
"""