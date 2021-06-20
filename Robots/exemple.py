import msvcrt as m
import os

ligne, colonne = (7, 7)
mat = [["*" for i in range(colonne)] for j in range(ligne)]


def affichage(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end=' ')
        print()


x = 3
y = 3
mat[x][y] = "X"
affichage(mat)
print("appuyer sur une touche pour démarrer")
print("\n")

char = m.getch()
c = char.decode("ascii")
while c != "x":
    if c == "q":
        if y > 0:
            mat[x][y] = "*"
            y -= 1
            mat[x][y] = "X"
    elif c == "d":
        if y < 6:
            mat[x][y] = "*"
            y += 1
            mat[x][y] = "X"
    elif c == "s":
        if x < 6:
            mat[x][y] = "*"
            x += 1
            mat[x][y] = "X"
    elif c == "z":
        if x > 0:
            mat[x][y] = "*"
            x -= 1
            mat[x][y] = "X"
    os.system('cls')
    affichage(mat)
    char = m.getwch()