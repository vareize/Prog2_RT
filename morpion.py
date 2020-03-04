"""
Jeu du morpion
"""

# Import
import random

# Fonctions
def initialisation_grille():
    """Initialisation"""
    grille = [['_' for i in range(3)] for j in range(3)]
    return grille


def affiche_grille(grille):
    print("  A B C")
    for i in range(3):
        print(i+1, ' '.join(grille[i]))
    return None


def est_vide(grille, i, j):
    return grille[i][j] == "_"


def saisie():
    s = input("entrez une case :")
    while not ((len(s) == 2) and (s[0] in ['1', '2', '3']) and (s[1] in ['A', 'B', 'C'])):
        s = input("Entrez une case valide :")
    return s


def conversion(case):
    case, n, L = [i for i in case], [1, 2, 3], ["A", "B", "C"]
    i = n.index(int(case[0]))
    j = L.index(case[1])
    return [i, j]


def ajoute_case_joueur(grille):
    a = conversion(saisie())
    while not est_vide(grille, a[0], a[1]):
        return ajoute_case_joueur(grille)
    grille[a[0]][a[1]] = 'X'
    return True


def get_cases_vides(grille):
    res = []
    for i in range(len(grille)):
        for j in range(len(grille[i])):
            if grille[i][j] == '_':
                res.append([i, j])
    return res


def ajoute_case_ordi(grille):
    gcv = get_cases_vides(grille)
    if len(gcv) != 0:
        case_ordi = random.choice(gcv)
        grille[case_ordi[0]][case_ordi[1]] = 'O'
        return True
    else:
        return False


def est_pleine(grille):
    if not get_cases_vides(grille):
        return True
    else:
        return False


def est_gagnante_ligne(grille, pion):
    a = 0
    for i in range(len(grille)):
        if grille[i].count(pion) == 3:
            a += 1
    if a > 0:
        return True
    else:
        return False


def est_gagnante_colonne(grille, pion):
    a, b, c = 0, 0, 0
    for i in range(len(grille)):
        if pion == grille[i][0]:
            a += 1
        if pion == grille[i][1]:
            b += 1
        if pion == grille[i][2]:
            c += 1
    if a == 3 or b == 3 or c == 3:
        return True
    else:
        return False


def est_gagnante_diagonale(grille, pion):
    return True if (pion == grille[0][0] == grille[1][1] == grille[2][2]) or (pion == grille[0][2] == grille[1][1] == grille[2][0]) else False


def est_gagnante(grille, pion):
    return True if est_gagnante_ligne(grille, pion) or est_gagnante_colonne(grille, pion) or est_gagnante_diagonale(grille, pion) else False


def main():
    # Une partie de morpion
    # *********************
    # 1) initialisations
    grille = initialisation_grille()   # la grille initiale
    pion = 'X'                         # le joueur débutant la partie -> le joueur


    # 2) boucle de jeu, itérant tant que la partie n'est pas finie
    partie_finie = False
    while not partie_finie:
        # affichages
        affiche_grille(grille)                      # la grille
        print("Au joueur", pion, "de jouer")        # le joueur qui doit jouer : X ou O

        # quelle est la case choisie (case vide) ? par saisie clavier si c'est le joueur, au hasard si c'est l'ordi
        if pion == "X": # le joueur
            ajoute_case_joueur(grille)
        else:           # l'ordinateur
            ajoute_case_ordi(grille)

        # la partie est-elle finie (gagnante/perdante/ex-aequo) ?
        analyse_fin_partie = est_gagnante(grille, pion) # <- à modifier
        if analyse_fin_partie:
            partie_finie = True
        else:  # si non : prépare la prochaine itération en changeant de pions pour alterner joueur <-> ordi
            if pion == 'X':
                pion = 'O'
            else:
                pion = 'X'
    # fin de la boucle de jeu

    # Analyse finale : la partie est-elle gagnée ou perdu ? & affichage final



    # fin du main


if __name__ == "__main__":
    main()

