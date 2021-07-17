from tkinter import *

def readValue():
    prenom = lp.get()
    nom = ln.get()
    age = la.get()
    print('Age :', age, 'Nom :', nom, 'Prenom :', prenom)

f = Tk()
ln = Label(f, text="Entre votre nom :")
ln.pack(side=LEFT)
lp = Label(f, text="Entre votre prénom :")
lp.pack(side=LEFT)
la = Label(f, text="Entre votre âge :")
la.pack(side=LEFT)

la = Entry(f)
la.pack(side=RIGHT)
lp = Entry(f)
lp.pack(side=RIGHT)
ln = Entry(f)
ln.pack(side=RIGHT)

read = Button(f, text='Lecture', command=readValue)
read.pack()
quit = Button(f, text='Quitter', command=f.quit)
quit.pack(side=BOTTOM)

f.title('Fenetre Python')
f.geometry('400x300')

f.mainloop()
########################################################
# -*- coding: utf-8 -*-
from tkinter import *
#
#
# utilisation tkinter"
#
def readValue():
    age = ea.get()
    nom = en.get()
    prenom = ep.get()
    print('Prenom:', prenom, 'Nom', nom, 'Age :', age)


f = Tk()
ln = Label(f, text="Nom :")
ln.grid(row=0,column=0)

lp = Label(f, text="Prenom :")
lp.grid(row=1,column=0)


la = Label(f, text="Age :")
la.grid(row=2,column=0)

en = Entry(f)
en.grid(row=0, column=1, padx=10)
ep = Entry(f)
ep.grid(row=1, column=1, padx=10)
ea = Entry(f)
ea.grid(row=2, column=1, padx=10)


read = Button(f, text='Lecture', command=readValue)
read.grid(row=0, column=4)
quit = Button(f, text='Quitter', command=f.quit)
quit.grid(row=4, column=4)

f.title('Une fenetre en python')
f.geometry('400x300')

f.mainloop()

