import csv
import pandas
from pandas import DataFrame


#####
# Fonctions
#####

def add_inventory():
    addobj = int(input("Veuillez saisir le nombre d'articles : "))

    for i in range(addobj):
        noartname = pandas.DataFrame(index=['Article '])    #index
        noartnum = input("n° d'article :")                  #input index
        noart = noartname + noartnum                        #concaténation index
        inti = input("Nom de l'article :")
        pri = input("Prix de l'article :")
        sto = input("Nombre d'article :")
        dicti = noart + inti + pri + sto
        dfObj = pandas.DataFrame(dicti, columns={'Intitule', 'Prix', 'Inventaire'})
        export_csv = dfObj.to_csv('Names.csv', index=True, header=True, encoding='utf-8', sep=';')
        print(dfObj)

        # export_csv = dfObj.to_csv('Names.csv', index=True, header=True, encoding='utf-8', sep=';')


def add_article():
    #append row to the dataframe
    df_marks = df_marks.append(new_row, ignore_index=True)

    print('\n\nNew row added to DataFrame\n--------------------------')
    print(df_marks)

# def delete_article():

"""n = 0
while True:
    n = input("Pour ajouter : 1, pour modifier : 2")
    if n == 1:
    add_article()"""

add_inventory()

# List of Tuples
# articles = {('Pate', 4, 2),
#            ('Tomate', 3, 2),
#            ('Fromage', 2.5, 1),
#            ('Vin', 15.0, 1)}
# Create a DataFrame object
# dfObj = pandas.DataFrame(articles, columns={'Intitule', 'Prix', 'Inventaire'},
#                         index={'Article 1', 'Article 2', 'Article 3', 'Article 4'})
# export_csv = dfObj.to_csv('Names.csv', index=True, header=True, encoding='utf-8', sep=';')
# print(dfObj)
