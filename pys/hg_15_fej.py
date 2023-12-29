#15.2. Pont osztály létrehozása pont reprezentálásásra

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """
    def __init__(self):    # Ez az inicializáló metódus, az __init__
        """ Egy új, origóban álló pont létrehozása. """
        self.x = 0
        self.y = 0

#  És a pont osztály felhasználása, 2 pont létrehozása (0,0) koordinátákkal

p = Pont()  # A Pont osztály egy objektumának létrehozása (példányosítás)
q = Pont()  # Egy második Pont objektum készítése

# Minden Pont objektum saját x és y attribútumokkal rendelkezik
print(p.x, p.y, q.x, q.y)


# 15.4. Az inicializáló metódus továbbfejlesztése

class Pont:
    """
    A Pont osztály (x, y) koordinátáinak reprezentálására és manipulálására.
    """

    def __init__(self, x = 0, y = 0):
        """ Egy új, (x, y) koordinátán álló pont készítése. """
        self.x = x
        self.y = y

p = Pont(4, 2)
q = Pont(6, 3)
r = Pont()          # r az origót reprezentálja

print(p.x, q.y, r.x)

# 15.5 Újabb metódusok hozzáadása az osztályunkhoz

class Pont:
    """ Pont osztály (x, y) koordináták reprezentálására és manipulálására. """

    def __init__(self, x=0, y=0):
        """ Egy új, x, y koordinátán álló pont készítése. """
        self.x = x
        self.y = y

    def origotol_mert_tavolsag(self):
        """ Az origótól mért távolság számítása. """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

#tesztek
p = Pont(3, 4)
print(p.x)
print(p.y)
print(p.origotol_mert_tavolsag())

q = Pont(5, 12)
print(q.x)
print(q.y)
print(q.origotol_mert_tavolsag())

r = Pont()
print(r.x)
print(r.y)
print(r.origotol_mert_tavolsag())


# 15.6. Példányok felhasználása argumentumként és paraméterként
# Írjunk metódust, ami kiírja a pontot (a pont koordinátáit)

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def pont_kiiras(pt):
        print("({0}, {1})".format(pt.x, pt.y))


p = Pont(4, 3)
r = Pont()      # az inicializáló metódus kezdeti értékei, azaz az origó
p.pont_kiiras()
r.pont_kiiras()


# 15.7 Egy objektum példányának stringgé alakítása

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return("({0}, {1})".format(self.x, self.y))


p = Pont(4, 3)
r = str(p)
print(str(p))
print(p)
print('r típusa = ', type(str(p))) # Sztring a típusa? Igen
print('p típusa = ', type(p))

# 15.8. Példányok, mint visszatérési értékek
# Súlypont kiszámítása 2 pont esetén függvényként leírva


# Definiálom az osztályt
class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

# Modul definiálása, az osztályon kívülre kerül
def sulypont_szamitas(p1, p2):
    """ Visszatér a p1 és p2 pontok súlypontjával. """
    mx = (p1.x + p2.x) / 2
    my = (p1.y + p2.y) / 2
    return (mx, my)

p = Pont(3, 4)
q = Pont(5, 12)
r = sulypont_szamitas(p, q)
print(r)


# 15.8.2 Példányok, mint visszatérési értékek
# Súlypont kiszámítása 2 pont esetén metódussal


# Definiálom az osztályt
class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def sulypont_szamitas(self, masik_pont):
        """ A súlypontom a másik ponttal. """
        mx = (self.x + masik_pont.x) / 2
        my = (self.y + masik_pont.y) / 2
        return (mx, my)

p = Pont(3, 4)
q = Pont(5, 12)
r = p.sulypont_szamitas(q)
print(r)

# 15.8.3 Példányok, mint visszatérési értékek
# Súlypont kiszámítása 2 pont esetén metódussal, változók nélkül


# Definiálom az osztályt
class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def sulypont_szamitas(self, masik_pont):
        """ A súlypontom a másik ponttal. """
        mx = (self.x + masik_pont.x) / 2
        my = (self.y + masik_pont.y) / 2
        return (mx, my)

print(Pont(3, 4).sulypont_szamitas(Pont(5, 12)))

# 15.12.1.

import math

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def tavolsag(pont1, pont2):
    return math.sqrt( (pont2.x - pont1.x)**2 + (pont2.y - pont1.y)**2 )

p = Pont(1, 2)
q = Pont(4, 6)
print(tavolsag(p, q))

# 15.12.2.

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def tukrozes_x_tengelyre(self):
        return(self.x, -self.y)

p = Pont(1, 2)
q = Pont(-4, -6)
r = Pont()
print(p.tukrozes_x_tengelyre())
print(q.tukrozes_x_tengelyre())
print(r.tukrozes_x_tengelyre())


# 15.12.3.

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def tukrozes_x_tengelyre(self):
        return(self.x, -self.y)

    def origotol_mert_meredekseg(self):
        if self.x == 0:
            tg = 0
        else:
            tg = self.y / self.x
        return tg

p = Pont(1, 2)
q = Pont(4, 10)
r = Pont()
print(p.origotol_mert_meredekseg())
print(q.origotol_mert_meredekseg())
print(r.origotol_mert_meredekseg())


# 15.12.4.

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def atmeno_egyenes(self, p2):
        """ Két ponton átmenő egyenes egyenlete """
        if self.x != p2.x:
            m = int((p2.y - self.y) / (p2.x - self.x))
            c = int(( (self.y * p2.x) - (p2.y * self.x) ) / (p2.x - self.x))
            return(m,c )
        elif (self.x, self.y) == (p2.x, p2.y):
            return("A két pont azonos")
        else:
            return("x = {0}".format(self.x))

p = Pont(4, 11)
q = Pont(6, 15)
print(p.atmeno_egyenes(q))
