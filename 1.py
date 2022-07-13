import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.speed(0)
t.penup()
t.backward(200)
t.pendown()

xs = [48, -99, -100, 117, 199, 200, -240, 160, 260, 220]

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    if abs(magassag) >= 200:
        t.color("blue", "red")
    elif abs(magassag) >= 100 and magassag <200:
        t.color("blue", "yellow")  
    else:
         t.color("blue", "green")

    t.begin_fill()
    t.left(90)
    t.forward(magassag) # Rajzold meg a bal oldalt!
    if magassag >= 0:
        t.right(90)
        t.write(' ' + str(magassag))
    else:
        t.penup()
        t.backward(15)       
        t.pendown()
        t.write(' ' + str(abs(magassag)))
        t.penup()
        t.forward(15)
        t.pendown()
        t.right(90)
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