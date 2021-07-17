#
#       Utililisation matplotlib
#
#       E. Goffaux
#
""""
up() : lève le crayon
down() : baisse le crayon
forward(n) : avance de n
left(d) : tourne vers la gauche de d degrés
right(d) : tourne vers la droite de d degrés
goto(x,y) : se déplace vers le point de coordonnées (x,y)
circle(r) : dessine un cercle de rayon r
width(e) : définit l’épaisseur du trait
speed(’’texte’’) : définit la vitesse de la tortue
write(’’texte’’) : écrit le texte
color(’’couleur’’) : définit la couleur du trait
bgcolor(’’couleur’’) : définit la couleur de fond
reset() : efface tout
done() : arrête le dessi


"""


import turtle  as t

t.setup(800, 600)
t.speed( 10 )
t.width(2)
t.shape('turtle')
t.color ("green")
def carre(taille=50):
    for i in range(4):
        t.forward(taille)
        t.right(90)

def triangle(taille=50):
    for i in range(3):
        t.forward(taille)
        t.right(120)

def deplace(distance, angle):
    t.right(angle)
    t.up()
    t.forward(distance)
    t.down()

def pointille(distance, tiret, angle):
    for i in range(int(distance/(2*tiret))):
        t.forward(tiret)
        deplace(tiret, 0)

def fractale(l):
    t.forward(l/3)
    t.right(60)
    t.forward(l/3)
    t.left(60)
    t.forward(l/3)
    t.right(60)
    t.forward(l / 3)

fractale(100)

carre(100)
deplace(100, 0)
carre()
deplace(150, -90)
triangle(150)

deplace( 100, 30)

t.circle(20, 270)
pointille( 300, 30, 90 )
t.mainloop()





