#3.1.1,2,3

import turtle

szinablak = input("Milyen háttérszine legyen az ablaknak? ")
szineszti = input("Milyen szine legyen Eszti teknősnek? ")
tollvastag = int(input("Milyen vastag legyen Eszti? "))
ablak = turtle.Screen()
ablak.bgcolor(szinablak)

ablak.title("Hello, Eszti!")

Eszti = turtle.Turtle()
Eszti.color(szineszti)
Eszti.pensize(tollvastag)

Eszti.forward(50)
Eszti.left(120)
Eszti.forward(50)

ablak.mainloop()


#Eszti teknős alakban

import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.shape("turtle")
# Eszti.shapesize(0.1,0.1, 0.1)
Eszti.color("blue")
Eszti.speed(10)

Eszti.penup()                # Ez új
meret = 20
for i in range(30):
   Eszti.stamp()             # Hagyj egy lenyomatot a vásznon!
   meret = meret + 3        # Növeld a méretet minden ismétlésnél!
   Eszti.forward(meret)      # Mozgasd ...
   Eszti.right(24)           #  ...  és fordítsd Esztit!

ablak.mainloop()




#3.8.1

for i in range(1,1001):
    print(f"{i}.Szeretjük a Python teknőcöket!")


#3.8.3

hónapok1 = ['január','február','március','április','május','június']
hónapok2 = ['július','augusztus','szeptember','október','november','december']

for a in hónapok1:
    print("Az év egyik hónapja " + a)

for a in hónapok2:
    print("Az év egyik hónapja " + a)

#3.8.5

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

#a
for i in xs:
    print(i)

#b
for i in xs:
    print(i, i ** 2)

#c
összeg = 0
for i in xs:
    összeg = összeg + i
print(összeg)

#d

szorzat = 1
for i in xs:
    szorzat = szorzat * i
print(szorzat)

#3.8.6

#1 háromszög

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)

for i in range(3):
    Zoli.forward(200)
    Zoli.left(120)

ablak.mainloop()


#2 négyzet

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)

for i in range(4):
    Zoli.forward(200)
    Zoli.left(90)

ablak.mainloop()


#3 hatszög

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)

for i in range(6):
    Zoli.forward(200)
    Zoli.left(60)

ablak.mainloop()



#4 nyolcszög

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
# Zoli.shape("turtle")
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)
Zoli.penup()
Zoli.right(135)
Zoli.forward(-200)
# Zoli.left(90)
Zoli.pendown()

for i in range(8):
    Zoli.forward(-200)
    Zoli.left(-45)

ablak.mainloop()



#3.8.7



import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.shape("turtle")
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)

szögek = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# Zoli.penup()
# Zoli.right(135)
# Zoli.forward(-200)
# Zoli.left(90)
# Zoli.pendown()

for i in szögek:
    Zoli.left(i)
    Zoli.forward(100)


ablak.mainloop()


#3.8.8



import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.shape("turtle")
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(4)

szögek = [160, -43, 270, -97, -43, 200, -940, 17, -86]
# Zoli.penup()
# Zoli.right(135)
# Zoli.forward(-200)
# Zoli.left(90)
# Zoli.pendown()

szögösszeg = 0
for i in szögek:
    Zoli.left(i)
    Zoli.forward(100)
    szögösszeg +=i

ablak.mainloop()
szögszum = str(szögösszeg)
print(f"A kalóz az eredeti helyzetéhez képest {szögszum} fokkal fordult el")

#3.8.9
#18 nyolcszög

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
# Zoli.shape("turtle")
Zoli.color("orange")
Zoli.pensize(3)
Zoli.speed(1)
Zoli.penup()
Zoli.right(90)
Zoli.forward(300)
Zoli.left(90)
Zoli.pendown()
Zoli.stamp()

for i in range(18):
    # Zoli.stamp()
    Zoli.forward(100)
    Zoli.left(360/18)

ablak.mainloop()
fordul = int(360 / 18)

print(f"A szabályos 18 szög rajzolása során a teknős {fordul} fokot fordul")


#3.8.11 Pentagram

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.color("red")
Eszti.left(36)
Eszti.pensize(5)
Eszti.hideturtle()


for i in range(5):
    Eszti.speed(0)
    Eszti.forward(300)
    Eszti.left(144)

Eszti.left(-36)
Eszti.showturtle()
ablak.mainloop()


#3.8.12 óralap

import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.speed(3)
Eszti.shape("turtle")
Eszti.penup()
Eszti.color("blue")
Eszti.stamp()


for i in range(12):
    Eszti.forward(150)
    Eszti.pendown()
    Eszti.pensize(3)
    Eszti.forward(10)
    Eszti.penup()
    Eszti.forward(30)
    Eszti.pendown()
    Eszti.stamp()
    Eszti.penup()
    Eszti.forward(-190)
    Eszti.left(360/12)




ablak.mainloop()


# + 3.8.16 hevenyészett kör a 3.8.12 alapján

import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")
Eszti = turtle.Turtle()
Eszti.speed(0)
Eszti.shape("circle")
Eszti.penup()
Eszti.color("red")
Eszti.stamp()
Eszti.hideturtle()
Eszti.pensize(3)


for i in range(360):
    Eszti.forward(150)
    Eszti.pendown()

    Eszti.forward(1)
    Eszti.penup()
    Eszti.forward(-151)
    Eszti.left(1)




ablak.mainloop()
