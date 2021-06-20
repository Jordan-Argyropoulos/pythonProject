"""

Repartir encodage des articles, reception... + expedition
1) creer une structure de menu  3 x 4 actions ( 2 + 12 focntions ) ...
    Fichier     Article     Reception     Expedition
    Ouvrir       Affichage   ...
    Enregistrer  Ajouter     ..
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


Affichage en mode tableau
Ajout bouton CRUD et champs de saisie

Inspired by codemy.com

"""
"""

Affichage en mode tableau
Ajout bouton CRUD et champs de saisie

Inspired by codemy.com

"""
from tkinter import *
from tkinter import ttk
from files import Rec
import logging


#  Du style que diable ...
def style():
    "Paramétrage du style des widget"
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=22, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', '#')])


#   Classe Tableau Affichage en mode tableau + ajout zone de saisie
class Tableau():
    def __init__(self, fm, header, data):
        # fenetre mere, entete, données
        self.count = 0
        self.data = data
        style()
        self.tf = Frame(fm)
        self.tf.pack(pady=20, side=TOP)
        # Ajouter tableau à gauche
        self.tv = ttk.Treeview(self.tf, selectmode='extended')
        self.tv.pack(side=LEFT)
        print(header)
        print([h for h, a in header])
        # Définition des colonnes
        self.tv['columns'] = [h for h, a in header]
        # Format des colonnes
        self.tv.column('#0', width=0, stretch=NO)
        self.tv.heading('#0', text='', anchor=CENTER)
        logger.info('Initialisation du tableau')
        # structure du tableau
        for titre, align in header:
            print(titre, align)
            # Colonnes
            self.tv.column(titre, anchor=align, width=140)
            #  Titres des colonnes
            self.tv.heading(titre, text=titre, anchor='center')

        # Ajout Scrollbar à droite
        self.sb = Scrollbar(self.tf, orient=VERTICAL)
        self.sb.pack(side=RIGHT, fill=Y)
        self.tv.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tv.yview)

        # Button(ws, text="Show Selected", command=self.show_selected).pack()
        #
        self.tv.tag_configure('oddrow', background='white')
        self.tv.tag_configure('evenrow', background='lightblue')
        self.count = 0
        for rec in data:
            if self.count % 2 == 0:
                self.tv.insert(parent='', index=self.count, iid=self.count, text='', values=rec, tags=('evenrow',))
            else:
                self.tv.insert(parent='', index=self.count, iid=self.count, text='', values=rec, tags=('oddrow',))
            self.count += 1
        self.tv.pack()

        #  Frame encodage des valeurs
        self.lf = LabelFrame(fm, text="Enregistrement", )
        self.lf.pack(fill="x", expand="yes", padx=10)  # , side=BOTTOM)
        #  Ajout des 4 labels
        self.labels = []
        self.entry = []
        i = 0
        for titre, align in header:
            l = Label(self.lf, text=titre)
            l.grid(row=0, column=i, padx=10, pady=10)
            e = Entry(self.lf)
            e.grid(row=1, column=i, padx=10, pady=10)
            self.labels.append(l)
            self.entry.append(e)
            i += 1

        #  Frame pour les boutons d'actions
        self.bf = LabelFrame(fm, text='Actions : <C>reate <R>ead <U>pdate <D>elete', )
        self.bf.pack(fill="x", expand="yes", padx=20, side=BOTTOM)

        #  Boutons d'actions CRUD
        add_button = Button(self.bf, text="Create: Ajout", command=self.add_rec)
        add_button.grid(row=0, column=0, padx=10, pady=10)
        sel_button = Button(self.bf, text="Read: Sélection", command=self.sel_rec)
        sel_button.grid(row=0, column=1, padx=10, pady=10)
        mod_button = Button(self.bf, text="Update: Modification", command=self.mod_rec)
        mod_button.grid(row=0, column=2, padx=10, pady=10)
        del_button = Button(self.bf, text="Delete: Suppression", command=self.del_rec)
        del_button.grid(row=0, column=3, padx=10, pady=10)

    #  Fonctions actions boutons
    def add_rec(self):
        rec = []
        for e in self.entry:
            rec.append(e.get())
            e.delete(0, END)
        #  Correction affichage ...
        self.tv.insert(parent='', index=self.count, iid=self.count, text='', values=rec, tags=('evenrow',))
        self.count += 1
        #  Ajouter mise a jour du fichier ...
        pass

    def mod_rec(self):
        # Recupération des données et reset
        selected = self.tv.focus()
        rec = []
        for e in self.entry:
            rec.append(e.get())
            e.delete(0, END)
        self.tv.item(selected, text="", values=rec)
        #  Ajouter mise a jour du fichier ...
        pass

    def del_rec(self):
        rec = self.tv.selection()[0]
        self.tv.delete(rec)
        self.count -= 1
        # ajouter mise à jours de tags ( even - odd )
        # ajouter sauvegarde des données
        pass

    def sel_rec(self):
        # effacer les valeurs
        rec = self.tv.focus()
        val = self.tv.item(rec, 'values')
        i = 0
        for e in self.entry:
            e.delete(0, END)
            print(val[i])
            e.insert(0, val[i])
            i += 1
        #
        pass


if __name__ == '__main__':
    header = (('id', W), ('Article', W), ('prix', E), ('qty', E))
    data = [[1, 'Ecran 21', 125, 12],
            [2, 'Ecran 24', 32, 16],
            [3, 'Ecran WS', 17, 32],
            [4, 'Ecran 36', 125, 12],
            [5, 'Ecran 37', 32, 16],
            [6, 'souris base', 17, 32],
            [7, 'souris medium ', 25, 0],
            [8, 'souris high', 37, 4],
            [9, 'souris bluetooth', 52, 32],
            [10, 'Clavier base', 17, 32],
            [11, 'Clavier Medium', 33, 12],
            [12, 'Clavier High', 54, 16],
            [13, 'Clavier bluetooth', 102, 32]
            ]

    logger = logging.getLogger('Journalisation des événements')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('../../../Downloads/log.txt')
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)  # file
    formatter = logging.Formatter('%(asctime)s - %(name)s %(levelname)s %(message)s')
    fh.setFormatter(formatter)

    ws = Tk()
    ws.title('Vue tableau')
    ws.geometry('650x500')
    ws['bg'] = '#fb0'
    #  Modification
    artStruct = ['id', 'nom', 'ecran', 'prix', 'qty']
    logger.info('Initialisation')
    fArticles = Rec('articles.csv', artStruct)
    print(fArticles)
    logger.info('Lancement fenetre')
    t = Tableau(ws, header, data)
    ws.mainloop()
    logger.info('Fin du programme')
