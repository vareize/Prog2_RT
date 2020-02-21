#  import
import random


#  Fonctions
def capitales():
    return {
        "Pays-Bas": "Amsterdam",
        "Allemagne": "Berlin",
        "Autriche": "Vienne",
        "Belgique": "Bruxelles",
        "Chypre": "Nicosie",
        "Espagne": "Madrid",
        "Estonie": "Tallinn",
        "Finlande": "Helsinki",
        "France": "Paris",
        "Grèce": "Athènes",
        "Irlande": "Dublin",
        "Italie": "Rome",
        "Lettonie": "Riga",
        "Lituanie": "Vilnius",
        "Luxembourg": "Luxembourg",
        "Malte": "La Valette",
        "Portugal": "Lisbonne",
        "Suède": "Stockholm",
        "Slovaquie": "Bratislava",
        "Slovénie": "Ljubljana",
        "Bulgarie": "Sofia",
        "Croatie": "Zagreb",
        "Danemark": "Copenhague",
        "Hongrie": "Budapest",
        "Pologne": "Varsovie",
        "Roumanie": "Bucarest",
        "Royaume-Uni": "Londres",
        "République Tchèque": "Prague",
    }

def affichage_capitales(europe):
    for values in europe.values():
        print(values)
    return None

def affichage_capitales_triees(europe):
    return sorted([values for values in europe.values()])

def choix_pays_aleatoire(europe):
    return random.choice(list(europe.keys()))

def choix_reponses_possibles(pays, europe):
    dic = {pays: europe[pays]}
    while len(dic) < 4:
        pays = choix_pays_aleatoire(europe)
        if pays not in dic:
            dic[pays] = europe[pays]
    return dic

def une_question(europe, pays):
    global i
    rep = affichage_capitales_triees(choix_reponses_possibles(pays, europe))
    print("Quelle est la capitale de " + pays + " ?")
    for i in range(4):
        print(str(i + 1) + " - " + rep[i])


#  Programme principal
def main():
    # Récupération de la liste des pays
    europe = capitales()  # <- à compléter

    score, i = 0, 0
    # Boucle de jeu : ici 5 parties
    while i < 5:  # <- à compléter
        # Choix du pays
        pays = choix_pays_aleatoire(europe)  # <- à compléter
        # Question
        une_question(europe, pays)
        res = input("Entrez une réponce :")# <- à compléter
        if res:  # La réponse est correcte
            print("Réponse correcte")
            score += 1
        else:
            print("Mauvaise réponse")
        i += 1
    print("Votre score final est " + str(score))


if __name__ == '__main__':
    main()
# Fin
