# 16.1 Téglalapok

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

teglalap = Teglalap(Pont(), 100, 200) # origo balsarkú pont
bomba = Teglalap(Pont(100,80), 5, 10)
print("teglalap: ", teglalap)
print("bomba :", bomba)
# a 'bomba' objektum csucs attributumának x attribútumának értéke
print(bomba.csucs.x)

# 16.2 Az objektumok módosíthatók, téglalapok méretezése, mozgatása

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def noveles(self, delta_szelesseg, delta_magassag):
        """ Növeli (vagy csökkenti) ezt az objektumot a delta értékekkel. """
        self.szelesseg += delta_szelesseg
        self.magassag += delta_magassag

    def mozgatas(self, dx, dy):
        """ Elmozdítja ezt az objektumot a delta értékekkel. """
        self.csucs.x += dx
        self.csucs.y += dy

r = Teglalap(Pont(10,5), 100, 50)
print(r)

r.noveles(25, -10)
print(r)

r.mozgatas(-10, 10)
print(r)

# 16.3.1 Azonosság, referencia és érték szerinti egyenlőségviszgálat

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))

    def azonos_koordinatak(p1, p2):
        return( (p1.x == p2.x) and (p1.y == p2.y) )

p1 = Pont(3, 4)
p2 = Pont(3, 4)
p3 = p1
# Érték szerinti egyenlőségvizsgálat
print(Pont.azonos_koordinatak(p1, p2))
# Referencia szerinti egyenlőségvizsgálat
print(p1 is p2) #False
print(p1 is p3) #True

# 16.3.2 A ' == ' pontok esetében referencia szerint vizsgál,
# listák vagy pontpárok esetében érték szerint

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ( "{0}, {1}".format(self.x, self.y) )

p = Pont(4, 2)
s = Pont(4, 2)
print("Az == eredménye Pontokra alkalmazva:", p == s)
# Alapértelmezés szerint az == a Pont objektumoknál
#  referencia szerinti egyenlőséget néz.

a = [2,3]
b = [2,3]
print("Az == eredménye listákra alkalmazva:", a == b)
# A listáknál viszont az érték szerinti egyenlőségvizsgálat
#  az alapértelmezett.

# 16.4.1 Sekény másolás, azaz 'copy'
# Egyszerű, beágyazott objektumot nem tartalmazó objektum másolására a 'copy',
# azaz a sekély másolás megfelelő
import copy


class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))

    def azonos_koordinatak(p1, p2):
        return( (p1.x == p2.x) and (p1.y == p2.y) )

p1 = Pont(3, 4)
p2 = copy.copy(p1)
print("p1 és p2 referencia szerint azonos?: ", p1 is p2)
print("p1 és p2 érték szerint azonos?: ", Pont.azonos_koordinatak(p1, p2))

#A sekély copy beágyazott objektum másolására nem alkalmas, mert a belső objektum
# referenciáját másolja

class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def noveles(self, delta_szelesseg, delta_magassag):
        """ Növeli (vagy csökkenti) ezt az objektumot a delta értékekkel. """
        self.szelesseg += delta_szelesseg
        self.magassag += delta_magassag

    def mozgatas(self, dx, dy):
        """ Elmozdítja ezt az objektumot a delta értékekkel. """
        self.csucs.x += dx
        self.csucs.y += dy

t1 = Teglalap(Pont(10,5), 100, 50)
t2 = copy.copy(t1)
print("t1 és t2 referencia szerint azonos?: ", t1 is t2)
print("t1 és t2 csúcskoordinátája refje azonos?: ", t1.csucs.x is t2.csucs.x)
print("t1: ", t1)
print("t2: ", t2)

# Itt jön ki a sekény copy hiányossága, mert a növelés esetében nem használja a
# csúcsot, de a mozgatás esetében igen
t1.noveles(25, -10)
print("t1 a növelés után: ", t1)
print("t2 a növelés után: ", t2) # Nem hat t2-re

t1.mozgatas(-10, 10)
print("t1 a mozgatás után: ", t1)
print("t2 a mozgatás után: ", t2) # Hat t2-re, együtt mozog a csúcs t1-gyel
print("t1 és t2 csúcskoordinátája refje azonos?: ", t1.csucs.x is t2.csucs.x)

# 16.4.2 Mély másolás, azaz 'deepcopy', beágyazott objektumok másolására, mert
# a beágyazott objektumot is másolja, de furi, mert a másolt beágyazott objektum
# referenciája megegyezik az eredetivel, de ha módosítom vmelyiket akkor a másik
# nem módosul, azaz mások lesznek a referenciák

import copy


class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))

    def azonos_koordinatak(p1, p2):
        return( (p1.x == p2.x) and (p1.y == p2.y) )


class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def noveles(self, delta_szelesseg, delta_magassag):
        """ Növeli (vagy csökkenti) ezt az objektumot a delta értékekkel. """
        self.szelesseg += delta_szelesseg
        self.magassag += delta_magassag

    def mozgatas(self, dx, dy):
        """ Elmozdítja ezt az objektumot a delta értékekkel. """
        self.csucs.x += dx
        self.csucs.y += dy

t1 = Teglalap(Pont(10,5), 100, 50)
t2 = copy.deepcopy(t1)
print("t1 és t2 referencia szerint azonos?: ", t1 is t2)
print("t1 és t2 csúcskoordinátája refje azonos?: ", t1.csucs.x is t2.csucs.x)
print("t1: ", t1)
print("t2: ", t2)

# A csúcs refje t1 és t2 esetében ugyanaz(wtf???), de itt már t1 mozgatása
# során t2 nem mozog

t1.noveles(25, -10)
print("t1 a növelés után: ", t1)
print("t2 a növelés után: ", t2) # Nem hat t2-re

t1.mozgatas(-10, 10)
print("t1 a mozgatás után: ", t1)
print("t2 a mozgatás után: ", t2) # Nem hat t2-re
print("t1 és t2 csúcskoordinátája refje azonos?: ", t1.csucs.x is t2.csucs.x)


# 16.6.1
from egyseg_teszt import teszt

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))


class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def terulet(self):
        """
        Visszaadja a téglalap területét a szélessége és magassága alapján
        """
        return (self.szelesseg * self.magassag)


r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.terulet() == 50)


# 16.6.2
from egyseg_teszt import teszt

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))


class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def kerulet(self):
        """
        Visszaadja a téglalap kerületét a szélessége és magassága alapján
        """
        return( (self.szelesseg + self.magassag) * 2 )


r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.kerulet() == 30)

# 16.6.3
from egyseg_teszt import teszt

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))


class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def forditas(self):
        """
        Megcseréli a téglalap szélességét és magasságát
        """
        (self.szelesseg, self.magassag) = (self.magassag, self.szelesseg)
        return(self.szelesseg, self.magassag)


r = Teglalap(Pont(100, 50), 10, 5)
# print(r.szelesseg, r.magassag)
# print(id(r.szelesseg), id(r.magassag))
teszt(r.szelesseg == 10 and r.magassag == 5)
r.forditas()
teszt(r.szelesseg == 5 and r.magassag == 10)
# print(r.szelesseg, r.magassag)
# print(id(r.magassag), id(r.szelesseg))


# 16.6.4
from egyseg_teszt import teszt

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("{0}, {1}".format(self.x, self.y))


class Teglalap:
    """ Egy osztály a téglalapok előállításához. """

    def __init__(self, poz, sz, m):
        self.csucs = poz
        self.szelesseg = sz
        self.magassag = m

    def __str__(self):
        return("{0}, {1}, {2}"
        .format(self.csucs, self.szelesseg, self.magassag))

    def tartalmazza_e(self, p1):
        """
        Meghatározza a téglalap 2 szélső pontját a referencia ponttól(origo) és
        megnézi, hogy a vizsgált pont az origó és a szélső pontok között van-e
        """
        self.x1 = self.csucs.x + self.szelesseg
        self.y1 = self.csucs.x + self.magassag

        s1 = p1.x < self.x1 and p1.x >= self.csucs.x
        s2 = p1.y < self.y1 and p1.y >= self.csucs.y
        return(s1 and s2)

r = Teglalap(Pont(0, 0), 10, 5)
teszt(r.tartalmazza_e(Pont(0, 0)))
teszt(r.tartalmazza_e(Pont(3, 3)))
teszt(not r.tartalmazza_e(Pont(3, 7)))
teszt(not r.tartalmazza_e(Pont(3, 5)))
teszt(r.tartalmazza_e(Pont(3, 4.99999)))
teszt(not r.tartalmazza_e(Pont(-3, -3)))
