# 14.11.4.e Az n királynő probléma egyedi családba tartozó megoldásai
# A program listázhatja az összes megoldást, ehhez a 22-ik és 28-ik sort
# be kell kapcsolni.
#! n értékének változtatásával (22-ik sor) a 'talalat_szama' változó
# felső határát a while ciklus fejlécében (25-ik sor) is változtatni kell!
# 5 -> 10 | 6 -> 4 | 7 -> 40 | 8 -> 92 | 9 -> 352 | 10 -> 724 | 11 ->2680
# 12 -> 14200

# https://en.wikipedia.org/wiki/Eight_queens_puzzle

import time


def main():
    """   Az n királynő probléma különböző megoldásai.   """
    import random
    rng = random.Random()

    global vezer_lista
    vezer_lista = []
    global n
    n = 8
    talalat_szama = 0
    # print(f"\nAz n királynő probléma összes megoldása n = {n} esetén:\n")
    while talalat_szama < 92:
        bd = list(range(n))
        rng.shuffle(bd)
        if not van_utkozes(bd) and not bd in vezer_lista:
            vezer_lista.append(bd)
            # print('{0:<4}'.format(talalat_szama + 1), bd)
            talalat_szama += 1
    vezer_lista.sort()
    return vezer_lista


def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van


def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx


def n_queen_symmetries(megoldas):
    """   Az n királynő probléma egy szimmetriacsaládja   """

    symmetries = []
    symmetries.append(megoldas)

# Tükrözés az x-tengelyre
    yaxis = megoldas[:]
    yaxis.reverse()
    symmetries.append(yaxis)

# Tükrözés az y-tengelyre
    xaxis = []
    xaxis_meg = megoldas[:]
    for i in range(len(megoldas)):
        xaxis_meg[i] = (len(megoldas) - 1) - megoldas[i]
        xaxis.append(xaxis_meg[i])
    symmetries.append(xaxis)

# Elforgatás 90 fokkal
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    symmetries.append(rotate90)

# Elforgatás 180 fokkal
    rotate180 = []
    rotate180_meg = megoldas[:]
    rotate180_meg.reverse()
    for i in rotate180_meg:
        rotate180.append(len(megoldas) - 1 - i)
    symmetries.append(rotate180)

# Elforgatás 270 fokkal
    rotate270 = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        y = x - megoldas.index(z)
        rotate270.append(y)
        z += 1
    symmetries.append(rotate270)

#Tükrözés a bal(\) szimmetria átlóra
    mirrorleft = []
    x = len(megoldas) - 1
    z = x
    while z != -1:
        y = x - megoldas.index(z)
        mirrorleft.append(y)
        z -= 1
    symmetries.append(mirrorleft)

#Tükrözés a jobb(/) szimmetria főátlóra
    mirrorright = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        mirrorright.append(megoldas.index(z))
        z += 1
    symmetries.append(mirrorright)
    return symmetries

# print(n_queen_symmetries([0,4,7,5,2,6,1,3]))

t0 = time.perf_counter()
main()
# print(vezer_lista)
queen_fundamental = []
vezer_temp = vezer_lista[:]
while len(vezer_temp) != 0:
    for i in vezer_temp:
        symmetry_temp = []
        queen_fundamental.append(i)
        symmetry_temp = n_queen_symmetries(i)
        for j in symmetry_temp:
            if j in vezer_temp:
                vezer_temp.remove(j)

queen_fundamental.sort()
print(f"\nAz n királynő probléma egyedi megoldásai n = {n} esetén:\n")
for i in queen_fundamental:
    print('{0:<4}{1}'.format(queen_fundamental.index(i) + 1, i))
t1 = time.perf_counter()
print("\nA program teljes futási ideje:{0:.4f} másodperc".format(t1-t0))