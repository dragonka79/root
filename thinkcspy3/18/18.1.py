import turtle
import time

a = turtle.Screen()
# a.bgcolor("lightgreen")
turtle.screensize(canvwidth=800, canvheight=400, bg="lightgreen")
t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)
t.speed(0)
t.hideturtle()

t.penup()
t.backward(700)
t.pendown()

def koch(t, rend, meret):
    """ Koch görbe"""
    if rend == 0:
        t.forward(meret * 100)
    else:
        for szog in [60, -120, 60, 0]:
            koch(t, rend-1, meret/3)
            t.left(szog)

koch(t, 4, 8)

a.mainloop()