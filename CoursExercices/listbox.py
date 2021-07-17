def afficstr(temp):
    """afficher texte dans fenêtre principale"""
    tmpFen = temp
    cblabel = Label(tmpFen, text="Référence").grid(row=0, column=0)
    artlabel = Label(tmpFen, text="Nom").grid(row=0, column=1)
    qtylabel = Label(tmpFen, text="Quantité").grid(row=0, column=2)
    pricelabel = Label(tmpFen, text="Prix").grid(row=0, column=3)


def affichageArticles():
    """Affiche inventaire"""
    afficstr(fenetre)
    var = StringVar(value=articleNom)
    var2 = IntVar(value=articleQty)
    var3 = IntVar(value=articlePrx)
    var4 = StringVar(value=articleCb)
    listbox1 = Listbox(fenetre, listvariable=var)
    listbox1.grid(row=1, column=1)
    listbox2 = Listbox(fenetre, listvariable=var2)
    listbox2.grid(row=1, column=2)
    listbox3 = Listbox(fenetre, listvariable=var3)
    listbox3.grid(row=1, column=3)
    listbox4 = Listbox(fenetre, listvariable=var4)
    listbox4.grid(row=1, column=0)