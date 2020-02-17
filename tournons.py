# coding: UTF-8
"""
Script: Prog2/tournons
"""


# Imports
import math
import matplotlib.pyplot

# Fonctions
def get_angles():
    i = 0
    angle = [-1000.0]
    while angle[i] < 1000:
        i += 1
        angle.append(0.5 + angle[i - 1])
    return angle


def degree_vers_radian(degree):
    return degree * math.pi / 180


def calcul_sinus_cardinal(angles):
    convert = []
    for angle in angles:
        angler = degree_vers_radian(angle)
        if angler != 0:
            calcul = math.sin(angler) / angler
        else:
            calcul = 1
        convert.append(calcul)
    return convert


# Programme principal
def main():
    liste_angles = get_angles()  # Récupère la liste d'angles
    liste_sinc = calcul_sinus_cardinal(liste_angles)  # Calcule le sinus des angles

    # Affichage
    matplotlib.pyplot.figure()  # Crée une nouvelle figure pyplot
    matplotlib.pyplot.plot(liste_angles, liste_sinc, 'b-')  # Trace la liste_sinc en fonction de la liste_angles en bleu
    matplotlib.pyplot.xlabel('angle (en degré)')  # Définit la légende de l'axe des abscisses
    matplotlib.pyplot.ylabel('sinc(angle)')  # Définit la légende de l'axe des ordonnées
    matplotlib.pyplot.legend(['sinc(x)'])  # Définit la légende des courbes
    matplotlib.pyplot.grid(True)  # Ajoute une grille
    matplotlib.pyplot.show()  # Affiche les tracés


if __name__ == '__main__':
    main()
# Fin
