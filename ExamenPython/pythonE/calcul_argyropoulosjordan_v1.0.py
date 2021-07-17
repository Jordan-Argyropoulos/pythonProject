"""
Nom: Argyropoulos Prénom: Jordan
Adresse: argyropoulosjordan@gmail.com

Cours: Programmation Orienté Objet
Année scolaire: 2020-2021
Ecole: IETC - Condorcet Charleroi - Promotion social

"""

val_e = "Valeur de E pour "
e4 = "2,7182"
e8 = "2,71828182"
e15 = "2,718281828459045"


def _facto_recur(nbr):
    """Factorielle d'un nombre avec récursivité"""
    if nbr == 0 or nbr == 1:
        return 1
    return nbr * _facto_recur(nbr - 1)


def euler(n):
    """Fonction Euler"""
    euler_nbr = 0
    for i in range(n):
        euler_nbr += 1 / _facto_recur(i)
    return euler_nbr


def affichage():
    print(f"{val_e}2 itérations : {euler(2):1.4f} comparatif avec E à 4 décilames = {e4}")
    print(f"{val_e}4 itérations : {euler(4):1.4f} comparatif avec E à 4 décilames = {e4}")
    print(f"{val_e}6 itérations : {euler(6):1.4f} comparatif avec E à 4 décilames = {e4}")
    print(f"{val_e}8 itérations : {euler(8):1.8f} comparatif avec E à 8 décilames = {e8}")
    print(f"{val_e}10 itérations : {euler(10):1.8f} comparatif avec E à 8 décimales = {e8}")
    print(f"{val_e}12 itérations : {euler(12)} comparatif avec E à 15 décimales = {e15}")
    print(f"{val_e}14 itérations : {euler(14):1.15f} comparatif avec E à 15 décimales = {e15}")
    print(f"{val_e}17 itérations : {euler(17)} comparatif avec E à 15 décimales = {e15}")


if __name__ == "__main__":

    affichage()
