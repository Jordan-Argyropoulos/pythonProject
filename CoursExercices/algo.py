# Pogramme Python pour calculer l'inverse d'une matrice
# en utilisant numpy
# Importer le package requis
import numpy as np

# On prend une matrice 4*4
from numpy import ndarray

A: ndarray = np.array ([[4, 1, 1, 3],
               [4, -2, 6, 1],
               [2, 8, 7, 6],
               [3, 1, 9, 7]])

#A = np.array([[[1, 3], [4, 1]],
#             [[2, 1], [5, 2]],
#             [[4, 2], [1, 2]]])

# On calcule l'inverse de la matrice
print(np.linalg.inv(A))

