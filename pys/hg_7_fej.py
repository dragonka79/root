# 7.5.1 A Collatz sorozat


def sor3np1(n):
    """ Kiírja a 3n+1 sorozatot n-től amíg el nem éri az 1-et. """
    while n != 1:
        print(n, end=', ')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(n, end='.\n')


sor3np1(16)


# 7.7.1. Számjegyek számlálása


def szamjegy_szam(n):
    """  7.7.1 megszámlálja egy szám számjegyeinek a számát.  """
    szamlalo = 0
    while n != 0:
        szamlalo += 1
        n = n // 10
    return szamlalo


print(szamjegy_szam(1009))

# 7.7.2. Nulla és Öt számjegyek számlálása

import sys


def nulla_es_ot_szamjegy_szam(n):
    """  7.7.2 megszámlálja egy szám 0 és 5 számjegyeinek a számát.  """
    if n == 0:
        return 1
    else:
        szamlalo = 0
        while n > 0:
            szamjegy = n % 10
            if szamjegy == 0 or szamjegy == 5:
                szamlalo = szamlalo + 1
            n = n // 10
        return szamlalo


# print(nulla_es_ot_szamjegy_szam(986412))


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def tesztkeszlet_nulla_es_ot_szamjegy_szam():
    """ A 7.7.2 modulhoz tartozó tesztkészlet futtatása.  """
    teszt(nulla_es_ot_szamjegy_szam(0) == 1)
    teszt(nulla_es_ot_szamjegy_szam(1) == 0)
    teszt(nulla_es_ot_szamjegy_szam(1055505) == 6)
    teszt(nulla_es_ot_szamjegy_szam(1986) == 0)


tesztkeszlet_nulla_es_ot_szamjegy_szam()


# 7.10. Számok és hatványai a kettes alapra táblázata

for x in range(13):   # Generálj számokat 0 és 12 között
    print(x, "\t", 2 ** x)


# 7.12. Szorzótábla

def tobbszorosok_kiirasa(n):
    """ Egy n szám többszörösei.  """
    for i in range(1, 7):
        print(n * i, end="    ")
    print()         # új sor kezdése miután az iteráció lefutott.

def szorzotabla_kiiras():
    for i in range(1, 7):
        tobbszorosok_kiirasa(i)


szorzotabla_kiiras()


# 7.15. Ha megtaláltad az első páratlan számot a listában akkor lépj ki és
# írd ki az addig talált páros számokat.

def elso_paratlanig():
    """  Írd ki a lista elemeit az első páratlan számig.  """
    lista = [12, 16, 17, 24, 29]
    for i in lista:
        if i % 2 != 0:
            break
        print(i)
    print("Kész.")


elso_paratlanig()


# 7.16. Számbekérő


def szam_bekero():
    """  Bekér számokat és összeadja őket.  """
    osszeg = 0
    while True:  #ismételd a ciklustörzset újra és újra
        i = input('Adj meg egy számot, ha nem akarsz többet, üss entert: ')
        if i == '':
            break
        osszeg += int(i)
    print('A számok összege amit adtál: ',osszeg)

szam_bekero()


# 7.17.1 Számkitalálósdi a könyv szerint

import random                   # Beszélni fogunk a véletlen számokról...
vel  = random.Random()          # ...a modulok fejezetbe, szóval fel a fejjel.
szam = vel.randrange(1, 1000)   # véletlen szám [1 és 1000) intervallumban.

tippszam = 0
uzenet = ""

while True:
    tipp = int(input(uzenet + "\nTaláld ki az 1 és 1000 közötti számot, amire gondoltam: "))
    tippszam += 1
    if tipp > szam:
        uzenet += str(tipp) + " túl nagy.\n"
    elif tipp < szam:
        uzenet += str(tipp) + " túl kicsi.\n"
    else:
        break

input("\n\nNagyszerű, kitaláltad {0} tipp segítségével!\n\n".format(tippszam))


# 7.17.2 Számkitalálósdi, saját változat

import random


def szamkitalalosdi():
    """   Találj ki egy véletlen számot.  """
    szam = random.randrange(1, 100)
    tippszam = 0
    tipp = int(input("Találd ki az 1 és 100 közötti számot, amire gondoltam: "))
    while True:
        tippszam += 1
        if tipp > szam:
            tipp = int(input(f"{tipp} túl nagy, tippelj tovább: "))
        elif tipp < szam:
            tipp = int(input(f"{tipp} túl kicsi, tippelj tovább: "))
        else:
            break
    input(f"\n\nNagyszerű, kitaláltad {tippszam} tipp segítségével!\n\n")

szamkitalalosdi()


# 7.18. Continue, írd ki a listában lévő összes páros számot egymás alá.

def osszes_paros():
    """  Írd ki a listában lévő összes páros számot egymás alá.  """
    lista = [12, 16, 17, 24, 29, 30]
    for i in lista:
        if i % 2 != 0:
            continue
        print(i)
    print("Kész.")


osszes_paros()



# 7.19. Szorzótábla n = 31-ig. A sorokban az elemek közötti szóközök az elem
#számjegyeinek száma szerint van korrigálva a jobb olvashatóság miatt.


def szamjegy_szam(n):
    """  7.7.1 megszámlálja egy szám számjegyeinek a számát.  """
    szamlalo = 0
    while n != 0:
        szamlalo += 1
        n = n // 10
    return szamlalo

def tobbszorosok_kiirasa(n, magassag):
    """ Egy n szám többszörösei.  """
    for i in range(1, magassag + 1):
        if szamjegy_szam(n * i ) == 1:
            print(n * i, end="    ") #Ha i 1 számjegyből áll, akkor 3 space-t üt.
        elif szamjegy_szam(n * i ) == 2:
            print(n * i, end="   ") #Ha i 2 számjegyből áll, akkor 2 space-t üt.
        elif szamjegy_szam(n * i ) == 3:
            print(n * i, end="  ") #Ha i 3 számjegyből áll, akkor 1 space-t üt.
    print()

def szorzotabla_kiiras(magassag):
    """  Szorzótábla n = 31-ig.   """
    for i in range(1, magassag+1):
        tobbszorosok_kiirasa(i, magassag)


szorzotabla_kiiras(8)



# 7.21. Értékpárban keresés

celebek = [("Brad Pitt", 1963), ("Jack Nicholson", 1937), ("Justin Bieber", 1994)]

def ertekpar_celebek():
    """  Írd ki azok neveit a celeb listából, akik 1980 előtt születtek.  """
    for (nev, ev) in celebek:
        if ev < 1980:
            print(nev)

ertekpar_celebek()


# 7.22. Beágyazott ciklus beágyazott adatokhoz


targy = "Informatika"
hallgatok = [
("Jani", ["Informatika", "Fizika"]),
("Kata", ["Matematika", "Informatika", "Statisztika"]),
("Peti", ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]),
("Andi", ["Információs rendszerek", "Könyvelés", "Közgazdaságtan", "Vállalkozási jog"]),
("Linda", ["Szociológia", "Közgazdaságtan", "Jogi ismeretek", "Statisztika", "Zene"])]

def nevek_kurzusok_szama():
    """  Kiírja a hallgatól nevét és hogy hány kurzust vettek fel.  """
    for (nev, kurzus) in hallgatok:
        print(f"{nev} {len(kurzus)} kurzust vett fel.")
    print("\r")

def hanyan_vettek_fel(targy):
    """  Hányan vették fel az argumentumban szereplő tárgyat.  """
    szamlalo = 0
    for (nev, kurzus) in hallgatok:
        for i in kurzus:
            if i == targy:
                szamlalo += 1
    print(f"A {targy} kurzust {szamlalo} diák vette fel.\n")


nevek_kurzusok_szama()
hanyan_vettek_fel(targy)



# 7.23. Newton módszer a négyzetgyök megtalálásához, saját, felturbózva

import sys
import math

n = 25                 #Ide írd a számot amiből gyököt akarsz vonni

def gyok(n):
    """ n szám négyzetgyöke a Newton módszerrel.  """
    kozelites = n/2.0     # Kezdjük egy alap sejtéssel
    while True:
        jobb = (kozelites + n/kozelites)/2.0
        if abs(kozelites - jobb) < 0.001:
            return jobb
        kozelites = jobb
        # print(jobb)


print(f"""
A(z) {n} Newton-négyzetgyöke:        {gyok(n)}
A(z) {n} négyzetgyöke:               {math.sqrt(n)}
A gyök és a Newton-gyök különbsége: {abs(gyok(n) - math.sqrt(n))}
""")


# 7.26.1 Páratlan számok egy listában

lista = [17, 22, 2, 5, 1, 7, 14, 13]

def paratlan_szamok_szama():
    """   Megszámolja a páratlan számokat egy listában.  """
    szamlalo = 0
    for l in lista:
        if l % 2 == 0:
            continue
        szamlalo += 1
    # print(szamlalo)
    input(f"A páratlan számok száma a listában {szamlalo}.\nNyomj entert és \
a program kilép.")

paratlan_szamok_szama()


# 7.26.2 Páros számok összege egy listában

lista = [17, -22, 2, 5, -4, 1, 7, 14, 13, 8]

def paros_szamok_osszege():
    """   Összeadja a páros számokat egy listában.  """
    osszeg = 0
    for l in lista:
        if l % 2 != 0:
            continue
        osszeg += int(l)
    # print(osszeg)
    input(f"A páros számok összege a listában {osszeg}.\nNyomj entert és \
a program kilép.")

paros_szamok_osszege()


# 7.26.3 Negatív összege egy listában

lista = [17, -22, 2, 5, -4, 8, 7, 14, 0, 13, -1]

def negativ_szamok_osszege():
    """   Összeadja a negatív számokat egy listában.  """
    osszeg = 0
    for l in lista:
        if l >= 0:
            continue
        osszeg += int(l)
    # print(osszeg)
    input(f"A negatív számok összege a listában {osszeg}.\nNyomj entert és \
a program kilép.")

negativ_szamok_osszege()

# 7.26.4 n betűs szavak száma egy listában

lista = [
'három',    # 1
'öt',
'kettő',    # 2
'nyolc',    # 3
'hét',
'bamba'     # 4
]

n = 5
def n_betus_szavak_szama(n):
    """   Megszámolja az n betűs szavakat egy listában.  """
    osszeg = 0
    for l in lista:
        if len(l) != n:
            continue
        osszeg += 1

    # print(szamlalo)
    input(f"Az {n} betűs szavak száma a listában {osszeg}.\nNyomj entert és \
a program kilép.")

n_betus_szavak_szama(n)


# 7.26.5 Az első páros szám előtti számok összege egy listában

import sys

lista = [17, 3, -7, -22, 2, 5]      # 13
teszt0 = [17, 3, -7, -22, 2, 5]     # 13
teszt1 = []                         # üres lista, összeg: 0
teszt2 = [17, 3, -7, 0, 1, 5]       # nulla(páros) van a listában, összeg: 13
teszt3 = [22, 0, 3]                 # első elem páros, összeg: 0
teszt4 = [17, 3, -7, 1, 5]          # nincs páros szám, összeg: 19

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def osszeg_paros_elott(lista):
    """   Összeadja a számokat az első páros számig egy listában.  """
    osszeg = 0
    for l in lista:
        if l % 2 == 0:
            break
        osszeg += l
    return osszeg


def tesztkeszlet_osszeg_paros_elott():
    """ A 7.26.4 modulhoz tartozó tesztkészlet futtatása.  """
    teszt(osszeg_paros_elott(teszt0) == 13)
    teszt(osszeg_paros_elott(teszt1) == 0)
    teszt(osszeg_paros_elott(teszt2) == 13)
    teszt(osszeg_paros_elott(teszt3) == 0)
    teszt(osszeg_paros_elott(teszt4) == 19)

# print(osszeg_paros_elott(teszt4))
tesztkeszlet_osszeg_paros_elott()


# 7.26.6 A szavak száma az első 'nem'-ig (a 'nem' is benne van) egy listában.

import sys

lista = ['igen','igen','igen','nem','igen']   # 4
teszt0 = ['igen','igen','igen']               # 3
teszt1 = []                                   # üres lista: 0
teszt2 = ['nem', 'igen']                      # 1


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def osszeg_nem_ig(lista):
    """Megszámolja a szavakat az első 'nem'-ig egy listában(a 'nem' benne van)."""
    osszeg = 0
    for l in lista:
        if l == 'nem':
            osszeg += 1
            break
        osszeg += 1
    return osszeg


def tesztkeszlet_osszeg_nem_ig():
    """ A 7.26.4 modulhoz tartozó tesztkészlet futtatása.  """
    teszt(osszeg_nem_ig(lista) == 4)
    teszt(osszeg_nem_ig(teszt0) == 3)
    teszt(osszeg_nem_ig(teszt1) == 0)
    teszt(osszeg_nem_ig(teszt2) == 1)


# print(osszeg_nem_ig(lista))
tesztkeszlet_osszeg_nem_ig()



# 7.26.7 Newton módszer a négyzetgyök megtalálásához, jobb-ak kiíratása

import sys
import math

n = 25                 #Ide írd a számot amiből gyököt akarsz vonni

def gyok(n):
    """ n szám négyzetgyöke a Newton módszerrel.  """
    kozelites = n/2.0     # Kezdjük egy alap sejtéssel
    while True:
        jobb = (kozelites + n/kozelites)/2.0
        if abs(kozelites - jobb) < 0.001:
            return jobb
        kozelites = jobb
        print(jobb)

gyok(n)


# 7.26.9 Háromszögszámok


def szamjegy_szam(n):
    """  7.7.1 megszámlálja egy szám számjegyeinek a számát.  """
    szamlalo = 0
    while n != 0:
        szamlalo += 1
        n = n // 10
    return szamlalo


def haromszogszamok(n):
    """ Kiszámolja az első n háromszögszámot.  """
    haromszog = 0
    for i in range(1, n+1):
        haromszog += i
        #Ha i 1 számjegyből áll, akkor 6 space-t üt.
        if szamjegy_szam(i) == 1:
            print(i, '      ', haromszog)
        #Ha i 2 számjegyből áll, akkor 5 space-t üt.
        elif szamjegy_szam(i) == 2:
            print(i, '     ', haromszog)
        #Ha i 3 számjegyből áll, akkor 4 space-t üt.
        elif szamjegy_szam(i) == 3:
            print(i, '    ', haromszog)


haromszogszamok(100)



# 7.26.10. Prímteszt, egy adott n szám prím-e?


import math
import sys


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def prim_e(n):
    """ Teszteli az n számot, hogy prím-e.  """
    i = 2

    if n == 1:
        return False
    if n == 2:
        return True

    while i <= int(math.sqrt(n)):
        if n % i == 0:
            return (i, False)  # Melyik a legkisebb osztója + False
            # return False         # A teszt miatt ez kell és nem a felette lévő
            break
        else:
            i+=1
    return True


def tesztkeszlet_prim_e():
    """ A 7.26.10 modulhoz tartozó tesztkészlet futtatása.  """
    teszt(prim_e(11) == True)
    teszt(prim_e(35) == False)
    teszt(prim_e(19981121) == False)




print(prim_e(19790130))
# tesztkeszlet_prim_e()




# 7.26.11 A részeg kalauz útvonalai

import turtle


ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.color("orange")
Zoli.pensize(1)
Zoli.speed(1)
Zoli.hideturtle()

kaloz_mozgas = [(160, 200), (-43, 100), (270, 80), (-43, 120)]
kaloz_mozgas_negyzet = [(90, 200), (90, 200), (90, 200), (90, 200)]
kaloz_mozgas_otszog = [(72, 200)]


def reszeg_kaloz():
    """   A részeg kalauz útvonala.   """
    for (forog, megy) in kaloz_mozgas:
        Zoli.right(forog)
        Zoli.forward(megy)


def reszeg_kaloz_otszog():
    """   A részeg kalauz szabályos ötszög alakú útvonala.   """
    for i in range(5):
        for (forog, megy) in kaloz_mozgas_otszog:
            Zoli.right(forog)
            Zoli.forward(megy)


# reszeg_kaloz()
reszeg_kaloz_otszog()


ablak.mainloop()


# 7.26.12 Házikó rajzolása

import turtle
import math

ablak = turtle.Screen()
ablak.bgcolor("black")
Zoli = turtle.Turtle()
Zoli.color("orange")
Zoli.pensize(1)
Zoli.speed(3)
Zoli.hideturtle()


i = 100 * math.sqrt(2)
k = 100 * math.sqrt(3)
haz = [(-90,100),(-45,100),(-90,100),(-45,100),(-90,i),(-145,k),(145,i),(145,k)]



def haz_forma():
    """   Ház.   """
    for (forog, megy) in haz:
        Zoli.right(forog)
        Zoli.forward(megy)


haz_forma()

ablak.mainloop()


# 7.26.14. Igazi számjegy számlálás

import sys


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def igazi_szamjegy_szam(n):
    """ Megszámolja egy számban a számjegyeket.  """
    szamlalo = 0
    k = abs(n)
    while True:
        if k // 10 == 0:
            szamlalo += 1
            return szamlalo
            break
        else:
            szamlalo += 1
            k = k // 10
    return szamlalo


def tesztkeszlet_igazi_szamjegy_szam():
    """ A 7.26.14 modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(igazi_szamjegy_szam(0) == 1)
    teszt(igazi_szamjegy_szam(-12345) == 5)
    teszt(igazi_szamjegy_szam(12345) == 5)
    teszt(igazi_szamjegy_szam(9) == 1)

# print(szamjegy_szam(0))
tesztkeszlet_igazi_szamjegy_szam()


# 7.26.15. Páros számjegy számlálás

import sys


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def paros_szamjegy_szam(n):
    """ Megszámolja egy számban a páros számjegyeket. """
    szamlalo = 0
    k = abs(n)
    while True:
        l = k % 10
        if k // 10 == 0 and l % 2 == 0:
            szamlalo += 1
            return szamlalo
            break

        elif k // 10 == 0 and l % 2 != 0:
            return szamlalo
            break

        elif k // 10 != 0 and l % 2 == 0:
            szamlalo += 1
            k = k // 10

        elif k // 10 != 0 and l % 2 != 0:
            k = k // 10


def tesztkeszlet_paros_szamjegy_szam():
    """ A 7.26.15 modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(paros_szamjegy_szam(123456) == 3)
    teszt(paros_szamjegy_szam(-2468) == 4)
    teszt(paros_szamjegy_szam(1357) == 0)
    teszt(paros_szamjegy_szam(0) == 1)

# print(paros_szamjegy_szam(9))
tesztkeszlet_paros_szamjegy_szam()


# 7.26.16. Listában szereplő számok négyzeteinek összege

import sys


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

xs = [2, 3, 4]

def negyzetosszeg(xs):
    """ Összeadja egy lista elemeinek négyzeteit """
    nosszeg = 0
    for i in xs:
        nosszeg += i ** 2
    return nosszeg


def tesztkeszlet_negyzetosszeg(xs):
    """ A 7.26.15 modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(negyzetosszeg([2, 3, 4]) == 29)
    teszt(negyzetosszeg([]) == 0)
    teszt(negyzetosszeg([2, -3, 4]) == 29)
    teszt(negyzetosszeg([1, -1, 1]) == 3)

# print(negyzetosszeg(xs))
tesztkeszlet_negyzetosszeg(xs)
