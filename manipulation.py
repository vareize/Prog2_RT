# coding: UTF-8
"""
Script: Prog2/manipulation
"""


# Imports
import tools_chaines

# Fonctions
def affiche_debut_dictionnaire():
    l, res = tools_chaines.liste_mots_francais(), []
    for i in range(5):
        res.append(l[i])
    return print('\n'.join(res))

def compte_mots_dictionnaire(caractere):
    l, res = tools_chaines.liste_mots_francais(), 0
    for i in range(len(l)):
        if l[i].startswith(caractere):
            res += 1
    return res

def affiche_mots_avec_caractere(caractere, nombre):
    l, res = tools_chaines.liste_mots_francais(), []
    for i in range(len(l)):
        if l[i].count(caractere) == nombre:
            res.append(l[i])
    return print('\n'.join(res))

def indice_2eme_occurrence(chaine, caractere):
    l, p = chaine.count(caractere), chaine.find(caractere)
    if l > 1:
        for i in range(p+1, len(chaine)):
            if chaine[i] == caractere:
                return i
    else:
        return -1

def hamming(mot1, mot2):
    res = 0
    for i in range(len(mot1)):
        if mot1[i] != mot2[i]:
            res += 1
    return res

def scrabble(mot, lettres_disponibles):
    ldl = list(lettres_disponibles)
    for i in range(len(mot)):
        if mot[i] in ldl:
            ldl.remove(mot[i])
        else:
            return False
    return True

def suppression(mot, caractere):
    mot = list(mot)
    if caractere in mot:
        mot.remove(caractere)
    else:
        return ''.join(mot)
    return ''.join(mot)

# Programme principal
def main():
    pass


if __name__ == '__main__':
    main()
# Fin
