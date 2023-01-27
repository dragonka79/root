import turtle
import time

""" Koch-hópehely"""

a = turtle.Screen()
a.bgcolor("lightgreen")
a.setup(width=1.0, height=1.0) # Fullscreen
# turtle.screensize(canvwidth=800, canvheight=400, bg="lightgreen")
t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(0)
t.hideturtle()

t.penup()
t.backward(400)
t.left(90)
t.forward(300)
t.right(90)
t.pendown()

def koch(t, rend, meret):
    """ Koch görbe"""
    if rend == 0:
        t.forward(meret * 100)
    else:
        for szog in [60, -120, 60, 0]:
            koch(t, rend-1, meret/3)
            t.left(szog)

for i in range(3):
    koch(t, 2, 8)
    t.right(120)

a.mainloop()