# -*- coding: UTF-8 -*-
"""
Script : prog2/pendu.py
"""
# Import
import tools_chaines, random

# Constantes
COUPS_MAX = 10

# fonctions
def choix_mot():
    return random.choice(tools_chaines.liste_mots_francais())

def affiche_mot_un_caractere(mot, caractere):
    for i in range(len(mot)):
        if caractere in mot[i]:
            print(caractere, end='')
        else:
            print('-', end='')

def affiche_mot(mot, propositions):
    for caractere in mot:
        if caractere in propositions:
            print(caractere, end='')
        else:
            print('-', end='')

def est_trouve(mot, lettres):
    a = 0
    for i in range(len(mot)):
        if mot[i] in lettres:
            a += 1
        else:
            a -= 1
    if a == len(mot):
        return True
    else:
        return False

def saisie(propositions):
    lettre = str(input('Entrez un caractere : '))
    lettre = lettre.lower()
    if (len(lettre) > 1) or (lettre in propositions):
        return saisie(propositions)
    else:
        return lettre

def main():
    # Programme principal
    print(">>> Jeu du pendu <<<")
    mot = choix_mot() # Choix du mot au hasard par l'ordinateur
    print("Mot à deviner pour debuggage :", mot)

    # Initialisations des variables de la boucle
    coup = 0              # nombre de coups joués par le joueur
    coup_perdant = 0      # nombre de coups perdant du joueur
    propositions = ""     # lettres proposées par le joueur
    partie_finie = False  # la partie est-elle finie ?

    # Boucle de jeu
    while not partie_finie:
        print("Coup n°{} (reste {} coups perdants possibles) :".format(coup, COUPS_MAX - coup_perdant))

        affiche_mot(mot, propositions)  # Affichage du mot masqué pour le joueur

        lettre = saisie(propositions)   # Choix d'une lettre
        propositions += lettre          # Ajout de la lettre au proposition

        # Analyse de la lettre et conséquences sur les coups perdants
        if lettre in mot:
            pass
        else:
            coup_perdant += 1
            if coup_perdant == 10:
                partie_finie = True

        # La partie est-elle finie ?
        if est_trouve(mot, propositions):
            partie_finie = True
        else:
            coup = coup + 1
    # Fin de la boucle de jeu

    # Analyse du jeu ? Le joueur a-t-il gagné
    if est_trouve(mot, propositions):
        print("Gagné : le mot est :", mot)
    else:
        print("Perdu : le mot était :", mot)


if __name__ == "__main__":
    main()
