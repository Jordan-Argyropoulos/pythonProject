import csv
import pandas
from pandas import DataFrame

# Dico {'Nom_Colonne':[values]}
dico = {'Article': [1, 2, 3, 4],
        'Intitulé': ['Tomate', 'Pâte', 'Fromage', 'Vin'],
        'Prix': [2.0, 3.0, 1.5, 15.0],
        'Inventaire': [3, 4, 2, 1]}


données = DataFrame(dico, columns=['Article', 'Intitulé', 'Prix', 'Inventaire'])
export_csv = données.to_csv('Names.csv', index=None, header=True, encoding='utf-8', sep=';')
print(données)

"""lire = pandas.read_csv("C:\\Users\\Jordan\\PycharmProjects\\pythonProject\\Names.csv")
print(lire)"""
