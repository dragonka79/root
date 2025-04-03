from unittest import teszt

def paros_szamjegy_szam(n):
    """Megszámolja a páros számjegyeket egy számban"""
    count = 0
    n = abs(n)
    while n != 0:
        m = n % 10
        if m % 2 == 0:
            count += 1
        n = n // 10
    return count


def tesztkeszlet_szamjegy_szam():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    teszt(paros_szamjegy_szam(123456) == 3)
    teszt(paros_szamjegy_szam(2468) == 4)
    teszt(paros_szamjegy_szam(1357) == 0)
    teszt(paros_szamjegy_szam(0) == 0) # A 0 nem páros és nem páratlan
    teszt(paros_szamjegy_szam(4) == 1)
    teszt(paros_szamjegy_szam(7) == 0)
    teszt(paros_szamjegy_szam(-123456) == 3)


tesztkeszlet_szamjegy_szam()

