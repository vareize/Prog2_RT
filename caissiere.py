# coding: UTF-8
"""
Script: Prog1/caissiere
"""

# Imports
import tools_caissiere
import math

# Fonctions
def affiche_prix(liste):
    a = 1
    for i in range(len(liste)):
        print("article "+str(a)+":"+" "+str(liste[i])+"€")
        a += 1
    return None

def calcul_montant(liste):
    l = int()
    for i in range(len(liste)):
        l = sum(liste)
    return l

def calcul_montant_avec_remise(liste, seuil, taux):
    res = int()
    l = []
    for i in range(len(liste)):
        if liste[i] >= seuil:
            l.append((liste[i]*((100-taux)/100)))
        else:
            l.append(liste[i])
        i += 1
    for i in range(len(l)):
        res = math.floor(sum(l))
    return res

def calcul_montant_a_rendre(montant_du):
    res = 500 - montant_du
    return res

def calcul_monnaie(montant):
    coupures = [100, 50, 20, 10, 5, 2, 1]
    for billet in coupures:
        nombres_billet = montant // billet
        reste_montant = montant % billet
        if (nombres_billet != 0) and (reste_montant != 1):
            print(f"{nombres_billet} x {billet}€", end="\n")
        else:
            print(f"{nombres_billet} x {billet}€  + ", end="")
        montant = reste_montant


# Programme principal
def main():
    l = tools_caissiere.get_liste_prix()
    print("Détails des articles :")
    affiche_prix(l)
    print("Total facturé (après remise): ", end="")
    print(str(calcul_montant_avec_remise(l, 10, 20))+"€")
    print("Montant à rendre sur 500€: "+str(calcul_montant_a_rendre(calcul_montant_avec_remise(l, 10, 20)))+"€, soit ", end="")
    calcul_monnaie(calcul_montant_a_rendre(calcul_montant_avec_remise(l, 10, 20)))

if __name__ == '__main__':
    main()
# Fin
