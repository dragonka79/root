# 18.1. Fraktálok rajzolása. Koch fraktál zárt alakzatban.
# Ugyanaz mint a 18.8.1 feladat aka Koch hópehely

import turtle


ablak = turtle.Screen()
ablak.bgcolor("green")
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.forward(-300)
t.left(90)
t.forward(200)
t.left(-90)
t.pendown()
t.pensize(1)
t.speed(0)


def koch(t, rend, meret):
    """
       Készíts egy t teknőst és rajzolj egy megadott 'rendű' és 'méretű'
       Koch fraktált. Hagyjuk a teknőst ugyanabban az irányban.
    """

    if rend == 0:          # Alapesetben csak egy egyenes
        t.forward(meret)
    else:
        for szog in [60, -120, 60, 0]:
           koch(t, rend-1, meret/3)
           t.left(szog)

for i in range(3):
    koch(t, 4, 700)
    t.right(120)
ablak.mainloop()

# 18.3.1 Rekurzív listák, beágyazott lista elemeinek összege

def rek_szum(beagyazott_lista):
    ossz = 0
    for elem in beagyazott_lista:
        if type(elem) == type([]): # ha az elem egy lista
            ossz += rek_szum(elem) # meghívja a rek_szumot a beágy. listára
            # print('osszrek:', ossz)
        else:
            ossz += elem
            # print('elem: ', elem)
            # print('ossz :', ossz)
    return ossz

lista = [1, [2, 3, [7, 8], [9, 10]]]
print(rek_szum(lista))

# 18.3.2 Rekurzív listák, beágyazott lista legnagyobb értéke

from egyseg_teszt import teszt


def rek_max(nsx):
    """
      Keresd meg a maximumot rekurzív módon
      egy beágyazott listában.
      Előfeltétel: A listák vagy részlisták nem üresek.
    """
    legnagyobb = None
    elso_alk = True
    for e in nsx:
        if type(e) == type([]):
            ert = rek_max(e)
        else:
            ert = e

        if elso_alk or ert > legnagyobb:
            legnagyobb = ert
            elso_alk = False

    return legnagyobb

teszt(rek_max([2, 9, [1, 13], 8, 6]) == 13)
teszt(rek_max([2, [[100, 7], 90], [1, 13], 8, 6]) == 100)
teszt(rek_max([[[13, 7], 90], 2, [1, 100], 8, 6]) == 100)
teszt(rek_max(["jancsi", ["sanyi", "bence"]]) == "sanyi")

# 18.4. Esettanulmány: Fibbonacci-számok

import time

def fib(n):
    if n<= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

t0 = time.clock()
n = 35
eredmeny = fib(n)
t1 = time.clock()

print("fib({0}) = {1}, ({2:.2f} masodperc)".format(n, eredmeny, t1-t0))
