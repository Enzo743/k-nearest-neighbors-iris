# Algorithme k plus proches voisins pour des espèces d'iris
import pandas
import matplotlib.pyplot as plt
from math import sqrt

iris = pandas.read_csv("iris.csv")
length = iris.loc[:, "petal_length"]
width = iris.loc[:, "petal_width"]
lab = iris.loc[:, "species"]
full_list = []
distances = []

search_length = float(input("Quelle est la longueur de la pétalle ?"))
search_width = float(input("Quelle est la largeur de la pétalle ?"))
k = 3

def distance(x1 : float, x2 : float, y1 : float, y2 : float) -> float :
    """Calcule la valeur absolue de la distance en 2 dimensions"""
    return abs(sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2))

def determine_iris(lists : list, y : int) -> str:
    number_0 = 0
    number_1 = 0
    number_2 = 0
    text_x = 0.9
    text_y = 1.75

    for i in range(y):
        if distances[i][1] == 0:
            number_0 += 1
        elif distances[i][1] == 1:
            number_1 += 1
        elif distances[i][1] == 2:
            number_2 += 1

    if number_0 < number_1 and number_2 < number_1:
        return plt.text(text_x, text_y, "L'iris est de l'espèce Virginica", fontsize=10)
    elif number_0 < number_2 and number_1 < number_2:
        return plt.text(text_x, text_y, "L'iris est de l'espèce Versicolor", fontsize=10)
    elif number_1 < number_0 and number_2 < number_0:
        return plt.text(text_x, text_y, "L'iris est de l'espèce Setosa", fontsize=10)
    elif number_0 == number_1 == number_2:
        return plt.text(text_x, text_y, "Il n'y a pas de solution pour ce nombre de plus proche voisins", fontsize=10)

def graphical():
    plt.scatter(length[lab == 0], width[lab == 0], color="g", label="setosa")
    plt.scatter(length[lab == 1], width[lab == 1], color="r", label="virginica")
    plt.scatter(length[lab == 2], width[lab == 2], color="b", label="versicolor")
    plt.scatter(search_length, search_width, color="black")
    determine_iris(distances, k)
    plt.legend()
    plt.show()

for element in range(len(iris)):
    full_list.append([length[element], width[element], lab[element]])

for element in full_list:
    distances.append([distance(element[0], search_length, element[1], search_width), element[2]])

distances.sort()
graphical()
