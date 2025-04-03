# 12.1.1. Véletlen számok. Egészek.

import random

# Létrehoz egy fekete doboz objektumot, amely véletlen számokat generál.
# Ez nem igazi randomszám generátor, lásd 12.2 később
rng = random.Random()
# Az 1, 4, 7, 10, 13, 16, 19 számok közül egyet véletlenszerűen kiválaszt.
# 1 = start; 20  stop; 3 = step
r_paratlan = rng.randrange(1, 20, 3)
print(r_paratlan)

# 12.1.1. Véletlen számok [0,1) között.

r_random = rng.random()
print(r_random)

# 12.1.3. Legenerálja az első 52 egész számot (mint pl egy kártyapakli) és
# összekeveri

kartyak = list(range(52))
print(kartyak)
rng.shuffle(kartyak)
print(kartyak)

# 12.1.1.1. Ismételhetőség és tesztelés

import random

# Ad egy kezdőértéket a random doboznak és ezzel mindig ugyanazt a random számot
# adja vissza -> nem igazi, pszeudo- random generátor, tesztelésnél jó, de
# ennél jobb a 12.1.1.2
drng = random.Random(123)
r_random = drng.randrange(1, 200)
print(r_random)


# 12.1.1.2. Ismételhetőség és tesztelés, igazi random generátor

r2_random = random.randrange(1, 200)
print(r2_random)


# 12.1.2.1. Random függvény, amely n darab random egész számot generál
# Ismétlődés nincs kizárva


import random

def random_egeszek(szam, also_hatar, felso_hatar):
    """ Random függvény, amely n darab random egész számot generál. """
    rng = random.Random()
    eredmeny = []
    for i in range(szam):
        eredmeny.append(rng.randrange(also_hatar, felso_hatar))
    return eredmeny

print(random_egeszek(5, 1, 13))


# 12.1.2.2. Random függvény, amely n darab random egész számot generál
# Ismétlődés kizárva. Random vs shuffle. "Kever és szeletel". A hibája az, hogy
# előre legenerálja a listát így feleslegesen erőforrást foglal.

import random

xs = list(range(1, 13)) # Létrehozunk egy listát 1..12-ig
rng = random.Random()   # Készítünk egy véletlenszám generátort
rng.shuffle(xs)         # Összekeverjük a listát
eredmeny = xs[:5]
print(eredmeny)


# 12.1.2.3. Random függvény, amely n darab random egész számot generál
# Ismétlődés kizárva. Nem generál listát, hatékony.
# Könyvbeli változat.

import random

def random_egeszek_duplikatum_nelkul(szam, also_hatar, felso_hatar):
  """ Véletlenszerűen generáljunk egy megadott számú egészeket tartalmazó listát
      az alsó és felső határ között. A felső határ nyitott. Az eredménylista nem
      tartalmazhat duplikátumokat. """
  eredmeny = []
  rng = random.Random()
  for i in range(szam):
       while True:
           valasztott = rng.randrange(also_hatar, felso_hatar)
           if valasztott not in eredmeny:
               break
       eredmeny.append(valasztott)
  return eredmeny

xs = random_egeszek_duplikatum_nelkul(5, 1, 10000000)
print(xs)


# 12.1.2.4. Random függvény, amely n darab random egész számot generál
# Ismétlődés kizárva. Nem generál listát, hatékony.
# Saját változat, sokkal jobban tetszik.


import random

def random_egeszek_duplikatum_nelkul(szam, also_hatar, felso_hatar):
  """ Véletlenszerűen generáljunk egy megadott számú egészeket tartalmazó listát
      az alsó és felső határ között. A felső határ nyitott. Az eredménylista nem
      tartalmazhat duplikátumokat. """
  eredmeny = []
  rng = random.Random()
  while len(eredmeny) != szam:
      valasztott = rng.randrange(also_hatar, felso_hatar)
      if valasztott not in eredmeny:
          eredmeny.append(valasztott)

  return eredmeny

xs = random_egeszek_duplikatum_nelkul(5, 1, 10)
print(xs)


# 12.2 A time modul clock függvénye. Itt megmérjük, hogy mennyi ideig tart
# egy program futása


import time

def sajat_szum(xs):
    """
Saját összegző függvény, amely egy küszöbszámig összeadja a természetes számokat
    """
    szum = 0
    for v in range(xs):
        szum += v
    return szum

sz = 10000000 # A küszöbszám legyen 10 millió

# Mennyi ideig fut a saját összegző függvényünk.
t0 = time.clock()                # Meghívja a clock fv-t sajat_szum futása előtt
sajat_eredmeny = sajat_szum(sz)
t1 = time.clock()                # Meghívja a clock fv-t sajat_szum futása után
print("saját_eredmény = {0} (eltelt idő = {1:.4f} másodperc)"
.format(sajat_eredmeny, t1 - t0))

# Mennyi ideig fut a beépített összegző függvény.
t2 = time.clock()
gepi_eredmeny = sum(range(sz))
t3 = time.clock()
print("gépi_eredmény  = {0} (eltelt idő = {1:.4f} másodperc)"
.format(gepi_eredmeny, t3 - t2))


# 12.3. Math modul. Írassuk ki a pi értékét

import math
print(math.pi)

# 12.3.2. Math modul. Írassuk ki az e (Euler konstans) értékét

import math
print(math.e)

# 12.3.3. Math modul. Vonjunk négyzetgyököt 2-ből

import math
print(math.sqrt(2))

# 12.3.4. Math modul. 90 fokot konvertáljuk radiánra

import math
print(math.radians(90))

# 12.3.5. Math modul. Számoljuk ki sin(90)-et

import math
print(math.sin(math.radians(90))) # Először radiánba kell átváltani.


# 12.4. Saját modul létrehozása.
# Meghívunk egy modult amit egy külső file-ba mentettünk, nem az alap könyvtárba
#  A modulok (file-ok) kiterjesztése .py

# Először hozzáadjuk annak a könyvtárnak a teljes elérési útját, ahol a file
#  van, ami a 'torol' függvényt tartalmazza.

import sys
sys.path.append('/home/zolcs/Dropbox/python/pys/moduls')

# Beimportáljuk a resztörlés.py-t mint modult, ebben van a 'torol' függvény
import resztorles

s = "Egy asztalt!"
i = 7

print(resztorles.torol(i, s))


# 12.5. Névterek. A névterek olyan azonosítók gyűjteményei, amelyek vagy egy
# modulhoz vagy egy függvényhez tartoznak.
# file = modul = névtér. A math.py file esetén a modul neve 'math' és a névtér
# szintén 'math'.
# Itt az 'n' 3 különböző névtérhez tartozik, ezért nem probléma a meghívásuk

def f():
   n = 7
   print("n kiírása az f-ben:", n)

def g():
   n = 42
   print("n kiírása a g-ben:", n)

n = 11
print("n kiírása az f hívása előtt:", n) # n a globális névtérhez tartozik
f()                                      # n az f függvény névteréhez tartozik
print("n kiírása az f hívása után:", n)  # n a globális névtérhez tartozik
g()                                      # n a g függvény névteréhez tartozik
print("n kiírása a g hívása után:", n)   # n a globális névtérhez tartozik


# Másik példa, különböző modulokból, azaz file-okból hívunk meg azonos nevű
# változókat, amely változókat a modul attribútumának nevezünk, a meghívást a
# pont operátor (.) segítségével teszük, azaz: modul.attribútum
# Ez a teljesen minősített név


# Modul1.py

kerdes = "Mi a jelentése az Életnek, a Világegyetemnek és a Mindenségnek?"
valasz = 42

# Modul2.py

kerdes = "Mi a küldetésed?"
valasz = "Keresni a Szent Grált!"

import Modul1
import Modul2

print(Modul1.kerdes)
print(Modul2.kerdes)
print(Modul1.valasz)
print(Modul2.valasz)


# 12.6. Hatókör, precedencia: lokális hatókör > globális hatókör > beépített
# hatókör

# 12.6.1. A lokális range() lesz erősebb a beépített range()-dzsel szemben.

def range(n):
   return 123*n

print(range(10))

# Másik példa

n = 10
m = 3
def f(n):
    m = 7
    return 2*n+m

print(f(5), n, m)


# 12.8. Az import utasítás 3 + 1 változata
# 1. változat, ez a legnépszerűbb, ez külön névteret őriz meg az importált
# modul számára, ezért kell a pont operátor, a kiértékelés a teljes minősített
# névvel történik

import math
x = math.sqrt(10)
print(x)


# 1.1 változat, lehet a beimportált modulnak más nevet is adni

import math as m
print(m.pi)


#2. változat, explicite azt importálom be a modulból ami kell, ekkor az
# importált objektumokat az importáló modul névterébe viszi, ezért NEM kell
# a pont operátor

from math import sqrt, sin, cos
y = sqrt(10)
print(y)

# 3. változat, beimportálok mindent mint az elsőnél de explicite

from math import *
z = sqrt(10)
print(z)


# 12.11.2.b

import math

print(math.ceil(1.0001))   # Felkerekít a köv. egész értékre
print(math.floor(1.999))   # # Lekerekít az előző egész értékre

# 12.11.2.c

x = 2
print(x ** 0.5)

# 12.11.2.d

print(math.pi)
print(math.e)


#1.Alapok, új változó a régi értékével, a referencia nem változik az új esetében

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

# A referenciája (a foglalt terület a memóriában) ugyanaz mind a 2 listánál

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))


# 2. Shallow copy. Az új objektumnak új referenciája lesz, de a beágyazott
# objektumok referenciái másolódnak -> ha vmelyik objektumhoz új elemet
# adok az nem fog változást okozni a másikban de ha egy beágyazott objektumot
# változtatok az egyikben akkor a másikban is változik

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print('Old List:', old_list)
print('ID of Old List:', id(old_list)) # A lista ref különböző
print('ID of [1][1] of Old List:', id(old_list[1][1])) # A beágyazott ref egyezik
print('ID of [1] of Old List:', id(old_list[1])) # A beágyazott ref egyezik

print('New List:', new_list)
print('ID of New List:', id(new_list)) # A lista ref különböző
print('ID of [1][1] of New List:', id(new_list[1][1])) # A beágyazott ref egyezik
print('ID of [1] of New List:', id(new_list[1])) # A beágyazott ref egyezik

# 2.1. Rakjunk be új elemet az egyik objektumba(listába). Csak abban jelenik meg
# amelyikbe explicite beraktam.

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

# 2.2 Változtassuk meg az egyik lista egy beágyazott listájának elemét.
# Mindkét listában megjelenik a változás.


old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)

# 2.3 Akkor is megjelenik a változás mindkét listában, ha olyan indexű helyre
# illesztek be elemet egy allistában, ami még nem létezik
# Az [1][3] elem nem létezik, oda rakom be a 'BB' stringet

old_list[1].insert(3, 'BB')

print("Old list:", old_list)
print("New list:", new_list)


#3. Deep copy, az objektumnak és a beágyazott objektumainak más lesz a
# referenciája, azaz két teljesen különböző, de azonos értékű objektumot
# kapok, ha az egyikben változtatok akkor az a másikra nem lesz hatással

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.deepcopy(old_list)

print('Old List:', old_list)
print('ID of Old List:', id(old_list)) # A lista ref különböző
print('ID of [1][1] of Old List:', id(old_list[1][1])) # A beágyazott ref egyezik
print('ID of [1] of Old List:', id(old_list[1])) # A beágyazott ref különböző

print('New List:', new_list)
print('ID of New List:', id(new_list)) # A lista ref különböző
print('ID of [1][1] of New List:', id(new_list[1][1])) # A beágyazott ref egyezik
print('ID of [1] of New List:', id(new_list[1])) # A beágyazott ref különböző

# 3.1. Rakjunk be új elemet az egyik objektumba(listába). Csak abban jelenik meg
# amelyikbe explicite beraktam.

old_list.append([4, 4, 4])

print("Old list:", old_list)
print("New list:", new_list)

# 3.2 Változtassuk meg az egyik lista egy beágyazott listájának elemét.
# Csak abban jelenik meg amelyikbe explicite beraktam.


old_list[1][1] = 'AA'

print("Old list:", old_list)
print("New list:", new_list)
print('ID of [1][1] of New List:', id(new_list[1][1]))
print('ID of [1][1] of Old List:', id(old_list[1][1]))

# 3.3 Adjunk hozzá új elemet az egyik listához.
# Csak abban jelenik meg amelyikbe explicite beraktam.

new_list[1].insert(3, 'BB')

print("Old list:", old_list)
print("New list:", new_list)


# 12.11.4. Nevter_teszt

import sajatmodul1
import sajatmodul2

print( (sajatmodul2.sajatev - sajatmodul1.sajatev) ==
       (sajatmodul2.ev - sajatmodul1.ev)  )

# 12.11.6. Tim Peters húsvéti tojása, a The Zen of Python

import this


#12.11.7. Karakterek cseréje szövegben

from egyseg_teszt import teszt


s = "Ez kell most, húsvéti tojás"
regi = 't'
uj = '2'

def cserel(regi, uj, s):
   """ Cseréld az s-ben a regi paraméter összes előfordulását az uj-ra. """
   t = s.split(regi)
   return uj.join(t)

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(cserel(",", ";", "ez, az, és valami más dolog") ==
                       "ez; az; és valami más dolog")
    teszt(cserel(" ", "**", "A szavak most csillaggal vannak elválasztva.") ==
                        "A**szavak**most**csillaggal**vannak**elválasztva.")

print(cserel(regi, uj, s))
# tesztkeszlet()


#12.11.8.1. Szótisztítás

import locale
from egyseg_teszt import teszt


locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása
abc = "aábcdeéfghiíjklmnoóöőpqrtuúüűvwxyzs0123456789"
abc_upper = abc.upper()

szo = "Hogy;mivanm.;-99)áé?"
print(szo)
def szo_tisztitas(szo):
    szo_tisztitott = ""
    for k in szo:
        if k in abc or k in abc_upper:
            szo_tisztitott += k
    return szo_tisztitott

def tesztkeszlet_szo_tisztitas():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(szo_tisztitas("hogyan?") ==  "hogyan")
    teszt(szo_tisztitas("'most!'") == "most")
    teszt(szo_tisztitas("?+='s-z-a-v!a,k@$()'") ==  "szavak")


# print(szo_tisztitas(szo))
tesztkeszlet_szo_tisztitas()

#12.11.8.2. Duplavonal

from egyseg_teszt import teszt

dp = "--"
szo = "?+='s-z-a--v!a,k@$()'"
def van_duplavonal(szo):
    """ Ellenőrzi, hogy van-e '--' karakterlánc az adott karakterláncban """
    if dp in szo:
        return True
    return False

def tesztkeszlet_van_duplavonal():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(van_duplavonal("kicsi--nagy") == True)
    teszt(van_duplavonal("") == False)
    teszt(van_duplavonal("magas--") == True)
    teszt(van_duplavonal("piros--fekete") == True)
    teszt(van_duplavonal("-igen-nem-") == False)

print(van_duplavonal(szo))
# tesztkeszlet_van_duplavonal()


#12.11.8.3. Szavakra bontás, 3 lépésben:
# 1.Minden betűt kicsire cserélünk a mondatba
# 2. Új mndatot készítünk, ahol nincsenek csak betűk és a szóköz
# 3. Szétválasztjuk a betűket a szeparátor alapján és egy listába rakjuk őket.

import locale
from egyseg_teszt import teszt

locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása
abc = "aábcdeéfghiíjklmnoóöőpqrtuúüűvwxyzs0123456789 "
mondat = "Cseréld az s-ben a regi paraméter összes előfordulását az uj-ra."
szep = ""

def szavakra_bontas(mondat):
    """
Szavakra bontja mndatot egy adott szeparátor alapján és egy listába teszi őket
    """
    mondat_lower = mondat.lower() # Minden betűt kicsire cserél
    pure_sentence = ""
    for k in mondat_lower:
        if k in abc:
            pure_sentence += k
    split_list = pure_sentence.split()
    return split_list

def tesztkeszlet_szavakra_bontas():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(szavakra_bontas(" Most van itt az idő? Igen, most.") ==
     ['most','van','itt','az','idő','igen','most'])
    teszt(szavakra_bontas("Ő megpróbált udvariasan viselkedni!") ==
     ['ő','megpróbált','udvariasan','viselkedni'])

# print(szavakra_bontas(mondat))
tesztkeszlet_szavakra_bontas()


#12.11.8.4. Szavak száma


from egyseg_teszt import teszt


lista = ["most","később","soha","most"]
szo = "most"

def szavak_szama(szo, lista):
    """  Megszámolja, hogy az adott szó hányszor szerepel a listában.  """
    counter = 0
    for k in lista:
        if k == szo:
            counter += 1
    return counter

def tesztkeszlet_szavak_szama():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(szavak_szama(
    "most", ["most","később","soha","most"]) == 2)
    teszt(szavak_szama(
    "itt", ["itt","ott","amott","itt","ott","amott","itt"]) == 3)
    teszt(szavak_szama(
    "tél", ["tavasz","nyár","ősz","tél","tavasz","nyár","ősz"]) == 1)
    teszt(szavak_szama(
    "kakukk", ["cinege","fecske","gólya","sas","veréb","páva","rigó"]) == 0)

# print(szavak_szama(szo, lista))
tesztkeszlet_szavak_szama()

#12.11.8.5. Szó halmaz, egy példányt minden szóból kiszed a listából és azt
# a listát abc szerint sorba rendezi.

from egyseg_teszt import teszt
import locale
import functools

locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása

lista = ["én", "te", "ő", "én", "te", "ő", "mi", "én"]


def szo_halmaz(lista):
    """  Egy szó példányt minden listából és abc szerint sorba rendez.  """
    egy_lista = []
    for k in lista:
        if k not in egy_lista:
            egy_lista.append(k)
    egy_lista.sort(key = functools.cmp_to_key(locale.strcoll))
    return egy_lista

def tesztkeszlet_szo_halmaz():
    teszt(szo_halmaz(
    ["most", "van", "itt", "most", "van", "itt"]) ==
    ["itt", "most", "van"])
    teszt(szo_halmaz(
    ["én", "te", "ő", "én", "te", "ő", "mi", "én"]) ==
    ["én", "mi", "ő", "te"])
    teszt(szo_halmaz(
    ["egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc"]) ==
    ["egy", "három", "hat", "hét", "kettő", "négy", "nyolc", "öt"])

# print(szo_halmaz(lista))
tesztkeszlet_szo_halmaz()


#12.11.8.6. Visszaadja egy listában a leghosszabb szó karaktereinek a számát

from egyseg_teszt import teszt
import locale


locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása

lista = ["én1111", "te", "ő", "123456789"]


def leghosszabb_szo(lista):
    """  Megszámolja, hogy a listában a leghosszabb szó hány karakter """
    hossz = 0
    for k in lista:
        if len(k) > hossz:
            hossz = len(k)
    return hossz

def tesztkeszlet_leghosszabb_szo():
    teszt(leghosszabb_szo(["alma", "eper", "körte", "szőlő"]) == 5)
    teszt(leghosszabb_szo(["én", "te", "ő", "mi"]) == 2)
    teszt(leghosszabb_szo(["ez","szórakoztatóelektronikai"]) == 24)
    teszt(leghosszabb_szo([ ]) == 0)

# print(leghosszabb_szo(lista))
tesztkeszlet_leghosszabb_szo()
