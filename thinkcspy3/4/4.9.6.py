import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)
t.speed(1)
t.hideturtle()

sz = 100
def sokszog_rajzolas(t, n, sz):
    """ Szabályos n-szög rajzolása, általános megoldás bármely n-re"""
    for i in range(n):
        t.forward(sz)
        t.left(360 /n )

def szabalyos_haromszog_rajzolas(t, sz):
    sokszog_rajzolas(t, 3, sz)

szabalyos_haromszog_rajzolas(t, sz)

a.mainloop()
