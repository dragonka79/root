import turtle # Eszti közlekedési lámpává válik.
import time
s = int(1.5)
turtle.setup(400,500)
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
Eszti.shapesize(3)
Eszti.fillcolor("green")
time.sleep(s) # s másodpercig áll a program, itt a zöld lámpa s idő után vált


allapot_sorszam = 0

def allapot_automata_esemenykezeloje():
    global allapot_sorszam
    if allapot_sorszam == 0: # Átmenet a 1. állapotból az 2. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("orange")
        allapot_sorszam = 1
    elif allapot_sorszam == 1: # Átmenet az 2. állapotból a 3. állapotba
        Eszti.forward(70)
        Eszti.fillcolor("red")
        allapot_sorszam = 2
    else: # Átmenet a 3. állapotból az 0. állapotba
        Eszti.back(140)
        Eszti.fillcolor("green")
        allapot_sorszam = 0
    ablak.ontimer(allapot_automata_esemenykezeloje, s * 1000)
    # print(allapot_sorszam)
        

allapot_automata_esemenykezeloje()
ablak.mainloop()