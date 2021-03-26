import csv
import pandas
from pandas import DataFrame
#####
"""
# Dico {'Nom_Colonne':[values]} Valeur brute
dico = {'Article': [1, 2, 3, 4],
        'Intitulé': ['Tomate', 'Pâte', 'Fromage', 'Vin'],
        'Prix': [2.0, 3.0, 1.5, 15.0],
        'Inventaire': [3, 4, 2, 1]}

a = {'Article': [],
     'Intitulé': [],
     'Prix': [],
     'Inventaire': []}
n = int(input("Entrer le nombre d'article à rajouté: "))
for i in range(n):
    art_input = input("Numéro d'article: ")
    int_input = input("Intitulé de l'article: ")
    prix_input = input("Prix de l'article: ")
    inv_input = input("Nombre d'article: ")
    a.loc[i] = [art_input, int_input, prix_input, inv_input]
    with open('Names.csv', 'a') as fd:
        fd.write([a])
"""

# Valeur Brute
"""données = DataFrame(dico, columns=['Article', 'Intitulé', 'Prix', 'Inventaire'])
export_csv = données.to_csv('Names.csv', index=None, header=True, encoding='utf-8', sep=';')
print(données)"""

"""lire = pandas.read_csv("C:\\Users\\Jordan\\PycharmProjects\\pythonProject\\Names.csv")
print(lire)"""

# List of Tuples
articles = [('Pate', 4, 2),
            ('Tomate', 3, 2),
            ('Fromage', 2.5, 1),
            ('Vin', 15.0, 1)]
# Create a DataFrame object
dfObj = pandas.DataFrame(articles, columns=['Intitule', 'Prix', 'Inventaire'],
                         index=['Article 1', 'Article 2', 'Article 3', 'Article 4'])
export_csv = dfObj.to_csv('Names.csv', index=True, header=True, encoding='utf-8', sep=';')
print(dfObj)
# Read file csv
lire = pandas.read_csv("C:\\Users\\Jordan\\PycharmProjects\\pythonProject\\Names.csv")
print(lire)