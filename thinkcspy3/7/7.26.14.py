from unittest import teszt


def szamjegy_szam(n):
    szamlalo = 0
    if n == 0:
        return 1
    else:
        while n != 0: 
            szamlalo += 1
            n = abs(n) // 10
            # print(n, szamlalo)
        return szamlalo


def tesztkeszlet_szamjegy_szam():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""

    teszt(szamjegy_szam(0) == 1)
    teszt(szamjegy_szam(-12345) == 5)
    teszt(szamjegy_szam(1) == 1)
    teszt(szamjegy_szam(1000) == 4)
    teszt(szamjegy_szam(9999) == 4)


tesztkeszlet_szamjegy_szam()