# 5.5.1 program ami lefut de nem csinál semmit, beléphet bármelyik if ágba.

n = 1
if n == 1:
    pass
else:
    pass

#5.12, oszlopokat rajzol, az oszlopok magasságai egy listában vannak +
#az oszlopoknak van talpa.

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.color("red")
Eszti.speed(0)
Eszti.hideturtle()

xs = [48, 117, 200, 240, 160, 260, 220]

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    t.begin_fill()           # Az új sor.
    t.left(90)
    t.forward(magassag)   # Rajzold meg a bal oldalt!
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)         # Az oszlop szélessége a tetején.
    t.right(90)
    t.forward(magassag)   # És ismét le.
    t.left(90)            # Fordítsd a teknőcöt a megfelelő irányba!
    t.end_fill()
    t.backward(40)      # Oszlop talpát rajzol
    t.forward(40)
    t.penup()
    t.forward(10)         # Hagyj egy kis rést minden oszlop után!
    t.pendown()

...
for m in xs:              # Tegyük fel, Eszti és xs kész vannak!
    rajzolj_oszlopot(Eszti, m)

# for i in range(len(xs)):
#     oszlopok_alja()

ablak.mainloop()

#5.14.1

napok = ['hétfő','kedd','szerda','csütörtök','péntek','szombat','vasárnap']
def nap_szám(x):
    return(print(napok[x]))
nap_szám(5)

#5.14.2

napok = ['hétfő','kedd','szerda','csütörtök','péntek','szombat','vasárnap']
x = int(input("Hányas számú napon indultál? "))
y = int(input("Hány napig voltál távol? "))

def nap_szám_távol():
    z = (napok[x])
    u = napok[(x + y + 1) % 7]
    return(print(f"A {z}-i napon indultál és a {u}-i napon térsz vissza."))

nap_szám_távol()

#5.14.6.1

def érdemjegy(x):
    if x >=90:
        print("Jeles")
    elif x >= 80 and x < 90:
        print("Jó")
    elif x >= 70 and x < 80:
        print("Közepes")
    elif x >= 60 and x < 70:
        print("Elégséges")
    elif x < 60 and x>= 0:
        print("Elégtelen")
    else:
        print("Ilyen vizsgapontszám nincs.")

érdemjegy(60)

#5.14.6.2

def érdemjegy(x):
    if x >=90:
        print(f"{x} pont, azaz 'Jeles'")
    elif x >= 80 and x < 90:
        print(f"{x} pont, azaz 'Jó'")
    elif x >= 70 and x < 80:
        print(f"{x} pont, azaz 'Közepes'")
    elif x >= 60 and x < 70:
        print(f"{x} pont, azaz 'Elégséges'")
    elif x < 60 and x>= 0:
        print(f"{x} pont, azaz 'Elégtelen'")


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in xs:
    érdemjegy(x)

#5.14.8.

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.speed(3)
Eszti.hideturtle()

xs = [48, 117, 200, 240, 160, 260, 220]

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    t.begin_fill()           # Az új sor.
    t.left(90)
    t.forward(magassag)   # Rajzold meg a bal oldalt!
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)         # Az oszlop szélessége a tetején.
    t.right(90)
    t.forward(magassag)   # És ismét le.
    t.left(90)            # Fordítsd a teknőcöt a megfelelő irányba!
    t.end_fill()
    t.backward(40)      # Oszlop talpát rajzol
    t.forward(40)
    t.penup()
    t.forward(10)         # Hagyj egy kis rést minden oszlop után!
    t.pendown()

...
for m in xs:             # Tegyük fel, Eszti és xs kész vannak!
    if m >= 200:
        Eszti.color("red")
        rajzolj_oszlopot(Eszti, m)
    elif m >= 100 and m < 200:
        Eszti.color("yellow")
        rajzolj_oszlopot(Eszti, m)
    else:
        Eszti.color("green")
        rajzolj_oszlopot(Eszti, m)

# for i in range(len(xs)):
#     oszlopok_alja()

ablak.mainloop()

#5.14.9

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.speed(1)
Eszti.hideturtle()

xs = [-48, 117, 200, -240, 160, 260, -220]

def rajzolj_oszlopot(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő magassággal """
    t.begin_fill()           # Az új sor.
    t.left(90)
    t.forward(magassag)   # Rajzold meg a bal oldalt!
    t.write("  "+ str(magassag))
    t.right(90)
    t.forward(40)         # Az oszlop szélessége a tetején.
    t.right(90)
    t.forward(magassag)   # És ismét le.
    t.left(90)            # Fordítsd a teknőcöt a megfelelő irányba!
    t.end_fill()
    t.backward(40)      # Oszlop talpát rajzol
    t.forward(40)
    t.penup()
    t.forward(10)         # Hagyj egy kis rést minden oszlop után!
    t.pendown()

def rajzolj_oszlopot_neg(t, magassag):
    """ A t teknőc oszlopot rajzol a megfelelő negatív magassággal """
    t.begin_fill()
    t.left(90)
    t.forward(magassag)
    t.penup()
    t.forward(-16)
    t.pendown()
    t.write("  "+ str(magassag))
    t.penup()
    t.forward(16)
    t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(magassag)
    t.left(90)
    t.end_fill()
    t.backward(40)
    t.forward(40)
    t.penup()
    t.forward(10)
    t.pendown()


...
for m in xs:             # Tegyük fel, Eszti és xs kész vannak!
    if m >= 200:
        Eszti.color("red")
        rajzolj_oszlopot(Eszti, m)
    elif m >= 100 and m < 200:
        Eszti.color("yellow")
        rajzolj_oszlopot(Eszti, m)
    elif m < 100 and m >= 0:
        Eszti.color("yellow")
        rajzolj_oszlopot(Eszti, m)
    else:
        Eszti.color("blue")
        rajzolj_oszlopot_neg(Eszti, m)

# for i in range(len(xs)):
#     oszlopok_alja()

ablak.mainloop()

#5.9.10

def atfogo(a,b):
    if a > 0 and b > 0:
        c = ((a ** 2) + (b ** 2)) ** 0.5
        return print(c)
    else:
        print("A háromszog oldala legyen pozitív szám")
        return

atfogo(5, 12)

#5.9.11

def derekszogu_e(a,b,c):
    t = ((a ** 2) + (b **2)) - (c ** 2)
    e = 0.0000000000001
    if a > 0 and b > 0 and c > 0:
        print(abs(t) < e)
    else:
        print("A háromszog oldalai legyenek pozitív számok")


derekszogu_e(4,12,13)

#5.9.12

def derekszogu_e(a,b,c):
    t = ((a ** 2) + (b **2)) - (c ** 2)
    k = ((b ** 2) + (c **2)) - (a ** 2)
    l = ((a ** 2) + (c **2)) - (b ** 2)

    e = 0.0000000000001

    if a > 0 and b > 0 and c > 0:
        print(abs(t) < e or abs(k) < e or abs(l) < e)
    else:
        print("A háromszog oldalai legyenek pozitív számok")


derekszogu_e(13,12,5)
