# coding: UTF-8
"""
Script: Prog1/horloge
"""


# Imports
import tools_horloge

# Fonctions
def calcule_offset_horloge(offset):
    heures = tools_horloge.get_heures()
    minutes = tools_horloge.get_minutes()
    minutes += offset
    heures += minutes // 60
    heures_futures = heures % 24
    minutes_futures = minutes % 60

    return [heures_futures, minutes_futures]
# Programme principal
def main():
    print(calcule_offset_horloge(90))

if __name__ == '__main__':
    main()
# Fin
