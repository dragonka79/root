from unittest import teszt

def abszolut_ertek(x):
    if x < 0:
        return -x
    return x

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(abszolut_ertek(17) == 17)
    teszt(abszolut_ertek(-17) == 17)
    teszt(abszolut_ertek(0) == 0)
    teszt(abszolut_ertek(3.14) == 3.14)
    teszt(abszolut_ertek(-3.14) == 3.14)

tesztkeszlet()