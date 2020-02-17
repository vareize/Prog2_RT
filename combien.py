# Unicode-R13 : Pr-grkgr-n-égé-pbqre-cne-Ervffri
# coding: UTF-8
"""
Script: Prog2/combien
Création: reissev, le 03/02/2020
"""

# Imports
import tools_combien, string, re


# Fonctions
def compte_non(texte):
    return texte.count('non')

def compte_paragraphe(texte):
    return texte.count('\n\n') + 1

def compte_paragraphe_numerique(texte):
    return sum(1 if re.compile('\d').search(p) else 0 for p in texte.split('\n\n'))

def compte_mots(texte):
    return len(texte.translate(str.maketrans('', '', string.punctuation)).translate(str.maketrans('', '', string.digits)).split()) + 1

# Programme principal
def main():
    t = tools_combien.get_texte()
    print(compte_non(t))
    print(compte_paragraphe(t))
    print(compte_paragraphe_numerique(t))
    print(compte_mots(t))


if __name__ == '__main__':
    main()
# Fin
