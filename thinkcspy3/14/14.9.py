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
    bd = list(range(8)) # Generálja a kezdeti permutációt
    talalat_szama = 0
    proba = 0
    while talalat_szama < 10:
        rng.shuffle(bd)
        proba += 1
        if not van_utkozes(bd):
            print(f"Megoldás {talalat_szama + 1}. : {bd}, próbálkozás: {proba}.")
            proba = 0
            talalat_szama += 1

main()
