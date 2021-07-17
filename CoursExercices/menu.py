
class Menu:
    """ Classe Menu"""
    def __init__(self):
        self.menu = {}
    def add(self, num, txt, func):
        self.menu[num] = (txt, func)
    def run(self):
        """ Affichage et execution du menu """
        c = '1'
        while c != 'q':
            # Affichage du menu
            for c, l in self.menu.items():
                print('{} - {}'.format(c, l[0]))
            # demander le choix
            c = input('Votre choix:')
            if c in self.menu:  # test appartenance
                print('votre choix : {}'.format(self.menu[c][0]))
                self.menu[c][1]()  # execution de la fonction associée au choix du dictionnaire


