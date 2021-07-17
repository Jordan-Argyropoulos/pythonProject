from tkinter import *

#Exercice 1 : fenetre @@@@@@@@@@@@@@@@@@
"""fenetre = Tk()

etiquette = Label(fenetre, text="Bonjour fan de Python !")
etiquette.pack()

fenetre.mainloop()
print('Fin de partie')"""

#Exercice 2 : fenetre + bouton @@@@@@@@@@@@@@@@@@

"""def action():
    print("Yes, we can !")

f = Tk()

l = Label(f, text="Label : Bonjour le monde !")

b = Button(f, text="Click here !", command=action)

b.pack()
l.pack()

f.mainloop()

print("Fin de partie s'affiche à la fermeture")"""

#Exercice 3

def action():
    print("Yes, we can !")

f = Tk()

l = Label(f, text="Label : Bonjour le monde !")
l['bg'] = 'black'
l['fg'] = 'yellow'
b = Button(f, text="Click here !", command=action)
b['fg'] = 'red'
quit = Button(f, text="Bouton : Quitter", command=f.destroy)
quit['fg'] = 'blue'
b.pack()
l.pack()
quit.pack()
f.title('Une fenetre en python')
f.geometry('800x800')

f.mainloop()

print("Fin de partie s'affiche à la fermeture")
