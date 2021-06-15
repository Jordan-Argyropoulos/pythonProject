from random import random


class Robot:
    """ Robot qui sait avancer d'une case et pivoter à droite de 90°.
 Il est repéré par son abscisse x, son ordonnée y et sa direction.
 """
    # des attributs de classe
    _directions = ('nord', 'est', 'sud', 'ouest')  # direction en clair
    _dx = (0, 1, 0, -1)  # incrément sur X en fonction de la direction
    _dy = (1, 0, -1, 0)  # incrément sur Y en fonction de la direction



    def __init__(self, x, y, direction):
        """ Initialiser le robot self à partir de sa position (x, y) et sa direction. """
        self.x = x
        self.y = y
        self.direction = Robot._directions.index(direction)
        self.nom = "à déterminer"
        self.type()

    def avancer(self):
        """ Avancer d'une case dans la direction. """
        self.x += Robot._dx[self.direction]
        self.y += Robot._dy[self.direction]

    def reculer(self):
        """ Reculer d'une case"""
        self.x -= Robot._dx[self.direction]
        self.y -= Robot._dy[self.direction]

    def pivoter(self):
        """ Pivoter ce robot de 90° vers la droite. """
        self.direction = (self.direction + 1) % 4

    def afficher(self, *, prefix=''):
        print(prefix, self, sep='')

    def type(self):
        """Getter type robot"""
        return self._type

    def statut(self, stat):
        """Setter statut robot"""
        self._statut = stat

    def orientation(self, ori):
        """Setter orientation robot"""
        self._orientation = ori

    def __str__(self):
        return '({}, {})>{}'.format(self.x, self.y, Robot._directions[self.direction])

rob1 = Robot
rob1.statut("En service")
"""type mobiles, industriels, humanoides"""