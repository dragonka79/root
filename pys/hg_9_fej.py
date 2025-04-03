# 9.1.1 Rendezett n-esek (tuple), változtathatatlan adatértékűek

# Rendezett pár

szuletesi_ev = ("Paris Hilton", 1981)
print(szuletesi_ev)
print(szuletesi_ev[0])  # A rendezett pár 0-ik indexű eleme
# szuletesi_ev[2] = 'X'   # A rendezett pár nem megváltoztatható

# Rendezett n-es

julia = ("Julia", "Roberts", 1967, "Kettős játék", 2009, "színésznő",
"Atlanta, Georgia")
print(julia)

# A rendezett n-es elemeit új rendezett n-esek létrehozására fel lehet használni
# Új 4-ik és 5-ik elemet veszek fel és azt egy azonos rendezett n-esbe mentem.

julia = julia[:3] + ("Pénzes cápa", 2016) + julia[5:]
print(julia)

# Rendezett 1-es, a végén egy ',' jel van a zárójelben.

egyes = ('egyes',)
print(egyes)


# 9.2.1. Értékadás rendezett n-essel, változóknak adok értéket rendezett n-es
# segítségével egy lépésben. Vagy máshogyan mondva rendezett n-esnek adok
# értéket egyetlen értékadó utasítással

adatok = ('Zoli', 1979, 'kék')
(nev, szul_ev, szeme_szine) = adatok
print(nev)
print(szul_ev)
print(szeme_szine)

# 9.2.2. Két változó értékének cseréje rendezett n-essel.

a = 5
b = 10
print(a, b)
(a, b) = (b, a)
print(a, b)


# 9.3.Rendezett n-es visszatérési értékként.

import math

r = 1

def ker_ter(r):
    """  Visszaadja egy kör kerületét és területét mint rendezett párt.  """
    k = 2 * r * math.pi
    t = pow(r, 2) * math.pi
    return (k, t)

print(ker_ter(r))


# 9.4 Adatszerkezetek alakíthatósága, példák homogén (különböző) típusú
# elemekből összeálló) listákra

# Ez egy olyan rendezett 5-ös, amely rendezett párokból áll, és a rendezett
# pároknak a második eleme egy több elemű lista

hallgatok = [
("Jani", ["Informatika", "Fizika"]),
("Kata", ["Matematika", "Informatika", "Statisztika"]),
("Peti", ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]),
("Andi", ["Információs rendszerek", "Könyvelés", "Közgazdaságtan"]),
("Feri", ["Szociológia", "Közgazdaságtan", "Jogi ismeretek", "Statisztika"])]

print(hallgatok)
print('\n')

# Ez egy olyan rendezett n-es, amelynek 5 eleme van, ezek az elemek különböző
# rendezett n-esek, például a harmadik egy sztring, az utolsó egy olyan lista,
# amely 7 darab rendezett párból áll.

julia_more_info = ( ("Julia", "Roberts"),
                    (1967, "október", 8),
                     "színésznő",
                    ("Atlanta", "Georgia"),
                    [ ("Sztárom a párom", 1999),
                      ("Micsoda nő", 1990),
                      ("Ízek, imák, szerelmek", 2010),
                      ("Erin Brockovich", 2000),
                      ("Álljon meg a nászmenet", 1997),
                      ("Egy veszedelmes elme vallomásai", 2002),
                      ("Oceans Twelve", 2004) ])

print(julia_more_info)


# 9.6.1. Rendezett n-es is lehet egy függvény paramétere

(a, b, c) = (2, 3, 5)

def abc(a, b, c):
    return(a*b, a*c, b*c)

print(abc(a, b, c))
