# list
"""
joursL = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
joursL[0] = 'Monday'
for jour in joursL:
    print(jour)

# tuple
joursT = ('Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi')
for jour in joursT:
    print(jour)

# dict
dico = {}
dico['nom'] = 'EINSTEIN'
dico['prenom'] = 'Albert'
dico['Annee'] = 1879

for cle in dico:
    print(cle, ' : ', dico[cle])

del dico['Annee']

for cle in dico:
    print(cle, ' : ', dico[cle])

#range

for i in range(5):
    print(i, end="  ")

l = range(5)
print( l )


#affiche msg

msg = 'Bonjour Python'

for lettre in msg:
    print (lettre, end='.')
"""

# class

class Tableau:

    def __init__(self):
        self.tab = []

    def inserer(self, elm):
        self.tab.append(elm)

    def __iter__(self):
        self.n = len(self.tab)
        self.i = -1
        return self

    def __next__(self):
        if self.i < self.n - 1:
            self.i += 1
            return self.tab[self.i]
        raise StopIteration

    def __setitem__(self, key, value):
        self.tab[key] = value

    def __getitem__(self, item):
        return self.tab[key]

    def __getitem__(self):

s = set()
s.append(1)
s.append(1)
s.append(2)
s.append('Abc')
s.append('abc')
for e in s:
    print(s)

tab = Tableau()
tab.inserer(1)
tab.inserer(1)
tab.inserer(1)
tab.inserer(3.14159)
tab.inserer('bonjour')
tab.inserer(4)
tab.inserer(5)

t = tab[2]
print( t )
tab[4] = 12

for elm in tab:
    print(elm)