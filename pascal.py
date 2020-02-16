# coding: UTF-8
"""
Script: Prog1/pascal
Création: valen, le 21/11/2019
"""

# Imports
from math import factorial, floor


# Fonctions
def triangle(N):
    for i in range(N + 1):
        for j in range(i + 1):
            print(j, end="\t")
        print()


def triangle_inverse(N):
    for i in range(N, -1, -1):
        for j in range(i + 1):
            print(j, end="\t")
        print()


def triangle_pascal(N):
    for i in range(N, -1, -1):
        for P in range(i + 1):
            print(floor((factorial(N) / (factorial(P) * factorial(N - P)))), end="\t")
        N -= 1
        print()


# Programme principal
def main():
    N = int(input("Entrez un Nombres N et je vous donnerais le triangle pascal, l'inverse et son Coefficient Binômial :"))
    print("| Triangle Pascal |\n")
    triangle(N)
    print("\n| Triangle Pascal Inverse |\n")
    triangle_inverse(N)
    print("\n| Triangle Pascal : Coefficient Binômial |\n")
    triangle_pascal(N)


if __name__ == '__main__':
    main()
# Fin
