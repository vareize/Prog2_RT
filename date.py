# coding: UTF-8
"""
Script: Prog1/estimation
"""

# Imports
import calendar
from random import *

# Fonctions
def est_valide(jour, mois, annee):
    if 0 < jour < 31 and 0 < mois < 12 and annee > 1552:
        if mois > 13 or mois < 0:
            if mois in (1, 3, 5, 7, 8, 10, 12):
                if jour > 31:
                    return False
                else:
                    return True
            elif mois == 2:
                if annee % 4 == 0:
                    if jour > 30:
                        return False
                    else:
                        return True
                else:
                    if jour > 29:
                        return False
                    else:
                        return True
            else:
                if jour > 31:
                    return False
                else:
                    return True
        else:
            return True
    else:
        return False

def get_jour_semaine(jour, mois, annee):
    a = calendar.weekday(annee, mois, jour)
    JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

    return JOURS[a]

# Programme principal
def main():
    annee = 2030
    mois = randint(1, 15)
    jour = randint(1, 40)
    if est_valide(jour, mois, annee):
        print("Le", end=' ')
        print(jour, mois, annee, sep='/', end=' ')
        print("est un", get_jour_semaine(jour, mois, annee))
    else:
        print("Random >>> Le", end=' ')
        print(jour, mois, annee, sep='/', end=' ')
        print("n' est pas une date valide.")

    annee = 2030
    mois = 10
    jour = 20
    print("Instance(20/10/2030) >>> Le", end=' ')
    print(jour, mois, annee, sep='/', end=' ')
    print("est un ", get_jour_semaine(jour, mois, annee), ".", sep='')

    annee = 2030
    mois = 10
    jour = 35
    print("Instance(35/10/2030) >>> Le", end=' ')
    print(jour, mois, annee, sep='/', end=' ')
    print("n' est pas une date valide.")

if __name__ == '__main__':
    main()
# Fin
