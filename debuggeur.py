# coding: UTF-8
"""
Script: TP1/debuggeur.py
Création: barasc, le 19/08/2017
"""


# Imports

# Fonctions
def somme(var1, var2):
    """Calcule et renvoie la somme de var1 et var2"""
    res = var1 + var2
    return res


# Programme principal
def main():
    nb1 = 1
    nb2 = 2
    chaine = "ABC"
    car = "2"
    print("Valeurs initiales des variables:")
    print("nb1=", nb1)
    print("nb2=", nb2)
    print("chaine=", chaine)

    resultat = somme(nb1, nb2)
    print("nb1+nb2=", resultat)

    resultat = somme(chaine, car)
    print("chaine+nb1=", resultat)
    # Fin du programme principal


if __name__ == '__main__':
    main()
