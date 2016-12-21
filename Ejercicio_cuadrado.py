

import turtle
a=turtle.Pen()

def cuadrado(size):
    for x in range(1,4):
        a.forward(size)
        a.left(90)

cuadrado(100)
