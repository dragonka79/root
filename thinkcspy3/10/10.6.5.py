import turtle # D0 közlekedési lámpává válik.
import time
turtle.setup(400,500)
ablak = turtle.Screen()
ablak.title("D0 közlekedési lámpává válik.")
ablak.bgcolor("lightgreen")

G1 = turtle.Turtle() # Zöld lámpa teknőc
G1.hideturtle()
O2 = turtle.Turtle() # Narancs lámpa teknőc
O2.hideturtle()
R3 = turtle.Turtle() # Piros lámpa teknőc
R3.hideturtle()


def doboz_rajzolas():
    """ Egy csinos doboz rajzolása a közlekedési lámpa számára """
    D0 = turtle.Turtle() # Doboz teknőc
    D0.speed(0)
    D0.hideturtle()
    D0.pensize(3)
    D0.color("black", "darkgrey")
    D0.begin_fill()
    D0.right(90)
    D0.penup()
    D0.forward(80)
    D0.left(90)
    D0.pendown()
    D0.forward(80)
    D0.left(90)
    D0.forward(200)
    D0.circle(40, 180)
    D0.forward(200)
    D0.left(90)
    D0.end_fill()

def zold_lampa():
    G1.speed(0)
    G1.penup()
    G1.right(90)
    G1.forward(80)
    G1.left(90)
    G1.forward(40)
    G1.left(90)
    G1.forward(50)
    G1.showturtle()
    G1.shape("circle")
    G1.shapesize(3)
    G1.fillcolor("lightgreen")

def orange_lampa():
    O2.speed(0)
    O2.penup()
    O2.right(90)
    O2.forward(80)
    O2.left(90)
    O2.forward(40)
    O2.left(90)
    O2.forward(120)
    O2.showturtle()
    O2.shape("circle")
    O2.shapesize(3)
    O2.fillcolor("#F6A761")

def red_lampa():
    R3.speed(0)
    R3.penup()
    R3.right(90)
    R3.forward(80)
    R3.left(90)
    R3.forward(40)
    R3.left(90)
    R3.forward(190)
    R3.showturtle()
    R3.shape("circle")
    R3.shapesize(3)
    R3.fillcolor("#FFA8A8")

allapot_sorszam = 0

def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0: # Átmenet a 1. állapotból az 2. állapotba
        G1.fillcolor("#00994C") # zöld
        R3.fillcolor("#FFA8A8") # halvány piros
        allapot_sorszam = 1
        ablak.ontimer(allapot_automata_esemenykezeloje, 3000)
    elif allapot_sorszam == 1: # Átmenet az 2. állapotból a 3. állapotba
        O2.fillcolor("#F27100") # narancs
        allapot_sorszam = 2
        ablak.ontimer(allapot_automata_esemenykezeloje, 1000)
    elif allapot_sorszam == 2: # Átmenet a 3. állapotból az 4. állapotba
        G1.fillcolor("lightgreen")
        allapot_sorszam = 3
        ablak.ontimer(allapot_automata_esemenykezeloje, 1000)
    else: # Átmenet a 4. állapotból az 0. állapotba
        O2.fillcolor("#F6A761")
        R3.fillcolor("red")
        allapot_sorszam = 0
        ablak.ontimer(allapot_automata_esemenykezeloje, 2000)
    # print(allapot_sorszam)

doboz_rajzolas()
zold_lampa()
orange_lampa()
red_lampa()
time.sleep(1.5) # s másodpercig áll a program, itt a zöld lámpa 1.5 másodperc után vált

allapot_automata_esemenykezeloje()
ablak.mainloop()