# Données labélisées et la donnée à classer
from math import sqrt

positions_classes = [[1, 1, "r"], [1.5, 1.5, "t"], [3, 3, "r"], [4, 4, "t"], [5, 5, "t"], [6, 6, "r"], [7, 7, "r"], [8, 8, "t"], [10, 10, "r"]]

x = 2
y = 2

def distance(x1 : float, x2 : float, y1 : float, y2 : float) -> float :
    '''Calcule la valeur absolue de la distance en 2 dimensions'''

    return abs(sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2))

distances = []

for element in positions_classes:
    print(element)
    distances.append([distance(element[0], x, element[1], y), element[2]])

distances.sort()

k = 3

def determiner_classe(distances_classes : list, y : int) -> str:
    nombre_t = 0
    nombre_r = 0
    for i in range(y):
        if distances[i][1] == "t":
            nombre_t = nombre_t + 1
        else :
            nombre_r = nombre_r + 1
    if nombre_t < nombre_r:
        return "L'élement est un rectangle"
    else:
        if nombre_t == nombre_r:
            return "Il n'y a pas de solution."
        else:
             return "L'élement est un triangle"


print(determiner_classe(distances, k))



