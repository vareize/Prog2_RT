# coding: UTF-8
"""
Script: Prog1/fractale
"""


# Imports
import turtle as trl

# Fonctions
def triangle(l):
    for i in range(3):
        trl.forward(l)
        trl.left(120)


def motif1(l):
    l = l/3
    trl.forward(l)
    trl.right(60)
    trl.forward(l)
    trl.left(120)
    trl.forward(l)
    trl.right(60)
    trl.forward(l)

def motif2(l):
    l = l/3
    motif1(l)
    trl.right(60)
    motif1(l)
    trl.left(120)
    motif1(l)
    trl.right(60)
    motif1(l)

def motif3(l):
    l = l/3
    motif2(l)
    trl.right(60)
    motif2(l)
    trl.left(120)
    motif2(l)
    trl.right(60)
    motif2(l)

def motif4(l):
    l = l/3
    motif3(l)
    trl.right(60)
    motif3(l)
    trl.left(120)
    motif3(l)
    trl.right(60)
    motif3(l)

def flocon1(l):
    for i in range(3):
        motif1(l)
        trl.left(120)

def flocon2(l):
    for i in range(3):
        motif2(l)
        trl.left(120)

def flocon3(l):
    for i in range(3):
        motif3(l)
        trl.left(120)

def flocon4(l):
    for i in range(3):
        motif4(l)
        trl.left(120)

def von_koch(l):
    trl.speed(10)
    trl.up()
    trl.goto(-200, -100)
    trl.down()
    triangle(l)
    flocon1(l)
    flocon2(l)
    flocon3(l)
    flocon4(l)
    trl.exitonclick()

# Programme principal
def main():
    von_koch(400)

if __name__ == '__main__':
    main()
# Fin
