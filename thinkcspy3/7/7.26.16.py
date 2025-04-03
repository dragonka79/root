from unittest import teszt

def negyzetosszeg(xs):
    negyzetsum = 0
    for i in xs:
        negyzetsum += i ** 2
    return negyzetsum

def tesztkeszlet_negyzetosszeg():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""

    teszt(negyzetosszeg([2, 3, 4]) == 29)
    teszt(negyzetosszeg([ ]) == 0)
    teszt(negyzetosszeg([2, -3, 4]) == 29)


tesztkeszlet_negyzetosszeg()


