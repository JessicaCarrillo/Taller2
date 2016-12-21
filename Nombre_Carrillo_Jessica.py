import turtle
import os 
 
win=turtle.Screen()
#win.bgcolor("pink")
t = turtle.Pen()
t.reset()
t.color(1,1,0)
t.begin_fill()
t.forward(180)
t.left(90)
t.forward(180)
t.left(90)
t.forward(-100)
t.left(-90)
t.forward(40)
t.left(90)
t.forward(90)

t.left(360)
t.forward(90)
t.left(360)
t.forward(90)
t.left(90)
t.forward(40)
t.left(-270)

t.forward(120)
t.left(-270)
t.forward(-60)
t.left(-180)
t.forward(80)
t.left(270)
t.forward(140)
t.left(90)
t.forward(40)

t.end_fill()


turtle.getscreen()._root.mainloop()
