# coding: UTF-8
"""
Script: Prog1/graphique_syracuse
Création: valen, le 26/11/2019
"""


# Imports
import turtle as trl
import syracuse as src
import dessin as dss

# Fonctions
def x_graph():
    trl.color("blue")
    trl.up()
    trl.goto(-300, -150)
    trl.down()
    trl.forward(800)
    trl.goto(-300, -150)

def y_graph():
    a = 14
    l = a
    for i in range(100):
        dss.rectangle(l)
        a = src.prochaine_valeur(a)
        l = a

def graph_syca():
    trl.speed(10)
    trl.setup(width=100, height=75, startx=0, starty=0)
    trl.setup(width=0.75, height=0.5, startx=None, starty=None)
    x_graph()
    y_graph()
    trl.exitonclick()

# Programme principal
def main():
    graph_syca()


if __name__ == '__main__':
    main()
# Fin