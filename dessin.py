# coding: UTF-8
"""
Script: Prog1/dessin
"""

# Imports
import turtle

# Fonctions
def carre(x, y, cote, couleur):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(couleur)
    for i in range(4):
        turtle.forward(cote)
        turtle.left(90)
        i += 1
    turtle.up()

    return None

def spirale(x, y, espacement, nbr_segment, couleur):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(couleur)
    for i in range(nbr_segment):
        turtle.forward(espacement)
        turtle.right(90)
        espacement += 5
    turtle.up()

    return None

def pentacle(x, y, longeur, couleur):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(couleur)
    for i in range(5):
        turtle.forward(longeur)
        turtle.right(180-(180/5))
    turtle.up()

    return None

def rectangle(longueur):
    for i in range(1):
        turtle.left(90)
        turtle.forward(longueur)
        turtle.right(90)
        turtle.write(longueur)
        turtle.forward(6)
        turtle.right(90)
        turtle.forward(longueur)
        turtle.left(90)
        turtle.forward(2)
    return None

# Programme principal
def main():
    turtle.clear()
    spirale(0, 0, 5, 23, "red")
    turtle.exitonclick()

if __name__ == '__main__':
    main()
# Fin
