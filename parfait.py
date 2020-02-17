# coding: UTF-8
"""
Script: Prog2/parfait
Création: arroyoe, le 04/02/2020
"""


# Imports

# Fonctions
def diviseurs(n):
    i = 0
    diviseurs = []
    while (i < n):
        i += 1
        if n % i == 0:
            diviseurs.append(i)
    return diviseurs


def est_parfait(n):
    return True if sum(diviseurs(n)) == 2 * n else False


def calcul_liste_entiers_parfaits(N):
    n = 0
    liste = []
    while (n < N):
        n += 1
        if (est_parfait(n)):
            liste.append(n)
    return liste


# Programme principal
def main():
    print(calcul_liste_entiers_parfaits(45))


if __name__ == '__main__':
    main()
# Fin