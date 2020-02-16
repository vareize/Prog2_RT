# coding: UTF-8
"""
Script: Prog1/magie
"""


# Imports
import tools_magie
# Fonctions
def calcul_spectateur(pointure, annee_naissance):
    res = pointure
    res *= 5
    res += 50
    res *= 20
    res += 1000
    res += (tools_magie.get_annee_courante()-2000)
    res -= annee_naissance
    return res

def calcul_spectateur_2019(pointure, annee_naissance):
    """Calcule la valeur magique demandée par le magicien au spectateur,
    en fonction de sa pointure et de son année de naissance, et renvoie la valeur calculée.

    Le calcul est fait en supposant que nous sommes en l'an 2019.
    """
    res = pointure
    res *= 5
    res += 50
    res *= 20
    res += 1000
    res += 19
    res -= annee_naissance
    return res

def get_pointure_from_valeur(pointure):
    res = str(pointure)
    res = (res[0:2])
    return int(res)

def get_age_from_valeur(age):
    res = str(age)
    res = (res[2:4])
    return int(res)


# Programme principal
def main():
    resultat = calcul_spectateur(37, 1989)
    pointure = get_pointure_from_valeur(resultat)
    age = get_age_from_valeur(resultat)
    print("Spectateur> La calculatrice affiche ", resultat)
    print("Magicien> Vous faites du", pointure, "et vous avez ", age, "ans.")


if __name__ == '__main__':
    main()
