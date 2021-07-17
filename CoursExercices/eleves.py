"""
    Exercices d'applictation des classes
    - Créer une classe Humain
        Attributs
        - nom, prenom
        - date de naissance
        - genre, titre
        - adresse ( rue, numéro, localité, code postal )
        - gsm
        Methodes
        - methode qui affiche la 'objet ( __rep__  __str__ )
        - methode changer adresse
        - methode retourne l'âge

    - Créer une classe Eleve
        hérite de humain
        Attributs :
            cours
                dictionnaire ( nom du cours, note de l'examen )
        Methodes :
        - AJouter des cours / résultats
        - calcul les résulats
            __str__()
            Jules a 80% ( en moyenne )

    - Créer une classe Classe
        Attributs
        - nom, local
        - Liste des éleves
        Methodes
        - ajouter des éléves
        - afficher les résultas d'une classe par cours
            parcourir les élévec et rerprned la moyenne pour un cours ..
"""

class Humain:
    def __init__(self, lname, fname, birth, title, street, num, city, codep, gsm):
        self.lastname = lname
        self.firstname = fname
        self.birthdate = birth
        self.genre = title
        self.
class Eleve(Humain):
    def