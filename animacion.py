from tkinter import*
tk=Tk()
canvas=Canvas(tk,width=200,height=200)
canvas.pack()

imagen=PhotoImage(file="ball.gif")
canvas.create_image(30,5,anchor=NW,image=imagen)
tk.mainloop()



##animacion basica
import time
from tkinter import*
a=Tk()
canvas=Canvas(a,width=400,height=200)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    canvas.move(1,5,0)
    a.update()
    time.sleep(0.05)
a.mainloop()

