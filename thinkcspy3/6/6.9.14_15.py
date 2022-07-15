from unittest import teszt

def paros_e(n):
    if n != 0:
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        return "A nulla nem páros és nem páratlan"

def tesztkeszlet_paros_e():
    """ Az ehhez a modulhoz tartozó tesztkészlet. """
    teszt(paros_e(2) == True)
    teszt(paros_e(3) == False)
    teszt(paros_e(-2) == True)
    teszt(paros_e(0) == "A nulla nem páros és nem páratlan")

tesztkeszlet_paros_e()


def paratlen_e(n):
    if n != 0:
        return not paros_e(n)
    else:
        return paros_e(n)


def tesztkeszlet_paratlen_e():
    """ Az ehhez a modulhoz tartozó tesztkészlet. """
    teszt(paratlen_e(2) == False)
    teszt(paratlen_e(3) == True)
    teszt(paratlen_e(-2) == False)
    teszt(paratlen_e(0) == "A nulla nem páros és nem páratlan")

tesztkeszlet_paros_e()
tesztkeszlet_paratlen_e()