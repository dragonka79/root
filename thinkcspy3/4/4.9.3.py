import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)
t.speed(1)
t.hideturtle()

def sokszog_rajzolas(t, n, sz):
    """ Szabályos n-szög rajzolása, általános megoldás bármely n-re"""
    for i in range(n):
        t.forward(sz)
        t.left(360 /n )

Eszti = t
n = 8
sz = 50

sokszog_rajzolas(t, n, sz)   

a.mainloop()