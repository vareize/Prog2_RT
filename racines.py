# coding: UTF-8
"""
Script: Prog1/racine
"""

# Imports
import math

# Fonctions
def Delta(a, b, c):
    res = (b*b)-(4*a*c)  # calcul du delta du polynome
    return res

def PremierDegre(b, c):
    res = c/b
    return res

def calcule_racines(a, b, c):
    if a == 0 and b == 0:
        res = None
    elif a == 0:
        res = -c/b
    elif Delta(a, b, c) > 0:
        delta = Delta(a, b, c)  # recupere le delta a partir de a, b, c
        raciest = (math.sqrt(delta))  # calcul de la racine de delta
        x_1 = (-b+raciest)/(2*a)  # racine polynomiale 1 si delta > 0
        x_2 = (-b-raciest)/(2*a)  # racine polynomiale 2 si delta > 0
        res = [x_1, x_2]
    elif Delta(a, b, c) == 0:
        res = (-b/(2*a))
    else:
        res = None
    return res

# Programme principal
def main():
    print(calcule_racines(4, 10, 3))  # resultat

if __name__ == '__main__':
    main()
# Fin
