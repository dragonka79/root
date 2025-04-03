# 10.1 Billentyű leütés események

import turtle

turtle.setup(400, 500)   # Az ablak méretének beállítása
ablak = turtle.Screen()  # Az ablak referenciájának lekérése
ablak.title("Billentyű leütés kezelése!")  # Az ablaknév módosítása
ablak.bgcolor("lightgreen")  # Háttér színének beállítása
Eszti = turtle.Turtle()  # A kedvenc teknőcünk elkészítése

# A következő függvények az eseménykezelőink
def ek1():
    Eszti.forward(30)

def ek2():
    Eszti.left(45)

def ek3():
    Eszti.right(45)

def ek4():
    ablak.bye()  # A teknőc ablak bezárása

# Ezek a sorok rendelik össze a billentyű leütés eseményeket
#  az általunk definiált eseménykezelő függvényekkel
ablak.onkey(ek1, "space") # Ha leütöm a space-t akkor az ek1 fv aktivizálódik.
ablak.onkey(ek2, "Left")
ablak.onkey(ek3, "Right")
ablak.onkey(ek4, "q")

# Most megkérjük az ablakot, hogy kezdje el figyelni az eseményeket.
# Ha bármelyik általunk figyelt billentyűt lenyomja valaki, akkor
#  a hozzá tartozó eseménykezelő meghívásra kerül.
ablak.listen()
ablak.mainloop()


# 10.2.1 Egér események, egy teknőc mozog

import turtle

turtle.setup(2000,3000)
ablak = turtle.Screen()
ablak.title("Ablakon belüli kattintások kezelése")
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.speed(9)
# Eszti.penup()
Eszti.color("purple")
Eszti.pensize(3)
Eszti.shape("circle")

def ek1(x, y):
    """  Oda viszi a kurzort ahova kattintok, s közben vonalat húz.  """
    ablak.title("Kattintás koordinátái: {0}, {1}".format(x, y))
    Eszti.goto(x, y)

ablak.onclick(ek1)  # Összerendeljük a kattintás eseményt az eseménykezelővel
ablak.mainloop()


# 10.2.2 Egér események, kettő teknőc, az mozog amelyikre rákattintok

import turtle

turtle.setup(2000, 3000)       # Az ablak méretének beállítása
ablak = turtle.Screen()      # Az ablak referenciájának lekérése
ablak.title("Kattintások kezelése!")  # Az ablaknév módosítása
ablak.bgcolor("lightgreen")  # Háttér színének beállítása
Eszti = turtle.Turtle()      # Két teknőc készítése
Eszti.color("purple")
Eszti.shape("circle")
Sanyi = turtle.Turtle()
Sanyi.color("blue")
Sanyi.penup()
Sanyi.forward(100)           # Teknőcök szétválasztása
Sanyi.pendown()
Sanyi.shape("circle")


def Eszti_esemenykezeloje(x, y):
    ablak.title("Eszti kattintásának koordinátái: {0}, {1}".format(x, y))
    Eszti.left(42)
    Eszti.forward(150)
    Eszti.right(-33)
    Eszti.forward(120)

def Sanyi_esemenykezeloje(x, y):
    ablak.title("Sanyi kattintásának koordinátái: {0}, {1}".format(x, y))
    Sanyi.right(84)
    Sanyi.forward(180)

# Ha Esztire kattintok, Eszti mozog
Eszti.onclick(Eszti_esemenykezeloje)
# Ha Sanyira kattintok, Sanyi mozog
Sanyi.onclick(Sanyi_esemenykezeloje)

ablak.mainloop()


# 10.3.1 Időzített, automatikus események

import turtle

turtle.setup(400,500)
ablak = turtle.Screen()
ablak.title("Időzítő használata")
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("purple")
Eszti.pensize(3)

def ek1():
    Eszti.forward(100)
    Eszti.left(56)

#Időzítő, a program indulása után 2000 milisec-kel az ek1 függvény elindul.
ablak.ontimer(ek1, 2000)

ablak.mainloop()


# 10.3.2 Időzített, automatikus események

import turtle

turtle.setup(400,500)
ablak = turtle.Screen()
ablak.title("Időzítő használata")
ablak.bgcolor("lightgreen")

Eszti = turtle.Turtle()
Eszti.color("purple")

def ek1():
    """   ek1 elindul aztán 60 msec után újra és újra.  """
    Eszti.forward(100)
    Eszti.left(56)
    ablak.ontimer(ek1, 60)

ek1()
ablak.mainloop()

# 10.4. Egy példa: állapotautomata

import turtle           # Eszti közlekedési lámpává válik.

turtle.setup(400,700)
ablak = turtle.Screen()
ablak.title("Eszti közlekedési lámpává válik.")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.speed(1)


def doboz_rajzolas():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Eszti.pensize(3)
    Eszti.color("black", "darkgrey")
    Eszti.begin_fill()
    Eszti.forward(80)
    Eszti.left(90)
    Eszti.forward(200)
    Eszti.circle(40, 180)
    Eszti.forward(200)
    Eszti.left(90)
    Eszti.end_fill()


doboz_rajzolas()

Eszti.penup()
# Eszti pozícionálása oda, ahol a zöld lámpának kell lennie
Eszti.forward(40)
Eszti.left(90)
Eszti.forward(50)
# Esztit egy nagy zöld körré alakítjuk át
Eszti.shape("circle")
Eszti.shapesize(3)
Eszti.fillcolor("green")

# A közlekedési lámpa egyfajta állapotautomata, három állapottal:
#  zölddel, sárgával és pirossal. Az állapotokat rendre
#  0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam # A 4 sorral fenti változóra utal, nem hoz létre újat.
    if allapot_sorszam == 0:       # Átmenet a 0. állapotból az 1. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        allapot_sorszam = 1
    elif allapot_sorszam == 1:     # Átmenet az 1. állapotból a 2. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("red")
        allapot_sorszam = 2
    else:                          # Átmenet a 2. állapotból az 0. állapotba
        Eszti.back(140)
        Eszti.fillcolor("green")
        allapot_sorszam = 0

# Az eseménykezelőt a space billentyűhöz kötjük
ablak.onkey(allapot_automata_esemenykezeloje, "space")

ablak.listen()                      # Események figyelése
ablak.mainloop()



# 10.6.1

import turtle

turtle.setup(2000, 3000)   # Az ablak méretének beállítása
ablak = turtle.Screen()  # Az ablak referenciájának lekérése
ablak.title("Billentyű leütés kezelése!")  # Az ablaknév módosítása
ablak.bgcolor("lightgreen")  # Háttér színének beállítása
Eszti = turtle.Turtle()  # A kedvenc teknőcünk elkészítése
i = 1
# A következő függvények az eseménykezelőink
def ek1():
    Eszti.forward(30)

def ek2():
    Eszti.left(45)

def ek3():
    Eszti.right(45)

def ek4():
    ablak.bye()  # A teknőc ablak bezárása

def ek5():
    """  Eszti színe piros lesz.   """
    ablak.title("Eszti színe: {0}".format('red'))
    Eszti.color('red')

def ek6():
    """  Eszti színe zöld lesz.   """
    ablak.title("Eszti színe: {0}".format('green'))
    Eszti.color('green')

def ek7():
    """  Eszti színe kék lesz.   """
    ablak.title("Eszti színe: {0}".format('blue'))
    Eszti.color('blue')

def ek8():
    """  Eszti tollvastagsága nő, max 20 értékig.  """
    global i
    ablak.title("Eszti mérete: {0}".format(i))
    if i <20:
        i += 1
        Eszti.pensize(i)

def ek9():
    """  Eszti tollvastagsága csökken, min 1 értékig.  """
    global i
    ablak.title("Eszti mérete: {0}".format(i))
    if i >1:
        i -= 1
        Eszti.pensize(i)

def ek10():
    """ Eszti alakja kör lesz.   """
    ablak.title("Eszti alakja: {0}".format('circle'))
    Eszti.shape('circle')

def ek11():
    """ Eszti alakja a klasszikus nyíl lesz.   """
    ablak.title("Eszti alakja: {0}".format('classic'))
    Eszti.shape('classic')

# Ezek a sorok rendelik össze a billentyű leütés eseményeket
#  az általunk definiált eseménykezelő függvényekkel
ablak.onkey(ek1, "space") # Ha leütöm a space-t akkor az ek1 fv aktivizálódik.
ablak.onkey(ek2, "Left")
ablak.onkey(ek3, "Right")
ablak.onkey(ek4, "q")
ablak.onkey(ek5, "r")
ablak.onkey(ek6, "g")
ablak.onkey(ek7, "b")
ablak.onkey(ek8, 'p')
ablak.onkey(ek9, 'm')
ablak.onkey(ek10, 'c')
ablak.onkey(ek11, 'a')

# Most megkérjük az ablakot, hogy kezdje el figyelni az eseményeket.
# Ha bármelyik általunk figyelt billentyűt lenyomja valaki, akkor
#  a hozzá tartozó eseménykezelő meghívásra kerül.
ablak.listen()
ablak.mainloop()

# 10.6.2.


import turtle           # Eszti közlekedési lámpává válik, automata változat.

turtle.setup(400,700)
ablak = turtle.Screen()
ablak.title("Eszti közlekedési lámpává válik.")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
Eszti.speed(1)


def doboz_rajzolas():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    Eszti.pensize(3)
    Eszti.color("black", "darkgrey")
    Eszti.begin_fill()
    Eszti.forward(80)
    Eszti.left(90)
    Eszti.forward(200)
    Eszti.circle(40, 180)
    Eszti.forward(200)
    Eszti.left(90)
    Eszti.end_fill()


doboz_rajzolas()

Eszti.penup()
# Eszti pozícionálása oda, ahol a zöld lámpának kell lennie
Eszti.forward(40)
Eszti.left(90)
Eszti.forward(50)
# # Esztit egy nagy zöld körré alakítjuk át
# Eszti.shape("circle")
# Eszti.shapesize(3)
# Eszti.fillcolor("green")

# A közlekedési lámpa egyfajta állapotautomata, három állapottal:
#  zölddel, sárgával és pirossal. Az állapotokat rendre
#  0, 1, 2 számokkal írjuk le.
# Az állapotváltásnál Eszti helyzetét és színét változtatjuk meg.

# Ez a változó hordozza az aktuális állapotot
allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam # A 4 sorral fenti változóra utal, nem hoz létre újat.
    if allapot_sorszam == 0:        # Eszti zöld körré változik
        Eszti.shape("circle")
        Eszti.shapesize(3)
        Eszti.fillcolor("green")
        allapot_sorszam = 1
    elif allapot_sorszam == 1:       # Átmenet a 0. állapotból az 1. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        allapot_sorszam = 2
    elif allapot_sorszam == 2:     # Átmenet az 1. állapotból a 2. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("red")
        allapot_sorszam = 3
    else:                          # Átmenet a 2. állapotból az 0. állapotba
        Eszti.back(140)
        Eszti.fillcolor("green")
        allapot_sorszam = 1
    ablak.ontimer(allapot_automata_esemenykezeloje, 1000)

# ablak.ontimer(allapot_automata_esemenykezeloje, 1000)
allapot_automata_esemenykezeloje()
ablak.mainloop()


# 10.6.3.Közlekedési lámpa 3 teknőccel


import turtle

turtle.setup(400,700)
ablak = turtle.Screen()
ablak.title("Lámpa 3 teknőccel.")
ablak.bgcolor("lightgreen")
Sanyi = turtle.Turtle()
Peti = turtle.Turtle()
Zoli = turtle.Turtle()
Sanyi.hideturtle()
Peti.hideturtle()
Zoli.hideturtle()
Sanyi.speed(0)
Peti.speed(0)
Zoli.speed(0)


def doboz_rajzolas():
    """ Lámpa rajzolása Sanyival + a 3 teknőc mint lámpa """
    Sanyi.pensize(3)
    Sanyi.color("black", "black")
    Sanyi.begin_fill()
    Sanyi.forward(80)
    Sanyi.left(90)
    Sanyi.forward(200)
    Sanyi.circle(40, 180)
    Sanyi.forward(200)
    Sanyi.left(90)
    Sanyi.end_fill()
    Sanyi.penup()
    Sanyi.forward(40)
    Sanyi.left(90)
    Sanyi.forward(50)
    Sanyi.shape("circle")
    Sanyi.shapesize(3)
    Sanyi.fillcolor("green")
    Peti.forward(40)
    Peti.left(90)
    Peti.forward(120)
    Peti.shape("circle")
    Peti.shapesize(3)
    Peti.fillcolor("orange")
    Zoli.forward(40)
    Zoli.left(90)
    Zoli.forward(190)
    Zoli.shape("circle")
    Zoli.shapesize(3)
    Zoli.fillcolor("red")
doboz_rajzolas()

allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:
        Sanyi.showturtle()
        allapot_sorszam = 1
    elif allapot_sorszam == 1:
        Sanyi.hideturtle()
        Peti.showturtle()
        allapot_sorszam = 2
    elif allapot_sorszam == 2:
        Peti.hideturtle()
        Zoli.showturtle()
        allapot_sorszam = 3
    else:
        Zoli.hideturtle()
        Sanyi.showturtle()
        allapot_sorszam = 1
    ablak.ontimer(allapot_automata_esemenykezeloje, 1500)

allapot_automata_esemenykezeloje()
ablak.mainloop()


# 10.6.4.Közlekedési lámpa 3 teknőccel, mélyeb színekkel mikor a lámpa kialszik.


import turtle

turtle.setup(400,700)
ablak = turtle.Screen()
ablak.title("Lámpa 3 teknőccel.")
ablak.bgcolor("lightgreen")
Sanyi = turtle.Turtle()
Peti = turtle.Turtle()
Zoli = turtle.Turtle()
Sanyi.hideturtle()
Peti.hideturtle()
Zoli.hideturtle()
Sanyi.speed(0)
Peti.speed(0)
Zoli.speed(0)


def doboz_rajzolas():
    """ Lámpa rajzolása Sanyival + a 3 teknőc mint lámpa """
    Sanyi.pensize(3)
    Sanyi.color("black", "black")
    Sanyi.begin_fill()
    Sanyi.forward(80)
    Sanyi.left(90)
    Sanyi.forward(200)
    Sanyi.circle(40, 180)
    Sanyi.forward(200)
    Sanyi.left(90)
    Sanyi.end_fill()
    Sanyi.penup()
    Sanyi.forward(40)
    Sanyi.left(90)
    Sanyi.forward(50)
    Sanyi.shape("circle")
    Sanyi.shapesize(3)
    Sanyi.fillcolor('#01f502')
    Peti.forward(40)
    Peti.left(90)
    Peti.forward(120)
    Peti.shape("circle")
    Peti.shapesize(3)
    Peti.fillcolor('#feab02')
    Zoli.forward(40)
    Zoli.left(90)
    Zoli.forward(190)
    Zoli.shape("circle")
    Zoli.shapesize(3)
    Zoli.fillcolor('#ff0102')
doboz_rajzolas()

allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:
        Sanyi.showturtle()
        Sanyi.fillcolor('#01f502')
        allapot_sorszam = 1
    elif allapot_sorszam == 1:
        Sanyi.fillcolor('#014402')
        Peti.showturtle()
        Peti.fillcolor('#feab02')
        allapot_sorszam = 2
    elif allapot_sorszam == 2:
        Peti.fillcolor('#ca4302')
        Zoli.showturtle()
        Zoli.fillcolor('#ff0102')
        allapot_sorszam = 3
    elif allapot_sorszam == 3:
        Zoli.fillcolor('#690009')
        Sanyi.fillcolor('#01f502')
        allapot_sorszam = 1

    ablak.ontimer(allapot_automata_esemenykezeloje, 1000)

allapot_automata_esemenykezeloje()
ablak.mainloop()


# 10.6.5.Közlekedési lámpa 4 állapottal.


import turtle

turtle.setup(400,700)
ablak = turtle.Screen()
ablak.title("Lámpa 3 teknőccel.")
ablak.bgcolor("lightgreen")
Sanyi = turtle.Turtle()
Peti = turtle.Turtle()
Zoli = turtle.Turtle()
Sanyi.hideturtle()
Peti.hideturtle()
Zoli.hideturtle()
Sanyi.speed(0)
Peti.speed(0)
Zoli.speed(0)


def doboz_rajzolas():
    """ Lámpa rajzolása Sanyival + a 3 teknőc mint lámpa """
    Sanyi.pensize(3)
    Sanyi.color("black", "black")
    Sanyi.begin_fill()
    Sanyi.forward(80)
    Sanyi.left(90)
    Sanyi.forward(200)
    Sanyi.circle(40, 180)
    Sanyi.forward(200)
    Sanyi.left(90)
    Sanyi.end_fill()
    Sanyi.penup()
    Sanyi.forward(40)
    Sanyi.left(90)
    Sanyi.forward(50)
    Sanyi.shape("circle")
    Sanyi.shapesize(3)
    Sanyi.fillcolor('#01f502')
    Peti.forward(40)
    Peti.left(90)
    Peti.forward(120)
    Peti.shape("circle")
    Peti.shapesize(3)
    Peti.fillcolor('#feab02')
    Zoli.forward(40)
    Zoli.left(90)
    Zoli.forward(190)
    Zoli.shape("circle")
    Zoli.shapesize(3)
    Zoli.fillcolor('#ff0102')
doboz_rajzolas()

allapot_sorszam = 0


def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0:
        Sanyi.showturtle()
        Sanyi.fillcolor('#01f502') #világos zöld
        allapot_sorszam = 1
        ablak.ontimer(allapot_automata_esemenykezeloje, 3000)
    elif allapot_sorszam == 1:
        Sanyi.fillcolor('#01f502') #világos zöld
        Peti.showturtle()
        Peti.fillcolor('#feab02') #világos narancs
        allapot_sorszam = 2
        ablak.ontimer(allapot_automata_esemenykezeloje, 1000)
    elif allapot_sorszam == 2:
        Sanyi.fillcolor('#014402') #sötétzöld
        Peti.showturtle()
        Peti.fillcolor('#feab02') #világos narancs
        allapot_sorszam = 3
        ablak.ontimer(allapot_automata_esemenykezeloje, 1000)
    elif allapot_sorszam == 3:
        Peti.fillcolor('#ca4302') #sötét narancs
        Zoli.showturtle()
        Zoli.fillcolor('#ff0102') #vörös
        allapot_sorszam = 4
        ablak.ontimer(allapot_automata_esemenykezeloje, 2000)
    elif allapot_sorszam == 4:
        Zoli.fillcolor('#690009') # sötét vörös
        Sanyi.fillcolor('#01f502') #világos zöld
        allapot_sorszam = 1
        ablak.ontimer(allapot_automata_esemenykezeloje, 3000)

allapot_automata_esemenykezeloje()

ablak.mainloop()
