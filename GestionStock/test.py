from tkinter import *
from tkinter import ttk

def style():
    "Paramétrage du style des widget"
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=22, fieldbackground="#D3D3D3")
    style.map('Treeview', background=[('selected', '#')])

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