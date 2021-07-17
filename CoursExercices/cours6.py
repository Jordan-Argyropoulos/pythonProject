"""
les fichiers
"""

# écriture - lecture fichier texte

# f = open('clients.txt', 'w') # création clients.txt, recherche clients.txt pour voir ou il se trouve dans les dossiers
# f.write('Hello world')
# f.close()
#
# f = open('clients.txt', 'r')
# msg = f.read()
# print(msg)
# f.close()

# f = open('clients.txt', 'w') # création clients.txt, recherche clients.txt pour voir ou il se trouve dans les dossiers
# for i in range(10):
# f.write('Hello world')
# f.close()
#
# f = open('clients.txt', 'r')
# msg = ' '
# while msg :
# msg = f.readlines()
# print(msg)
# f.close()
#
# for m in msg:
# print(m)

'''
path = "C:/Users/Jean-Julien/Desktop/JJ/Cours/Programmation orienté objet/" # ne prend pas avec \ mais le / ou alors mettre \\ (doublé le \)
file = "mateux.csv"

fileName = path + file

f = open(fileName, 'r')

fichier = csv.reader(f)
for line in fichier: # permet d'afficher les lignes du fichier csv creer avec excel
print(line)

print(fileName)
'''
def afficher{

}

class Menu:

    def __init__(self):
        self.menu = {}
    def add(self, num, txt, func):
        self.menu[num] = (txt, func)
    def run(self):

        c = '1'
        while c != 'q':
            for c, l in menu.items():
                txt = l[0]
                print('{} - {}'.format(c, txt))
            c = input('Votre choix: ')
            if c in self.menu:
                print('Votre choix: {}'.format(self.menu[c][0]))
                self.menu[c][1]()

menu = Menu()

menu.add('1', 'Afficher,')