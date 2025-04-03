import turtle
from math import sqrt

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Zoli = turtle.Turtle()
Zoli.hideturtle()
Zoli.color("blue")
Zoli.pensize(3)
Zoli.speed(0)


I = (135, sqrt(2) * 100)
J = (-120, 100)
K = (135, 100)

house = [(0, 100), I, K, I, K, J, J, (-30, 100)]

for (spin, go) in house:
    Zoli.left(spin)
    Zoli.forward(go)

ablak.mainloop()

