# coding: UTF-8
"""
Script: Prog2/transmission
Création: arroyoe, le 04/02/2020
"""


# Imports
import tools_transmission
import math
import random


# Fonctions
def saisie():
    valide = False
    while not valide:
        entree = input("Entrer une chaine de 10 ou rien : ")
        if entree == "":
            return "j aime python"
        if not len(entree) < 10:
            valide = True
    return entree


def codage_chaine2bits(message):
    liste = []
    for car in message:
        liste.extend(tools_transmission.codage_caractere2bits(car))
    return liste


def decodage_bits2chaine(bits):
    liste = []
    for i in range(0, len(bits), 8):
        tranche = bits[i:i + 8]
        dcode = tools_transmission.decodage_bits2caractere(tranche)
        print(dcode, end="")
        liste.append(dcode)
    return liste


def modulation(bits, A):
    liste = []
    for bit in bits:
        liste.append(A) if bit == 1 else liste.append(-A)
    return liste


def canal(signal_module, P):
    liste = []
    for signal in signal_module:
        bruit = random.gauss(0, math.sqrt(P))
        liste.append(signal + bruit)
    return liste


def demodulation(signal_recu):
    liste = []
    for sig in signal_recu:
        if sig >= 0:
            liste.append(1)
        else:
            liste.append(0)
    return liste


def taux_erreur_binaire(bits_emis, bits_recus):
    nberreur = 0
    for i in range(len(bits_emis)):
        if bits_emis[i] != bits_recus[i]:
            nberreur += 1
    return nberreur


# Programme principal
def main():
    A = 1
    P = 10 ** (-1)
    message = saisie()  # éventuellement "j aime python"
    print("Message émis :", message)
    bits_emis = codage_chaine2bits(message)
    signal_module = modulation(bits_emis, A)
    signal_bruite = canal(signal_module, P)
    bits_recus = demodulation(signal_bruite)
    message_recu = decodage_bits2chaine(bits_recus)
    print("Message reçu :", message_recu)
    # Tracé avec matplotlib
    tools_transmission.visualise_transmission(message, bits_emis, signal_module,
                                              signal_bruite, bits_recus, message_recu)


if __name__ == '__main__':
    main()
# Fin