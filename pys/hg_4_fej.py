#4.1.a Alapfüggvény négyzet rajzolására

import turtle

def negyzet_rajzolasa(t, h):
    """Egy h oldalú négyzet rajzolása t teknőccel"""
    for i in range(4):
        t.forward(h)
        t.left(90)

#Egy ablak létrehozása és egyéb tulajdonságok beállítása

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Sanyi találkozik egy függvénnyel")

Sanyi = turtle.Turtle()
negyzet_rajzolasa(Sanyi, 50)
a.mainloop()

# 4.1.b  A 4.1.a módosítása

import turtle

def tobbszinu_negyzet_rajzolas(t, h):
    """Egy h oldalhosszúságú, többszínű négyzet rajzoltatása a t teknőccel"""
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(h)
        t.left(90)

#Egy ablak létrehozása és tulajdonságainak beállítása
a = turtle.Screen()
a.bgcolor("lightgreen")

#Eszti létrehozása és tulajdonságainak beállítása
Eszti = turtle.Turtle()
Eszti.pensize(3)


meret = 20          # A legkisebb négyzet mérete
for i in range(15):
    tobbszinu_negyzet_rajzolas(Eszti, meret)
    meret = meret + 10      #Növeljük a következő négyzet méretét
    Eszti.forward(10)       # Kicsit arrébb léptetjük a teknőcöt
    Eszti.right(18)         # És kicsit elfordítjuk

a.mainloop()

#4.2.a Téglalap rajzolása illetve a téglalap függvény felhasználása négyzethez


import turtle

def teglalap_rajzolas(t, sz, m):
    """Egy sz szélességű, m magasságú téglalap rajzoltatása t teknőccel"""
    for i in range(2):
        t.forward(sz)
        t.left(90)
        t.forward(m)
        t.left(90)

def negyzet_rajzolas(tk, sz):
    teglalap_rajzolas(tk, sz, sz)

a = turtle.Screen()
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
szelesseg = 100
magassag = 60

teglalap_rajzolas(Eszti, szelesseg, magassag)
negyzet_rajzolas(Eszti, szelesseg)
a.mainloop()

#4.4.a Függvény, amely x-et az a hatványra emeli

x = 2
a = 3

print(pow(x, a))


#4.5.a A kamatos kamat függvénye a 2.14.15 alapján

def kamatos_kamat(c, r, m ,t):
    """A futamidő végén kapott érték számítása c befektetett összegre a kamatos
    kamat képletének megfelelően"""
    fv = c *(1 + r/m) ** (m*t)
    return fv   #Ez az újdonság teszi a függvényt produktív függvénnyé.

#Most, hogy van egy függvényünk, hívjuk is meg!
befektetettOsszeg = float(input("Mekkora összeget kíván befektetni? "))
vegOsszeg = kamatos_kamat(befektetettOsszeg, 0.08, 12, 1)
print("A futamidő végén Önnek ennyi pénze lesz: ", vegOsszeg)



#4.9.1

import turtle

a = turtle.Screen()
a.title("négyzet")
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)
t.color("magenta")
t.speed(1)

def negyzet():

    for i in range(4):
        t.forward(20)
        t.left(90)


for i in range(5):

    negyzet()
    t.penup()
    t.forward(40)
    t.pendown()

a.mainloop()



#4.9.2

import turtle
import math

a = turtle.Screen()
a.title("négyzet")
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)
t.color("magenta")
t.speed(1)
k = 20

def negyzet(k):

    for i in range(4):
        t.forward(k)
        t.left(90)


for i in range(5):


    negyzet(k)
    t.penup()
    t.right(135)
    t.forward(10 * math.sqrt(2))
    t.left(135)
    t.pendown()
    k += 20

a.mainloop()



#4.9.3

import turtle


a = turtle.Screen()
a.title("sokszog_rajzolas(t, n, sz)")
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(3)
Eszti.color("magenta")
Eszti.speed(1)
Eszti.penup()
Eszti.right(90)
Eszti.forward(150)
Eszti.left(90)
Eszti.pendown()

def sokszog_rajzolas(t, n, sz):

    for i in range(n):
        t.forward(sz)
        t.left(360 / n)

sokszog_rajzolas(Eszti, 8, 50)

a.mainloop()

#4.9.4

import turtle

a = turtle.Screen()
a.title("Gyönyörű minta")
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(3)
Eszti.color("blue")
Eszti.speed(0)
Eszti.hideturtle()
Eszti.penup()
Eszti.right(90)
Eszti.forward(50)
Eszti.left(90)
Eszti.pendown()

h = 200

def abra(h):

    for i in range(5):
        Eszti.forward(h/2)
        Eszti.left(90)
        Eszti.forward(h/2)
        Eszti.left(90)
        Eszti.forward(h)
        Eszti.left(90)
        Eszti.forward(h)
        Eszti.left(90)
        Eszti.forward(h)
        Eszti.left(90)
        Eszti.forward(h / 2)
        Eszti.left(90)
        Eszti.forward(h)
        Eszti.backward(h / 2)
        Eszti.right(90)
        Eszti.forward(h / 2)
        Eszti.backward(h)
        Eszti.forward(h / 2)
        Eszti.right(162)

abra(h)
a.mainloop()


#4.9.5.

import turtle

a = turtle.Screen()
a.title("spirál")
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(1)
Eszti.color("blue")
Eszti.speed(0)
Eszti.hideturtle()
Eszti.penup()
Eszti.right(90)
Eszti.forward(50)
Eszti.left(90)
Eszti.pendown()

h = 20
t = 91
def spiral(h):

    for i in range(200):
        Eszti.right(t)
        Eszti.forward(h/2)
        h = h + 5


spiral(h)
a.mainloop()


#4.9.6

import turtle


a = turtle.Screen()
a.title("szabalyos_haromszog_rajzolas(t, sz)")
a.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.pensize(3)
Eszti.color("magenta")
Eszti.speed(1)
Eszti.penup()
Eszti.right(90)
Eszti.forward(150)
Eszti.left(90)
Eszti.pendown()

def sokszog_rajzolas(t, n, sz):

    for i in range(n):
        t.forward(sz)
        t.left(360 / n)

def szabalyos_haromszog_rajzolas(t, sz):
    n = 3
    sokszog_rajzolas(t, n, sz)

szabalyos_haromszog_rajzolas(Eszti, 150)

a.mainloop()


# 4.9.7 Az első n természetes szám összege

def osszeg(n):
    k = 0
    for i in range(n+1):
        k += i
    return print(k)


osszeg(100)



#4.9.8 Kör területe

import math

def kor_terulet(r):

    T = (r ** 2) * math.pi
    return print(f"A(z) {r} sugarú kör területe: {T}")

kor_terulet(pow(1, (1 / 2)))

#4.9.9. h oldalú pentagram

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.color("red")
Eszti.left(36)
Eszti.pensize(1)
Eszti.hideturtle()


def pentagram(h):
    for i in range(5):
        Eszti.speed(1)
        Eszti.forward(h)
        Eszti.left(144)

pentagram(400)

ablak.mainloop()
