import turtle

def ablak_keszites(szin, ablaknev):
    """
    Egy ablak elkészítése, és a háttérszín, valamint az ablaknév beállítása.
    Visszatérési érték: az új ablak.
    """
    a = turtle.Screen()
    a.bgcolor(szin)
    a.title(ablaknev)
    return a

def teknoc_keszites(szin, tm):
    """
    Létrehoz egy teknőcöt, és beállítja az általa használt toll
    színét és méretét.
    Visszatérési érték: az új teknőc.
    """
    t = turtle.Turtle()
    t.color(szin)
    t.pensize(tm)
    return t

a = ablak_keszites("lightgreen", "Eszti és Sanyi táncol")
Eszti = teknoc_keszites("hotpink", 5)
Sanyi = teknoc_keszites("black", 1)
David = teknoc_keszites("yellow", 2)

a.mainloop()