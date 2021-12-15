#
#   Machine Learning
#   E. Goffaux 08-05-2021
#
#

import os
import pandas_test as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pandas_test.plotting import scatter_matrix
from sklearn.preprocessing import OrdinalEncoder

class Immo():
    """
    Class Immo, prédiction valeur immobilière
    """
    def __init__(self, f):
        self.df = pd.read_csv(f, delimiter=';')
        self.param = []
        self. target = []
        self.train = []
        self.test = []
        col = list(self.df.head())
        print('Colonnes:', col)
        # y = f( x )

        print( self.df )
        # qq functions sur les dataframes

        type =[]
        type = [t for t in self.df['type'] if t not in type]
        type = self.df['type'].unique()
        print('Type de bien\n', type)
        self.model = LinearRegression()

    def cleansing(self):
        """
        Nettoyage et transformation des données
        :return:
        """
        # transformer des variables discretes en numérique ( villa -> 1, maison -> 0 )
        ord_enc = OrdinalEncoder()
        self.df.insert(1, 'type_num', ord_enc.fit_transform(self.df[["type"]]))
        self.df[["type", "type_num"]].head(11)

        # nom des colonnes paramètres du modèles
        self.param = self.df.columns[1:-2]
        print(self.param)
        # nom de la colonne cible .. résultat du modèle
        self.target = self.df.columns[-1]

        # partager les données entr etrain et test
        self.train, self.test = train_test_split(self.df, test_size=0.2)

    def observe(self):
        """
        Affichage synthétique des données
        :return:
        """

        self.df.info()
        print(self.df.head())   # première ligne
        print(self.df.tail())   # dernière ligne
        print(self.df.describe())   # analyse du data frame
        print(self.df)

        figure = plt.figure()
        ax = figure.add_subplot(1, 2, 1, projection='3d')
        ax.scatter(self.df["surface"], self.df["chambres"], self.df["prix"], c='r', marker='^')
        ax.set_xlabel('surface')
        ax.set_ylabel('chambres')
        ax.set_zlabel('prix')
        plt.show()

        self.df.hist()
        scatter_matrix(self.df)
        plt.show()



    def learn(self):
        """
        Méthode d'apprentissage du modèle
        :return:
        """
        # target = f ( param )  objectif estimer 'f'
        print(self.train[self.param])
        print(self.train[self.target])
        self.model.fit(self.train[self.param], self.train[self.target])
        print('Train data\n', self.train)
        print('Test data\n', self.test)

    def evaluate(self):
        """
        Evaluation du modèle, comparaison entre résultats attendus et données de test
        :return:
        """
        print("Modele", self.model)

        pred = self.model.predict(self.test[self.param])
        print( pred )
        df_test = pd.DataFrame(self.test)
        df_test['estimation'] = pred
        print(df_test)
        estimation = math.sqrt(mean_squared_error(pred, self.test[self.target]))
        print( 'Estimation des moindres carrés : ', estimation)

        return True if estimation < 15 else False

    def predict(self, f):
        """
        Prédiction d'une estimation de valeur
        :param f:
        :return:
        """
        #  adapter la méthode pour utiliser le type_num comme 'cleansing'
        dfp = pd.read_csv(f, delimiter=';')
        col = list(dfp.head())
        ord_enc = OrdinalEncoder()
        dfp.insert(1, 'type_num', ord_enc.fit_transform(dfp[["type"]]))
        print('Colonnes:', col)
        print(dfp)
        param = dfp.columns[1:-2]
        target = dfp.columns[-1]
        print('Prédiction - estimation d\'une valeur immobilière')
        print(param)
        print(target)
        estimation = self.model.predict(dfp[param])
        dfp['estimation'] = estimation
        dfp['diff'] = (dfp['estimation'] - dfp['prix']) / dfp['prix']*100

        print(dfp)



if __name__ == '__main__':

    file = 'immeubles.csv'
    immo = Immo(file)

    # Nettoyage et transformation du dataframe
    immo.cleansing()

    # Observation des données
    immo.observe()

    # Apprentissage
    immo.learn()

    # Evaluation du modèle
    if immo.evaluate():
        print('Le modèle fit avec les prédictions')
    else:
        print('Améliorer le modèle avec des données + précises')

    # Utilisation
    immo.predict('estimation.csv')



