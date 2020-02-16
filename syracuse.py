# coding: UTF-8
"""
Script: Prog1/syracuse
Création: valen, le 23/11/2019
"""


# Imports

# Fonctions
N_MAX = 100     # nombre de termes maximum dans l'analyse des suites de Syracuse

def prochaine_valeur(u_n):
    if u_n % 2 == 0:
        u_n_2 = u_n // 2
    else:
        u_n_2 = (u_n * 3) + 1
    return u_n_2

def vol(a, N):
    print(str(a)+", ", end="")
    for i in range(0, N):
        a = prochaine_valeur(a)
        if i != N-1:
            print(str(a)+", ", end="")
        else:
            print(str(a))
    return a, N

def temps_vol(a):
    n = 0
    for i in range(0, N_MAX):
        while a != 1:
            a = prochaine_valeur(a)
            n += 1
    if n < N_MAX:
        return n
    else:
        return N_MAX

def altitude_max(a):
    Max = a
    for i in range(0, N_MAX):
        a = prochaine_valeur(a)
        if Max < a:
            Max = a
    return Max


# Programme principal
def main():
    print([vol(14, 17)])
    print(temps_vol(14))
    print(str(altitude_max(14)))


if __name__ == '__main__':
    main()
# Fin