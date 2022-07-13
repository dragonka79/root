import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("blue", "red")
t.pensize(3)
t.speed(2)

xs = [48, 117, 200, 240, 160, 260, 220]

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    t.begin_fill()
    t.left(90)
    t.forward(magassag) # Rajzold meg a bal oldalt!
    t.right(90)
    t.write(' ' + str(magassag))
    t.forward(40) # Az oszlop szélessége a tetején.
    t.right(90)
    t.forward(magassag) # És ismét le.
    t.left(90) # Fordítsd a teknőcöt a megfelelő irányba!
    t.end_fill()
    t.penup()
    t.forward(10) # Hagyj egy kis rést minden oszlop után!
    t.pendown()


for m in xs: # Tegyük fel, Eszti és xs kész vannak!
    rajzolj_oszlopot(t, m)

a.mainloop()