import turtle
import math

"""" Cesaro-négyzet, korrigált oldalakkal, az oldalak minden rend esetén ugyanolyan hosszúak"""

a = turtle.Screen()
a.bgcolor("lightgreen")
a.setup(width=1.0, height=1.0) # Fullscreen
# turtle.screensize(canvwidth=800, canvheight=400, bg="lightgreen")
t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(0)
# t.hideturtle()

t.penup()
t.backward(500)
t.left(90)
t.forward(500)
t.right(90)
t.pendown()

ang = 10   # This can be changed
m = ang - 180
rad = math.radians(ang) # The attributum of math.sin should be expressed in radius
size = 5


def cesaro(t, rend, meret):
    """ Cesaro-fraktál """
    x = meret / (2 * (1 + math.sin(rad / 2)))
    if rend == 0:
        t.forward(x * 400)
    else:
        for szog in [m / 2, -m, (m / 2), 0]:
            cesaro(t, rend-1, x)
            t.left(szog)
for i in range(4):
    cesaro(t, 3, size)
    t.right(90)

a.mainloop()