"""
Tennis
Affichage du score au Tennis
E. Goffaux 09-06

#TODO: Ajouter la notion de match en 2 ou 3 sets gagnants ( ici c'est en 2 sets gagnants )
#TODO:  6,1 6,5  6-1 1-6 6-1   -> 6-1 6-4 7-5 (3sets) .. 6-1 2-6 2-6 6-3 6-4 ( 5 sets )

"""
import random

class Tennis:
    points ={  # Tennis.points
        0: '0',
        1: '15',
        2: '30',
        3: '40'
    }

    def __init__(self, j1, j2, nb_set=2):
        """
        Création des attributs pour conserver le score
        Initialisaton du score
        :return:
        """
        self.joueurs = [j1, j2]
        self.joueur = 0 #  joueur qui gagne le point ... le set ... le match

        self.cur_set = 0 # set courant
        self.point = [0, 0] # 0, 1, 2, 3 & 4
        self.jeux = []  # 0, 15, 30, 40
        if nb_set in (2,3):
            self.nb_set = nb_set
        else:
            self.nb_set = 2 # valeur par défaut
        # initialistion des compteurs de set suivant match en 2 ou 3 sets gagnants
        if self.nb_set == 2:
            self.set = [[0, 0, 0], [0, 0, 0]]
        else:
            self.set = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        self.result = [0,0]
        print(" Jeux {} contre {} en {} sets gagnants".format(self.joueurs[0], self.joueurs[1], self.nb_set))

    def affiche(self):
        """
        Affichage du score
        :return:
        """
        # calcul affichage

        if self.point == [3, 3]: #Deuce
            self.jeux =['40', '40']
        elif self.point == [4, 3]: #adv 1
            self.jeux = ['Adv', '']
        elif self.point == [3, 4]: #adv 2
            self.jeux = ['', 'Adv']
        else:
            self.jeux = [Tennis.points[self.point[0]], Tennis.points[self.point[1]]]
        msg = 'Affichage du score Roland Garos (sponsorisé par Peugeot & BMW)  {}\n'.format(self.joueurs[self.joueur])
        for i in range(2):
            msg += '\t{:>10} : {} \t{} \n'.format(self.joueurs[i], self.set[i], self.jeux[i])
        print(msg)
        pass

    def init(self, set_val, points):
        for i in range(2):
            for s in range(3):
                self.set[i][s] = set_val[s][i]
        self.point = points

    def add(self, j):
        """
        Ajoute 1 point au joueur j
        :param j: 0 ou 1 ou le nom du joueur
        :return:
        """
        # contrôle du joueur
        if j in (0, 1):
            joueur = j
        elif j not in self.joueurs:
            print('mauvais nom de joueur')
            return
        else:
            joueur = self.joueurs.index(j)
        # verifier si etat (adv1, adv2 )
        perdant = not joueur # le perdant n'est pas le gagnant ;-)
        if self.point[joueur] == 3 and (self.point == [4, 3] or self.point == [3, 4]):
            self.point[perdant] -= 1  # retour au Deuce (3,3) ( 0 -> not 0 = 1  1 ->not 1 = 0)
        else:
            self.point[joueur] += 1
        # test .. le point est gagné ... différence de 2 points et > 3
        self.joueur = joueur
        if self.point[joueur] > 3 and (self.point[joueur] - 1) > self.point[perdant]:
            # incrementer le set du joueur ...
            self.set[joueur][self.cur_set] += 1
            self.point = [0, 0]
            # verification gain du set
            if self.set[joueur][self.cur_set] > 5 and self.set[joueur][self.cur_set] - 1 > self.set[perdant][self.cur_set]:
                print('Set gagné par {}'.format(self.joueurs[joueur]))
                self.result[joueur] += 1  # joueue a gangé 1 set en +
                self.cur_set += 1
                if self.result[joueur] == self.nb_set: # si le joueur a gagné le nbr de set requis pour gagner le match
                    print('Match gagné par {}'.format(self.joueurs[joueur]))
                    return False
        return True

# test du module
if __name__ == '__main__':

    jeux = Tennis('Maxence', 'Antoine', 4)

    j = Tennis('Tony', 'Stéphane', 3)
    while j.add(random.randint(0, 1)):
        j.affiche()
    j.affiche()

    j = Tennis('Laure', 'Jordan', 2)
    while j.add(random.randint(0, 1)):
        j.affiche()
    j.affiche()



