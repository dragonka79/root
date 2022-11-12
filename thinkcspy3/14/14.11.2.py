# n királynő probléma különböző megoldásai 

# https://en.wikipedia.org/wiki/Eight_queens_puzzle

# n = 4 esetén 2 megoldás
# n = 8 esetén 92 megoldás
# n = 9 esetén 352 megoldás ~ 1 perc
# n = 10 esetén 724 megoldás ~ 8 perc
# n = 12 esetén 14,200 megoldás
# n = 16 esetén 14,772,512 megoldás

n = 10
r = 724

import time

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0) # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0) # Kiszámoljuk x távolságának abszolút értékét
    return dx == dy # Ütköznek, ha dx == dy

def oszlop_utkozes(bs, c):
    """ True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik a tőle balra levőkkel. """
    for i in range(c): # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True
    return False # Nincs ütközés, a c oszlopban biztonságos helyen van

def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
    Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
    ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False

def main():
    import random
    rng = random.Random() # A generátor létrehozása
    bd = list(range(n)) # Generálja a kezdeti permutációt
    talalat_szama = 0
    proba = 0
    talalatok = list()
    while talalat_szama < r:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd) and bd not in talalatok:
            print(f"Megoldás {talalat_szama + 1}. : {bd}, próbálkozás: {proba}.")
            fd = bd[:]  # bd-t klónozni kell, mert ha megváltozik bd a keverés miatt akkor talalatok egyetlen eleme(ami bd) is megváltozik
            talalatok.append(fd)
            proba = 0
            talalat_szama += 1
    # return talalatok

t0 = time.perf_counter()
main()
t1 = time.perf_counter()

td = t1 - t0
tm = td // 60
ts = td - (tm * 60)
print(f"Ez {int(tm)} perc {ts:.4f} másodpercet vett igénybe.")

# print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))
