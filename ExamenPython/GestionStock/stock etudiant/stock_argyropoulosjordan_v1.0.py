"""
Nom: Argyropoulos Prénom: Jordan
Adresse: argyropoulosjordan@gmail.com

Cours: Programmation Orienté Objet
Année scolaire: 2020-2021
Ecole: IETC - Condorcet Charleroi - Promotion social
"""

from tkinter import *
from tkinter.filedialog import *
import csv

# entreNom = ""
donneNom = ""

file = open("inventaire_argyropoulosjordan_v1.0.csv")
article = csv.reader(file)
data = list(article)

# del (data[0])
# articleInv = []##
#

articleCb = []
articleNom = []
articleQty = []
articlePrx = []

recepCb = []
recepNom = []
recepQty = []
recepPrx = []

expCb = []
expNom = []
expQty = []
expPrx = []


#######################################################
#                                                     #
#           Definition des fonctions                  #
#                                                     #
#######################################################


def afficstr(temp):
    """afficher texte dans fenêtre principale"""
    tmpFen = temp
    cblabel = Label(tmpFen, text="Référence").grid(row=0, column=0)
    artlabel = Label(tmpFen, text="Nom").grid(row=0, column=1)
    qtylabel = Label(tmpFen, text="Quantité").grid(row=0, column=2)
    pricelabel = Label(tmpFen, text="Prix").grid(row=0, column=3)


def affichage_art():
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


def ouvrir_art():
    """ouvre fichier inventaire"""
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('csv files', '.csv'), ('all files', '.*')])
    fichier = open(filename, "r")
    content = csv.reader(fichier)
    data = list(content)
    del (data[0])

    for x in list(range(0, len(data))):
        articleCb.append(data[x][0])
        articleNom.append(data[x][1])
        articleQty.append(int(data[x][2]))
        articlePrx.append(int(data[x][3]))
    fichier.close()


def ajout_art():
    """confirmation d'ajout d'un article inventaire"""
    global entreCb, entreNom, entreQty, entrePrx, ajv, articleCb
    for x in list(range(0, len(articleCb))):
        if x == entreCb:
            print("test")
    articleCb.append(entreCb.get())
    articleNom.append(entreNom.get())
    articleQty.append(entreQty.get())
    articlePrx.append(entrePrx.get())
    ajPopup = Tk()
    ajPopup.geometry("500x50")
    tmpStr = ("L'article {} avec le codebare {} à été ajouté, n'oubliez pas de sauvegarder".format(entreNom.get(),
                                                                                                   entreCb.get()))
    strLabel = Label(ajPopup, text=tmpStr).grid(row=1, column=0)
    popQuit = Button(ajPopup, text='Quitter', command=lambda: quit(ajPopup))
    popQuit.grid(row=2, column=0)
    ajPopup.mainloop()


def ajout_inv():
    """fenêtre d'Ajout d'article inventaire"""
    global donneNom
    global entreCb, entreNom, entreQty, entrePrx, ajv
    ajv = Tk()
    ajv.geometry("600x150")
    donneCb = StringVar()
    donneNom = StringVar()
    donneQty = IntVar()
    donnePrx = IntVar()
    afficstr(ajv)
    entreCb = Entry(ajv, textvariable=donneCb, bg='black', fg='white')
    entreCb.grid(row=1, column=0)
    entreNom = Entry(ajv, textvariable=donneNom, bg='black', fg='white')
    entreNom.grid(row=1, column=1)
    entreQty = Entry(ajv, textvariable=donneQty, bg='black', fg='white')
    entreQty.grid(row=1, column=2)
    entrePrx = Entry(ajv, textvariable=donnePrx, bg='black', fg='white')
    entrePrx.grid(row=1, column=3)
    ajouter = Button(ajv, text='Ajouter', command=ajout_art)
    ajouter.grid(row=1, column=4)
    ajvQuit = Button(ajv, text='Quitter', command=lambda: quit(ajv))
    ajvQuit.grid(row=2, column=4)

    ajv.mainloop()


def supprimer(num, suPopup):
    """suppression"""
    del articleCb[num], articleNom[num], articleQty[num], articlePrx[num]
    suPopup.destroy()


def supprimer_art(tempo):
    """confirmation Fonction suppression d'article"""
    for x in list(range(0, len(articleCb))):
        if tempo == articleCb[x]:
            suPopup = Tk()
            suPopup.geometry("500x100")
            tmpStr = (
                "L'article {} avec le codebare {}\n va être supprimer, Voulez-vous continuer?".format(articleNom[x],
                                                                                                      articleCb[x]))
            tmpStr = Label(suPopup, text=tmpStr).grid(row=1, column=0)
            popConti = Button(suPopup, text='continuer', command=lambda: supprimer(x, suPopup))
            popConti.grid(row=2, column=1)
            popQuit = Button(suPopup, text='annuler', command=lambda: quit(suPopup))
            popQuit.grid(row=2, column=0)
            suPopup.mainloop()
            break


def supprimer_inv():
    """fonction suppression d'article"""
    supV = Tk()
    supV.geometry("600x150")
    donneCb = StringVar()
    supCb = Entry(supV, textvariable=donneCb, bg='black', fg='white')
    supCb.grid(row=1, column=0)
    ajouter = Button(supV, text='supprimer', command=lambda: supprimer_art(supCb.get()))
    ajouter.grid(row=1, column=4)
    supQuit = Button(supV, text='Quitter', command=lambda: quit(supV))
    supQuit.grid(row=2, column=4)


def ouvrir_recep():
    """ouvre un fichier csv reception"""
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('csv files', '.csv'), ('all files', '.*')])
    fichier = open(filename, "r")
    content = csv.reader(fichier)
    data2 = list(content)
    del (data2[0])

    for x in list(range(0, len(data2))):
        recepCb.append(data2[x][0])
        recepNom.append(data2[x][1])
        recepQty.append(int(data2[x][2]))
        recepPrx.append(int(data2[x][3]))
    fichier.close()


def affichage_recep():
    """Affiche inventaire"""
    afficstr(fenetre)
    var = StringVar(value=recepNom)
    var2 = IntVar(value=recepQty)
    var3 = IntVar(value=recepPrx)
    var4 = StringVar(value=recepCb)
    listbox1 = Listbox(fenetre, listvariable=var)
    listbox1.grid(row=1, column=1)
    listbox2 = Listbox(fenetre, listvariable=var2)
    listbox2.grid(row=1, column=2)
    listbox3 = Listbox(fenetre, listvariable=var3)
    listbox3.grid(row=1, column=3)
    listbox4 = Listbox(fenetre, listvariable=var4)
    listbox4.grid(row=1, column=0)


def ajout_recep():
    """confirmation d'ajout d'un article reception"""
    global entreCb, entreNom, entreQty, entrePrx, ajv, articleCb
    for x in list(range(0, len(articleCb))):
        if x == entreCb:
            print("test")
    recepCb.append(entreCb.get())
    recepNom.append(entreNom.get())
    recepQty.append(entreQty.get())
    recepPrx.append(entrePrx.get())
    ajPopup = Tk()
    ajPopup.geometry("500x50")
    tmpStr = ("L'article {} avec le codebare {} à été ajouté, n'oubliez pas de sauvegarder".format(entreNom.get(),
                                                                                                   entreCb.get()))
    strLabel = Label(ajPopup, text=tmpStr).grid(row=1, column=0)
    popQuit = Button(ajPopup, text='Quitter', command=lambda: quit(ajPopup))
    popQuit.grid(row=2, column=0)
    ajPopup.mainloop()


def ajout_fenetre():
    """fenêtre d'Ajout d'article reception"""
    global donneNom
    global entreCb, entreNom, entreQty, entrePrx, ajv
    ajv = Tk()
    ajv.geometry("600x150")
    donneCb = StringVar()
    donneNom = StringVar()
    donneQty = IntVar()
    donnePrx = IntVar()
    afficstr(ajv)
    entreCb = Entry(ajv, textvariable=donneCb, bg='black', fg='white')
    entreCb.grid(row=1, column=0)
    entreNom = Entry(ajv, textvariable=donneNom, bg='black', fg='white')
    entreNom.grid(row=1, column=1)
    entreQty = Entry(ajv, textvariable=donneQty, bg='black', fg='white')
    entreQty.grid(row=1, column=2)
    entrePrx = Entry(ajv, textvariable=donnePrx, bg='black', fg='white')
    entrePrx.grid(row=1, column=3)
    ajouter = Button(ajv, text='Ajouter', command=ajout_recep)
    ajouter.grid(row=1, column=4)
    ajvQuit = Button(ajv, text='Quitter', command=lambda: quit(ajv))
    ajvQuit.grid(row=2, column=4)

    ajv.mainloop()


def supprimer_recep(num, suPopup):
    """suppression"""
    del recepCb[num], recepNom[num], recepQty[num], recepPrx[num]
    suPopup.destroy()


def supprimer_recep_pop(tempo):
    """confirmation Fonction suppression d'article"""
    for x in list(range(0, len(recepCb))):
        if tempo == recepCb[x]:
            suPopup = Tk()
            suPopup.geometry("500x50")
            tmpStr = (
                "L'article {} avec le codebare {} va être supprimer, Voulez-vous continuer?".format(recepNom[x],
                                                                                                    recepNom[x]))
            strLabel = Label(suPopup, text=tmpStr).grid(row=1, column=0)
            popConti = Button(suPopup, text='continuer', command=lambda: supprimer_recep(x, suPopup))
            popConti.grid(row=2, column=1)
            popQuit = Button(suPopup, text='annuler', command=lambda: quit(suPopup))
            popQuit.grid(row=2, column=0)
            suPopup.mainloop()
            break


def supprimer_recep_fenetre():
    """fonction suppression d'article"""
    supV = Tk()
    supV.geometry("600x150")
    donneCb = StringVar()
    supCb = Entry(supV, textvariable=donneCb, bg='black', fg='white')
    supCb.grid(row=1, column=0)
    ajouter = Button(supV, text='supprimer', command=lambda: supprimer_art(supCb.get()))
    ajouter.grid(row=1, column=4)
    supQuit = Button(supV, text='Quitter', command=lambda: quit(supV))
    supQuit.grid(row=2, column=4)


def ouvrir_expedition():
    """ouvre un fichier csv reception"""
    filename = askopenfilename(title="Ouvrir votre document", filetypes=[('csv files', '.csv'), ('all files', '.*')])
    fichier = open(filename, "r")
    content = csv.reader(fichier)
    data2 = list(content)
    del (data2[0])

    for x in list(range(0, len(data2))):
        expCb.append(data2[x][0])
        expNom.append(data2[x][1])
        expQty.append(int(data2[x][2]))
        expPrx.append(int(data2[x][3]))
    fichier.close()


def affichage_expedition():
    """Affiche inventaire"""
    afficstr(fenetre)
    var = StringVar(value=expNom)
    var2 = IntVar(value=expQty)
    var3 = IntVar(value=expPrx)
    var4 = StringVar(value=expCb)
    listbox1 = Listbox(fenetre, listvariable=var)
    listbox1.grid(row=1, column=1)
    listbox2 = Listbox(fenetre, listvariable=var2)
    listbox2.grid(row=1, column=2)
    listbox3 = Listbox(fenetre, listvariable=var3)
    listbox3.grid(row=1, column=3)
    listbox4 = Listbox(fenetre, listvariable=var4)
    listbox4.grid(row=1, column=0)


def ajout_exp():
    """confirmation d'ajout d'un article reception"""
    global entreCb, entreNom, entreQty, entrePrx, ajv, articleCb
    for x in list(range(0, len(articleCb))):
        if x == entreCb:
            print("test")
    expCb.append(entreCb.get())
    expNom.append(entreNom.get())
    expQty.append(entreQty.get())
    expPrx.append(entrePrx.get())
    ajPopup = Tk()
    ajPopup.geometry("500x50")
    tmpStr = ("L'article {} avec le codebare {} à été ajouté, n'oubliez pas de sauvegarder".format(entreNom.get(),
                                                                                                   entreCb.get()))
    strLabel = Label(ajPopup, text=tmpStr).grid(row=1, column=0)
    popQuit = Button(ajPopup, text='Quitter', command=lambda: quit(ajPopup))
    popQuit.grid(row=2, column=0)
    ajPopup.mainloop()


def ajout_expedition():
    """fenêtre d'Ajout d'article reception"""
    global donneNom
    global entreCb, entreNom, entreQty, entrePrx, ajv
    ajv = Tk()
    ajv.geometry("600x150")
    donneCb = StringVar()
    donneNom = StringVar()
    donneQty = IntVar()
    donnePrx = IntVar()
    afficstr(ajv)
    entreCb = Entry(ajv, textvariable=donneCb, bg='black', fg='white')
    entreCb.grid(row=1, column=0)
    entreNom = Entry(ajv, textvariable=donneNom, bg='black', fg='white')
    entreNom.grid(row=1, column=1)
    entreQty = Entry(ajv, textvariable=donneQty, bg='black', fg='white')
    entreQty.grid(row=1, column=2)
    entrePrx = Entry(ajv, textvariable=donnePrx, bg='black', fg='white')
    entrePrx.grid(row=1, column=3)
    ajouter = Button(ajv, text='Ajouter', command=ajout_recep)
    ajouter.grid(row=1, column=4)
    ajvQuit = Button(ajv, text='Quitter', command=lambda: quit(ajv))
    ajvQuit.grid(row=2, column=4)

    ajv.mainloop()


def supprimer_exp(num, suPopup):
    """suppression expedition"""
    del expCb[num], expNom[num], expQty[num], expPrx[num]
    suPopup.destroy()


def supprimer_exp_pop(tempo):
    """confirmation Fonction suppression d'article expedition"""
    for x in list(range(0, len(expCb))):
        if tempo == expCb[x]:
            suPopup = Tk()
            suPopup.geometry("500x50")
            tmpStr = (
                "L'article {} avec le codebare {} va être supprimer, Voulez-vous continuer?".format(expNom[x],
                                                                                                    expNom[x]))
            strLabel = Label(suPopup, text=tmpStr).grid(row=1, column=0)
            popConti = Button(suPopup, text='continuer', command=lambda: supprimer_exp(x, suPopup))
            popConti.grid(row=2, column=1)
            popQuit = Button(suPopup, text='annuler', command=lambda: quit(suPopup))
            popQuit.grid(row=2, column=0)
            suPopup.mainloop()
            break


def supprimer_exp_fenetre():
    """fonction suppression d'article expedition"""
    supV = Tk()
    supV.geometry("600x150")
    donneCb = StringVar()
    supCb = Entry(supV, textvariable=donneCb, bg='black', fg='white')
    supCb.grid(row=1, column=0)
    ajouter = Button(supV, text='supprimer', command=lambda: supprimer_exp_pop(supCb.get()))
    ajouter.grid(row=1, column=4)
    supQuit = Button(supV, text='Quitter', command=lambda: quit(supV))
    supQuit.grid(row=2, column=4)


def sauver():
    """Sauver sur le fichier"""
    global articleCb, articleNom, articleQty, articlePrx
    sav = csv.writer(open("inventaire2.csv", "w", newline=''))
    sav.writerow(["nomanclature"] + ["nom"] + ["quantité"] + ["prix"])
    for x in list(range(0, len(articleCb))):
        sav.writerow([articleCb[x]] + [articleNom[x]] + [articleQty[x]] + [articlePrx[x]])


def ouvrir():
    print("ouvrir")


def quit(fenFerm):
    """ferme les fenêtres"""
    fenFerm.destroy()


def quitter():
    """quitter le programme"""
    raise SystemExit


####################
#       main       #
####################


fenetre = Tk()
menubar = Menu(fenetre)
fenetre.config(menu=menubar)

menuFichier = Menu(menubar, tearoff=0)
menuArticle = Menu(menubar, tearoff=0)
menuReception = Menu(menubar, tearoff=0)
menuExpedition = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Fichier", menu=menuFichier)
menubar.add_cascade(label="Articles", menu=menuArticle)
menubar.add_cascade(label="Reception", menu=menuReception)
menubar.add_cascade(label="Expedition", menu=menuExpedition)

menuFichier.add_command(label="Ouvrir ", command=ouvrir_art)
menuFichier.add_command(label="Ouvrir pour réception ", command=ouvrir_recep)
menuFichier.add_command(label="Ouvrir pour expédition ", command=ouvrir_expedition)
menuFichier.add_command(label="Enregistrer", command=sauver)
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=quitter)

menuArticle.add_command(label="Afficher", command=affichage_art)
menuArticle.add_command(label="Ajouter", command=ajout_inv)
menuArticle.add_command(label="Modifier", command=ouvrir)
menuArticle.add_command(label="Supprimer", command=supprimer_inv)

menuReception.add_command(label="Afficher", command=affichage_recep)
menuReception.add_command(label="Ajouter", command=ajout_fenetre)
menuReception.add_command(label="Modifier", command=ouvrir)
menuReception.add_command(label="Supprimer", command=supprimer_recep_fenetre)

menuExpedition.add_command(label="Afficher", command=affichage_expedition)
menuExpedition.add_command(label="Ajouter", command=ajout_expedition)
menuExpedition.add_command(label="Modifier", command=ouvrir)
menuExpedition.add_command(label="Supprimer", command=supprimer_exp_fenetre)

fenetre.geometry('800x600')

fenetre.mainloop()
