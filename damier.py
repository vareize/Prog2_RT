# coding: UTF-8
"""
Script: Prog1/damier
Création: valen, le 21/11/2019
"""


# Imports
import turtle

# Fonctions
def carre(x, y, taille, couleur):
    turtle.speed(10)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.pencolor(couleur)
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(taille)
        turtle.right(90)
        i += 1
    turtle.end_fill()
    turtle.up()
    return None

def ligne(x, y, taille, couleurs):
    turtle.speed(10)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    for i in range(5):
        carre(x, y, taille, couleurs[0])
        turtle.forward(taille)
        x += taille
        carre(x, y, taille, couleurs[1])
        x += taille
    return None

def deux_lignes(x, y, taille, couleurs):
    turtle.speed(10)
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    x2 = x
    y2 = y - taille
    ligne(x, y, taille, couleurs)
    for i in range(5):
        carre(x2, y2, taille, couleurs[1])
        turtle.forward(taille)
        x2 += taille
        carre(x2, y2, taille, couleurs[0])
        x2 += taille
    return None

def damier(x, y, taille, couleurs):
    turtle.speed(10)
    for i in range(5):
        deux_lignes(x, y, taille, couleurs)
        y = y - taille * 2
    return None

# Programme principal
def main():
    damier(-200, 100, 25, ['pink', 'green'])
    turtle.exitonclick()


if __name__ == '__main__':
    main()
# Fin