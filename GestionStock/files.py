#
#   Lecture - ecriture CSV
#
#   emmanuel_goffaux@hotmail.com
#

import os
import csv
import logging


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class Rec:
    # Class Rec : lecture d'un csv, init d'un dico, Add, Ret, Mod, Del
    def __init__(self, fichier, champs):
        self.fichier = fichier
        self.champs = champs
        self.rec = {}
        if not os.path.exists(self.fichier):
            print('Création fichier {} {}'.format(self.fichier, self.champs))
            self._save()
        else:
            print('Lecture fichier {} {}'.format(self.fichier, self.champs))
            self._read()

    def __del__(self):
        print('Fichier {} sauvé...{} '.format(self.fichier, len(self.rec)))


    def __setitem__(self, key, rec):  #  fArticles[12] = ... fArticles.__setItem__(12)=article
        if key not in self.rec:
            self.rec[key] = rec
            self._save() # ecriture des données
        else:
            print('Clé {} déjà existante'.format(key))
    def __delitem__(self, key):   # del rec[12]
        if key in self.rec:
            del self.rec[key]
            self._save()  #ecriture des données
        else:
            print('Clé {} inexistante'.format(key))

    def __getitem__(self, key):  #   art = rec[12:14]
        if key in self.rec:
            rec = self.rec[key]
        else:
            rec = {}
            print('Clé {} inexistante'.format(key))
        return rec

    def __repr__(self):
        return self.rec.__repr__()

    def __str__(self):
        return self.rec.__str__()

    def __contains__(self, key):
        print('key:',key)
        print('in:', self.rec)
        return key in self.rec


    def _save(self):
        """sauve le dictionnaire en csv (entête noms des champs, ensuite les données  )"""
        print('fichier à sauver : {}'.format(self.fichier))
        with open(self.fichier, mode='w', newline='') as file:
            csvFile = csv.writer(file)
            csvFile.writerow(self.champs)
            print(self.rec)
            for k in self.rec:
                print(k, self.rec[k])
                csvFile.writerow(self.rec[k])
        print('fichier sauvé ...')

    def _read(self):
        """ lecture du fichier et initialisation du dictionnaire"""
        with open(self.fichier, mode='r') as file:
            csvFile = csv.reader(file)
            entete = next(csvFile)   # lecture du format d'entete
            for line in csvFile:      # lecture des autres enregistrements
                k = int(line[0])
                if k not in self.rec:
                    #self.rec[k] = dict(zip(self.champs, line))
                    self.rec[k] = line
                    print('Lecture : ', self.rec[k])
                else:
                    print('Key {} existe dans {}'.format(k, self.fichier))

    def __iter__(self):
        self.l = len(self.rec)
        self.i = -1
        return self

    def __next__(self):
        rec_tmp = [r for k, r in self.rec.items()]
        if self.i < self.l-1:
            self.i += 1
            print(rec_tmp[self.i])
            return(rec_tmp[self.i])
        else:
            raise StopIteration()

# test du module
if __name__ == '__main__':

    art1 = {'id':12,'nom':'Ecran','prix':120,'qty':'45'}
    art2 = {'id':13,'nom':'Clavier','prix':30,'qty':'45'}
    art3 = {'id':14,'nom':'Ecran','prix':120,'qty':'45'}
    art4 = {'id':15,'nom':'Clavier','prix':35,'qty':'35'}

    articles = {art1['id']: art1, art2['id']: art2, art3['id']: art3, art4['id']: art4,art4['id']: art4 }

    # print(articles)
    artStruct = ['id', 'nom', 'ecran', 'prix', 'qty']
    artStruct = art1.keys()
    artValue = art1.values()
    fArticles = Rec('articles.csv', artStruct)

    for key, article in articles.items():
        # ajout d'un record
        rec = [r for r in article.values()]
        fArticles[rec[0]] = rec


    #supression d'un article
    wait = input('Avant supression du 15 ')
    del fArticles[15]  # __getitem()
    wait = input('Apres supression du 15 ')
    del fArticles[20]  # __getitem()
    if 15 in fArticles:
        print ('15 repris')
    else:
        print('15 exclus')
    # Appel __set__
    fArticles[12] = article
    print('12 ème article:',fArticles[12])
    print( 'Article 12 : ', article)
    # __get__
    article = fArticles[20]
    print( 'Article 20 : ', article)

    for rec in fArticles:
        print(rec)


    #  Création du fichier des receptions
    receptionStruct = ['id','date','article','qty']
    reception = Rec('receptions.csv', receptionStruct)
    recepData = [[1, '15-04-2021','12', 24],
                [2,'15-04-2021','13',15],
                [3, '15-04-2021', '15', 12],
                ]
    for recept in recepData:
        reception[recept[0]] = recept
    print(artStruct, artValue)
    # création du fichier des expéditions
    expeStruct = ['id','date','article','qty']
    expeData = [[1, '15-04-2021','12', 14],
                [2,'15-04-2021','13',5],
                [3, '15-04-2021', '15', 10],
                ]
    expedition = Rec('expedition.csv', expeStruct)
    for exp in expeData:
        expedition[exp[0]] = exp


