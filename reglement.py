# coding: UTF-8
"""
Script: Python/reglement
Création: valen, le 12/11/2019
"""


# Imports

# Fonctions
def passage(note):
    if note >= 10:
        note = "validé"
    elif 8 <= note < 10:
        note = "à rattraper"
    elif 4 < note < 8:
        note = "recalé"
    else:
        note = "éliminatoire"
    return note

# Programme principal
def main():
    passage()

if __name__ == '__main__':
    main()
# Fin