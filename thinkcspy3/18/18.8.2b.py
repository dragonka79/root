import turtle

"""" Cesaro-négyzet """

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
t.backward(800)
t.left(90)
t.forward(500)
t.right(90)
t.pendown()

ang = 10
m = ang - 180
size = 5

def cesaro(t, rend, meret):
    """ Cesaro-fraktál """
    if rend == 0:
        t.forward(meret * 100)
    else:
        for szog in [m / 2, -m, (m / 2), 0]:
            cesaro(t, rend-1, meret/2)
            t.left(szog)
for i in range(4):
    cesaro(t, 2, size)
    t.right(90)

a.mainloop()