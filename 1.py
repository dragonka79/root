import turtle

a = turtle.Screen()

def sokszög_rajzolasa(t, h, s):
    """
    Egy s oldalú h oldalhosszúságú sokszög rajzolása a t teknőccel
    """
    for i in range(s):
        t.forward(h)
        t.left(360/s)

s = 8
Zoli = turtle.Turtle()
sokszög_rajzolasa(Zoli, 50, s)

a.mainloop()
