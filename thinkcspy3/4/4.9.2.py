import turtle
from math import sqrt

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)
t.speed(0)


def square(h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.penup()
    t.right(135)
    t.forward(10* sqrt(2))
    t.left(135)
    t.pendown()

for i in range(1, 6):
    square(i * 20)

a.mainloop()