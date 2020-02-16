# coding: UTF-8
"""
Script: Prog1/carre
"""

# Imports

# Fonctions
def carre2D():
    for dizaine in range(10):
        for unite in range(10):
            print(f"{dizaine}{unite}", end=" ")
        print()
    return None

def carre2D_barre(dizaine, unite):
    nombre_colonne_ligne = 10
    for d in range(nombre_colonne_ligne):
        if dizaine != d:
            for u in range(nombre_colonne_ligne):
                if unite != u:
                    print(f"{d}{u}", end=" ")
                else:
                    print("**", end=" ")
        else:
            print("** "*nombre_colonne_ligne, end="")
        print()
    return None

def multiplication():
    multiple = 1
    for multiple_dizaine in range(1, 11):
        for multiple_unite in range(1, 11):
            print(multiple_unite*multiple, end="\t")
        multiple += 1
        print()
    return None




# Programme principal
def main():
    multiplication()


if __name__ == '__main__':
    main()
# Fin
