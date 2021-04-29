from math import *


class Cercles:
    def __init__(self, rayon):
        self.rayon = rayon

    def perimetre(self):
        return 2 * pi * self.rayon

    def surface(self):
        return pi * self.rayon ** 2


class Cylindres(Cercles):
    def __init__(self, rayon, hauteur):
        Cercles.__init__(self, rayon)
        self.hauteur = hauteur

    def volume(self):
        return self.surface() * self.hauteur


monCercle = Cercles(5)
print("Le périmètre du cercle est : ", monCercle.perimetre())
print("La surface de mon cercle : ", monCercle.surface())

cyl = Cylindres(5, 7)
print("La surface du cylindre est : ", cyl.surface())  # Surface cylindre
print("Le volume du cylindre est : ", cyl.volume())   # Volume cylindre
