import turtle # Eszti közlekedési lámpává válik.
turtle.setup(400,500)
k = 3
ablak = turtle.Screen()
ablak.title("Eszti közlekedési lámpává válik.")
ablak.bgcolor("lightgreen")
Eszti = turtle.Turtle()
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
Eszti.shapesize(k)
Eszti.fillcolor("green")

allapot_sorszam = 0

def allapot_automata_esemenykezeloje():
    global allapot_sorszam   
    if allapot_sorszam == 0: # Átmenet a 0. állapotból az 1. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        allapot_sorszam = 1
    elif allapot_sorszam == 1: # Átmenet az 1. állapotból a 2. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("red")
        allapot_sorszam = 2
    else: # Átmenet a 2. állapotból az 0. állapotba
        Eszti.back(140)
        Eszti.fillcolor("green")
        allapot_sorszam = 0
    # print(allapot_sorszam)
def B_allapot_automata_esemenykezeloje():
        Eszti.fillcolor("blue")
def R_allapot_automata_esemenykezeloje():
        Eszti.fillcolor("red")
def G_allapot_automata_esemenykezeloje():
        Eszti.fillcolor("green")        
def shapesizemodminus():
        global k
        if k >1:
                k -= 1
        Eszti.shapesize(k)
        print(k)

def shapesizemodplus():
        global k
        if k <20:
                k += 1
        Eszti.shapesize(k)
        print(k)

# Az eseménykezelőt a space billentyűhöz kötjük
ablak.onkey(allapot_automata_esemenykezeloje, "space")
ablak.onkey(G_allapot_automata_esemenykezeloje, "G")
ablak.onkey(R_allapot_automata_esemenykezeloje, "R")
ablak.onkey(B_allapot_automata_esemenykezeloje, "B")
ablak.onkey(shapesizemodminus, "-")
ablak.onkey(shapesizemodplus, "+")
ablak.listen() # Események figyelése
ablak.mainloop()