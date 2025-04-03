# 11.1 A lista eleme lehet string, integer, float vagy beágyazott lista

zs = ["hello", 2.0, 5, [10, 20]]
print(zs)


# 11.2 A lista elemeinek elérése

print(zs[0]) # Sima index alapján
print(zs[9-8]) # Egész értéket visszaadó kifejezés alapján
print(zs[int(8 / 4)]) # a Törés float-ot ad vissza, ezért kell int-té tenni.

# Lista bejárása, a ciklusváltozó is lehet a lista indexe

lovasok = ["háború", "éhínség", "pestis", "halál"]

for i in [0, 1, 2, 3]:
    print(lovasok[i])
print("\n")

for i in range(4):
    print(lovasok[i])
print("\n")
# De inkább használjuk ezt a lista elemeinek bejárásához

for h in lovasok:
    print(h)


# 11.3. A lista hossza

lovasok = ["háború", "éhínség", "pestis", "halál"]

for i in range(len(lovasok)):
    print(lovasok[i])

# Beágyazott lista esetén annak hossza 1 mert 1 lista elem

hossz = len(["autó gyártók", 1, ["Ford", "Toyota", "BMW"], [1, 2, 3]])
print(hossz)


# 11.4. Lista tagság, benne van-e az adott elem a listában

lovasok = ["háború", "éhínség", "pestis", "halál"]

print("pestis" in lovasok)
print("dezertálás" in lovasok)
print("dezertálás" not in lovasok)


# 11.5.1 Lista műveletek, összefűzés

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# 11.5.2 Lista műveletek, ismétlés

d = [0] * 4
print(d)

e = [1, 2, 3] * 3
print(e)


# 11.6. Lista szeletek

a_list = ["a", "b", "c", "d", "e", "f"]

print(a_list[1:3]) # elemek [1,3)
print(a_list[:4])  # elemek [0,4)
print(a_list[3:])  # elemek [3,end]
print(a_list[:])   # a lista összes eleme, maga a lista


# 11.7.1 Indexelt értékadás, egy elem módosítása

sajat_lista = ["A", "D", "A", "T"]
sajat_lista[3] = "G"
print(sajat_lista)


# 11.7.2 Indexelt értékadás, szelet módosítása, bővítés

a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = ["x", "y"]
print(a_list)

# 11.7.3 Indexelt értékadás, szelet módosítása, bővítés egyszerűbben

a_list = ["a", "d", "f"]
a_list[1:1] = ["b", "c"] # az "a" és "d" közé szúrjuk be
print(a_list)

# 11.7.4 Indexelt értékadás, lista elem vagy elemek eltávolítása üres lista
# beszúrásával

a_list = ["a", "b", "c", "d", "e", "f"]
a_list[1:3] = [] # 2-ik és 3-ik elemet üres listával írom felül azaz törlöm őket
print(a_list)


# 11.8.1  Lista törlése, egy elem törlése

a = ["egy", "kettő", "három"]
del a[1]
print(a)

# 11.8.2  Lista törlése, több elem törlése

a_list = ["a", "b", "c", "d", "e", "f"]
del(a_list[1:5]) # lista elemek [1:5) törlése
print(a_list)


# 11.9.Objektumok és hivatkozások. Ha sztringnek ugyanaz az értéke akkor
# ugyanarra az objektumra hivatkoznak, ez érthető, mert a sztringek
# megváltoztathatatlanok.
# A listák esetén nincs így, 2 különböző objektumra hivatkoznak.

a = "banán"
b = "banán"
print(a == b )  # egyenlő az értékük? Igen.
print(a is b)   # ugyanarra az objektumra hivatkoznak? Igen.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # egyenlő az értékük? Igen.
print(a is b)   # ugyanarra az objektumra hivatkoznak? Nem.


# 11.10. Fedőnevek: ha ugyanazon listára 2 névvel hivatkozunk

a = [1, 2, 3]
b = a
print(a, b)
print(a is b) #a és b ugyanarra az objektumra hivatkozik?Igen-> a és b fedőnevek

b[0]= 5
print(a, b)
print(a is b) #a és b ugyanarra az objektumra hivatkozik?Igen-> a és b fedőnevek


#11.11. Listák klónozása, az eredetivel egyező értékű lista létrehozása,
# amely az eredetihez képest másik objektumra mutat.

a = [1, 2, 3]
b = a[:]    # a klónozása b néven
print(a, b)
print(a is b) # a és b ugyanarra az objektumra mutatnak? Nem!
print(a == b) # a és b egyenlő? Igen

# Mivel más objektumra mutatnak, ezért változtatás az egyikben nem hat ki a
# másikra.

a[0] = 4
b[0] = 5
print(a, b)
print(a is b) # a és b ugyanarra az objektumra mutatnak? Nem!
print(a == b) # a és b egyenlő? Már nem.


# 11.12.1 Listák és a for ciklus. Emeljük egy lista minden elemének értékét
# négyzetre

xs = [5, 6, 7, 8, 9]

for i in range(len(xs)):
    xs[i] = xs[i] ** 2
print(xs)


# 11.12.2. Írassuk ki egy lista minden elemének indexét és az elemek értékét
# értékpárokba fogva-> enumerate

xs = [1, 2, 3, 4, 5]
for (i, v) in enumerate(xs):
    print(i, v)


# 11.12.3. Az 1. és 2. feladat egybegyúrva: emeljük négyzetre a lista minden
# elemének értékét a négyzetére

xs = [5, 6, 7, 8, 9]
for (i, v) in enumerate(xs):
    xs[i] = v ** 2
print(xs)


# 11.14.1 Lista metódusok, lista bővítése egy elemmel a lista végére

xs = [ 1, 2]
print(xs)
xs.append(3)
print(xs)

# 11.14.2 Lista metódusok, lista bővítése egy elemmel egy adott indexű helyre
#Szúrjuk be a 2-t az első indexű helyre
xl = [ 1, 3, 2]
print(xl)
xl.insert(1, 2)
print(xl)

# 11.14.3 Lista metódusok, egy adott értékű elem megszámlálása

print(xl.count(2))  #2

# 11.14.4 Lista metódusok, lista bővítése egy másik listával a végére

xl.extend([4, 5, 6]) # Listával bővítés az elemek felsorolásával
print(xl)

xn = [ 7, 8, 9]
xl.extend(xn)     # Listával bővítés magávala lista nevével
print(xl)

# 11.14.5 Lista metódusok, mi az első 2-es érték indexe xl-ben?

print(xl.index(2))  # 1


# 11.14.6 Lista metódusok, fordítsuk meg a lista elemeinek sorrendjét

xl.reverse()
print(xl)

# 11.14.7 Lista metódusok, rendezzük sorba a lista elemeit, amelyek csak
# számokat tartalmaz az értéküknél fogva

xl.sort()
print(xl)

# 11.14.8.1 Lista metódusok, szöveges adatot tartalmazó lista rendezése
# Itt nincs semmi extra.

szoveg_lista = ["barack", "alma", "mandarin"]
szoveg_lista.sort()
print(szoveg_lista)


# 11.14.8.2 Lista metódusok, szöveges adatot tartalmazó lista rendezése
# Itt van egy kis extra mert ékezetes betűk is vannak

szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort()
print(szoveg_lista2)  #Nem az igazi

import locale
import functools

locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort(key = functools.cmp_to_key(locale.strcoll))
print(szoveg_lista2)

# 11.14.9. Lista metódusok, szedjük ki az első 2-es értékű elemet

xk = [1, 2, 3, 2, 2]

xk.remove(2)
print(xk)


# 11.15.1 Tiszta függvények, amelyek az argumentumként kapott listát
# nem változtatják meg. Ez a funkcionális programozási stílus

def megduplaz(lista):
    uj_lista = []
    for i in lista:
        j = 2 * i
        uj_lista.append(j)
    return uj_lista

a = [ 2, 4, 6]
xs = megduplaz(a)
print(a)
print(xs)


# 11.15.2 Módosítók, olyan függvények, amelyek az argumentumként kapott listát
# megváltoztatják, az általuk okozott változás a mellékhatás.
# az előző 11.15.1-es megoldás módosítókkal.

# def megduplaz2(lista): # Ez egy egyszerűbb megoldás a csak módosítókra
#     for i in lista:
#         i = 2 * i
#     return lista


b = [2, 4, 6]
print(b)
b = megduplaz(b)
# b = megduplaz2(b)
print(b)


# 11.16.Listákat előállító függvények.
# n-nél kisebb prímek listája. Ehhez felhasználjuk a 7.26.10-ben készített
# prímszám tesztelő prim_e függvényt


import math
import sys

n = 1000


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
            break
        else:
            i+=1
    return True


# print(prim_e(19790130))


def prim_kisebbmint(n):
    """ Visszaadja az összes n-nél kisebb prímszámot. """
    eredmeny = []
    for i in range(2, n):
        if prim_e(i) == True:
            eredmeny.append(i)
    return eredmeny

xx = prim_kisebbmint(n)
print(xx)


# 11.17.1. Szrtingek és listák. Split metódus # 1

# Szétválasztjuk a karakterláncot szavak listájába, az elválasztó(határoló)
# a szóköz

nota = "Esik eső, szép csendesen csepereg..."
szavak = nota.split()
print(szavak)


# 11.17.2. Szrtingek és listák. Split metódus # 2
# Szétválasztjuk a karakterláncot szavak listájába, az elválasztó(határoló)
# az 'se' string

print(nota.split('se'))


# 11.17.3. Szrtingek és listák. Join metódus, ragasztó, a split inverze,
# összeragasztunk 2 stringet egy adott határolóval

ragaszto = ';'
s = ragaszto.join(szavak)
print(s)
ragaszto2 = ' -- '
s = ragaszto2.join(szavak)
print(s)
ragaszto3 = ''
s = ragaszto3.join(szavak)
print(s)


# 11.18.1. A list függvény, megpróbál mindent listává alakítani.

xs = list("Mocsári Béka")
print(xs)
print("".join(xs))


# 11.18.2. Range függvény.Lusta, nem számolja ki rögtön az összes értéket,
# csak megigéri, hogy elvégzi ha kell -> nem pakol be mindent egyszerre a
# memóriába, ez csak Python2 esetén még ez nem volt így, de Python3-nél már igen.


n = 199

def f(n):
    """
Keresse meg az első pozitív egész számot 101 és n között, amely osztható 21-el.
    """
    for i in range(101, n):
        if i % 21 == 0:
            return i

print(f(n))

print(range(10))           # Hozzon létre egy lusta ígéretet
print(list(range(10)))     # Hívja meg az ígéretet, mely létrehozza a listát


# 11.19.Beágyazott listák

# Irassuk ki az s lista 3-ik elemének, ami egy beágyazott lista, első elemét (20)
# első megoldás

s = ["hello", 2.0, 5, [10, 20]]

print(s)

k = s[3]
t = k[1]
print(t)

# második, elegánsabb megoldás

print(s[3][1])

# Ez a második megoldás általánosítható tetszőleges mélységű beágyazás esetén.

ss = ["hello", 2.0, 5, [10, 20, [1, 3]]]
print(ss[3][2][1]) # Az eredmény 3


# 11.20. Mátrixok. Gyakorlatilag beágyazott listák, nulladik beágyazott lista a
# mátrix első sora, a második beágyazot lista az első sora és így tovább

mx = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mx)

# Irassuk ki mátrix első sorát.

print(mx[1])

# Irassuk ki mátrix második sorának első elemét(8).
# Az első index kiválasztja a sort, a második pedig az oszlopot.
print(mx[2][1])


# 11.22.3.

a = [1, 2, 3]
b = a[:]
print(a is b) # False, mert b a klónja
print(a, b)
b[0] = 5
print(a, b)

# 11.22.4.

ez = ["Én", "nem", "vagyok", "egy", "csodabogár"]
az = ["Én", "nem", "vagyok", "egy", "csodabogár"]
print("Test 1: {0}".format(ez is az))
ez = az
print("Test 2: {0}".format(ez is az))
print(ez, az)


# Mi van akkor ha az egyik listát azonosítjuk a másikkal és értékük nem egyenlő?

test1 = ["1Ma", "holnap"]
test2 = ["Ma", "2holnap"]

print("Test 1: {0}".format(test1 is test2))
# A jobb oldal kiértékelődik és a bal oldalon lévő változó megkapja értékként
test2 = test1 # test1 értékét megkapja test2
print("Test 2: {0}".format(test1 is test2))
print(test1, test2)

# Kontra ellenőrzés, most megcseréljük az azonosítást

test1 = ["1Ma", "holnap"]
test2 = ["Ma", "2holnap"]

print("Test 1: {0}".format(test1 is test2))
# A jobb oldal kiértékelődik és a bal oldalon lévő változó megkapja értékként
test1 = test2  # test2 értékét megkapja test1
print("Test 2: {0}".format(test1 is test2))
print(test1, test2)


# 11.22.5. Összead két vektort a koordinátájuk alapján.

import sys


vektor1 = [1, 2, 3, 1, 1]
vektor2 = [4, 5, 6, 2, 2]


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)



def vektorok_osszege(u, v):
    """  Összead két vektort a koordinátájuk alapján.  """
    osszeg_vektor = []
    for i in range(len(u)):
        szum = u[i] + v[i]
        osszeg_vektor.append(szum)
    return osszeg_vektor


def tesztkeszlet_vektorok_osszege():
    """ A 11.22.5. modulhoz tartozó tesztkészlet futtatása.  """
    teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
    teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
    teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])

# print(vektorok_osszege(vektor1, vektor2))
tesztkeszlet_vektorok_osszege()


# 11.22.6. Egy vektor egy skalárral való szorzása

import sys


vektor = [2, 4, 1, -1, 1]
skalar = 3


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)



def szorzas_skalarral(s, v):
    """  Egy vektor egy skalárral való szorzása.  """
    skalar_vektor = []
    for i in range(len(v)):
        skalar_koordinata = s * v[i]
        skalar_vektor.append(skalar_koordinata)
    return skalar_vektor


def tesztkeszlet_szorzas_skalarral():
    """ A 11.22.6. modulhoz tartozó tesztkészlet futtatása.  """
    teszt(szorzas_skalarral(5, [1, 2]) == [5, 10])
    teszt(szorzas_skalarral(3, [1, 0, -1]) == [3, 0, -3])
    teszt(szorzas_skalarral(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

# print(szorzas_skalarral(skalar, vektor))
tesztkeszlet_szorzas_skalarral()


# 11.22.7. Két vektor skaláris szorzata

import sys


vektor1 = [1, 2, 3, 1, 1]
vektor2 = [4, 5, 6, 2, 2]


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)



def skalaris_szorzat(u, v):
    """  Két vektor skaláris szorzata  """
    skalaris_szorzat = 0
    for i in range(len(u)):
        koordinata_szorzat = u[i] * v[i]
        skalaris_szorzat += koordinata_szorzat
    return skalaris_szorzat


def tesztkeszlet_skalaris_szorzat():
    """ A 11.22.7. modulhoz tartozó tesztkészlet futtatása.  """
    teszt(skalaris_szorzat([1, 1], [1, 1]) ==  2)
    teszt(skalaris_szorzat([1, 2], [1, 4]) ==  9)
    teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)

# print(skalaris_szorzat(vektor1, vektor2))
tesztkeszlet_skalaris_szorzat()


# 11.22.8. Két vektor vektoriális szorzata

import sys


vektor1 = [1, 2, 3]
vektor2 = [4, 5, 6]


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)



def vektorialis_szorzat(u, v):
    """  Két vektor vektoriális szorzata  """
    c1 = u[1] * v[2] - u[2] * v[1]
    c2 = u[2] * v[0] - u[0] * v[2]
    c3 = u[0] * v[1] - u[1] * v[0]
    c = [c1, c2, c3]
    return c


def tesztkeszlet_vektorialis_szorzat():
    """ A 11.22.8. modulhoz tartozó tesztkészlet futtatása.  """
    teszt(vektorialis_szorzat([1, 1, 1], [0, 0, 0]) ==  [0, 0, 0])
    teszt(vektorialis_szorzat([1, -1, 2], [3, -2, -3]) ==  [7, 9, 1])
    teszt(vektorialis_szorzat([-2, 2, 4], [2, -1, 3]) ==  [10, 14, -2])

# print(vektorialis_szorzat(vektor1, vektor2))
tesztkeszlet_vektorialis_szorzat()


# 11.22.10. Karaktereket cserél ki egy karakterláncban

import sys


string = "Mississippi"
regi = "i"
uj = "I"


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def cserel(s, regi, uj):
    """  Karaktereket cserél ki egy karakterláncban  """
    split_lista = s.split(regi)
# Az eredeti stringbe íratom vissza hogy a harmadik teszt lefusson
    string = uj.join(split_lista)
    return string

def tesztkeszlet_cserel():
    s = "Kerek a gömb, gömbszerű!"
    """ A 11.22.10 a modulhoz tartozó tesztkészlet futtatása.  """
    teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
    teszt(cserel(s, "öm", "om") == "Kerek a gomb, gombszerű!")
    teszt(cserel(s, "o", "ö") == "Kerek a gömb, gömbszerű!")

# print(cserel(string, regi, uj))
tesztkeszlet_cserel()


# 11.22.11. Csere függvény, működő változat, 2 új sort kell belerakni


def csere(x, y):
    print("csere utasítás előtt: x:", x, "y:", y)
    (x, y) = (y, x)
    print("csere utasítás után: x:", x, "y:", y)
    return (x, y)   # új sor

a = ["Ez", "nagyon", "érdekes"]
b = [2,3,4]
print("csere függvény hívása előtt: a:", a, "b:", b)
(a,b) = csere(a, b) # új sor
print("csere függvény hívása után: a:", a, "b:", b)


# 11.22.11.Extra saját feladat: Hogyan törlök egy lista beágyazott listájából
# egy elemet.
# Töröljük ki a [1][1] elemet az old_list listából

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

del old_list[1][1]
print(old_list)
