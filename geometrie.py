# coding: UTF-8
"""
Script: Python/geometrie
"""


# Imports

# Fonctions
def carre(nb):
    print("+" + "-"*(nb-2) + "+")
    for i in range(1, nb-1):
        print("|" + " "*(nb-2) + "|")
    print("+" + "-"*(nb-2) + "+")

    return None

def triangle(nb):
    a = 1
    for i in range(nb):
        print("*"*a)
        a += 1

    return None

def losange(nb):
    #  Partie haute du triangle
    x = 1
    a = nb - x
    b = 0
    for i in range(nb):
        print(" "*a + "/" + " "*b + "\\")
        x += 1
        a = nb - x
        b += 2
    #  Partie basse du triangle
    for i in range(nb):
        x -= 1
        a = nb - x
        b -= 2
        print(" " * a + "\\" + " " * b + "/")

    return None

def croix(x, y, taille):
    tronc = (" " * (x - 1) + "|" + " " * (taille - x))
    barre = ("-" * (x - 1) + "+" + "-" * (taille - x))
    for i in range(taille):
        if i == (y-1):
            print(barre)
        else:
            print(tronc)

    return None


# Programme principal
def main():
    print("\n" + "-----Carre-----" + "\n")
    carre()
    print("\n" + "-----Triangle-----" + "\n")
    triangle()
    print("\n" + "-----Losange-----" + "\n")
    losange()
    print("\n" + "-----Croix-----" + "\n")
    croix()


if __name__ == '__main__':
    main()
# Fin
