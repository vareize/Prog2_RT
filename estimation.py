# coding: UTF-8
"""
Script: Prog1/estimation
Création: valen, le 22/11/2019
"""


# Imports
from math import sqrt, pi
from random import random
import turtle

# Fonctions
def riemann(n):
    S = []
    for i in range(1, n+1):
        valeur_n = (1/i**2)
        S.append(valeur_n)
    return sqrt(6*sum(S))

def calcul_erreur_relative(valeur):
    val = valeur
    erreur = round(abs((val - pi)/pi*100), 3)
    return erreur

def convergence_riemann():
    n = 10
    for i in range(1):
        while n < 1000001:
            print("estimation pour n=" + str(n) + " : " + str(riemann(n)) + " (" +
                  str(calcul_erreur_relative(riemann(n)))+"% d'erreur)")
            n *= 10

def est_dans_cercle(x, y):
    distance_centre_point = sqrt(x**2+y**2)
    if 0 <= distance_centre_point <= 1:
        return True
    else:
        return False

def monte_carlo(n):
    T = True
    C = 0
    for i in range(n):
        x = random()
        y = random()
        if est_dans_cercle(x, y) == T:
            C += 1
    return 4*C/n

def convergence_monte_carlo():
    n = 10
    for i in range(1):
        while n < 1000001:
            print("estimation pour n=" + str(n) + " : " + str(monte_carlo(n)) + " (" + str(calcul_erreur_relative(
                monte_carlo(n)))+"% d'erreur)")
            n *= 10


# Programme principal
def main():
    print("| Serie de riemann pour (pi) avec le pourcentage d'erreur |\n")
    convergence_riemann()
    print("\n\n| Méthode de Monte-Carlo pour (pi) avec le pourcentage d'erreur|\n")
    convergence_monte_carlo()
    print("\n| La convergence de riemann est plus precise que celle de monte-carlo |")



if __name__ == '__main__':
    main()
# Fin