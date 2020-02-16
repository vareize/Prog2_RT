# coding: UTF-8
"""
Script: Prog1/crypto
"""

# Imports
import string

# Fonctions
def car_rot13(caractere):
    return str(string.ascii_lowercase[(string.ascii_lowercase.find(caractere) + 13) % 26])

def rot13(chaine):
    i, res = 0, []
    while i < len(chaine):
        res.append(car_rot13(chaine[i]))
        i += 1
    return ''.join(res)

def car_cesar(caractere, decalage):
    return str(string.ascii_lowercase[string.ascii_lowercase.find(caractere) + decalage])

def vigenere_numerique(chaine, liste):
    i, res = 0, []
    while i < len(chaine):
        res.append(car_cesar(chaine[i], liste[i % len(liste)]))
        i += 1
    return ''.join(res)

def erenegiv_numerique(chaine_chiffrer, nombre):
    i, res = 0, []
    while i < len(chaine_chiffrer):
        res.append(string.ascii_lowercase[string.ascii_lowercase.find(chaine_chiffrer[i]) - (nombre[i % len(nombre)])])
        i += 1
    return ''.join(res)

def vigenere(mot, code):
    i, res = 0, []
    while i < len(mot):
        car = ((ord(mot[i]) + ord(code[i % len(code)])) % 26) + 104
        if car > 122:
            car -= 26
        res.append(chr(car))
        i += 1
    return ''.join(res)

def erenegiv(mot, code):
    i, res = 0, []
    while i < len(mot):
        car = ((ord(mot[i]) - ord(code[i % len(code)])) % 26) + 104
        if car < 97:
            car += 26
        elif car > 122:
            car -= 26
        res.append(chr(car))
        i += 1
    return ''.join(res)

# Programme principal
def main():
    print(erenegiv("biapmuzkbyanwe", "python"))
    """resultat = 'tropfortpython'"""

if __name__ == '__main__':
    main()
# Fin






























""""
def erenegiv_numerique2(chaine_chiffrer, nombre):
    res = ""
    for (i, car) in enumerate(chaine_chiffrer):
        res += string.ascii_lowercase[(string.ascii_lowercase.find(car) - nombre[i]) % len(nombre)]
    return res

def erenegiv_numerique3(chaine_chiffrer, nombre):
    res = [string.ascii_lowercase[(string.ascii_lowercase.find(car) - nombre[i]) % len(nombre)] for (i, car) in enumerate(chaine_chiffrer)]
    return ''.join(res)
"""""
