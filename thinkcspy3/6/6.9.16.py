from unittest import teszt

def tenyezo_e(t, n):
    """n t-nek egész számszorosa-e"""
    try:
        if n % t == 0:
            return True
        else:
            return False
    except:
        return "Zero division"


def tesztkeszlet_tenyezo_e():
    """ Az ehhez a modulhoz tartozó tesztkészlet. """
    teszt(tenyezo_e(3, 12))
    teszt(not tenyezo_e(5, 12))
    teszt(tenyezo_e(7, 14))
    teszt(not tenyezo_e(7, 15))
    teszt(tenyezo_e(1, 15))
    teszt(tenyezo_e(15, 15))
    teszt(not tenyezo_e(25, 15))
    teszt(tenyezo_e(0, 15) == "Zero division")


def tobbszorose_e(n, t):
    return tenyezo_e(t, n)


def tesztkeszlet_tobbszorose_e():
    """ Az ehhez a modulhoz tartozó tesztkészlet. """
    teszt(tobbszorose_e(12, 3))
    teszt(tobbszorose_e(12, 4))
    teszt(not tobbszorose_e(12, 5))
    teszt(tobbszorose_e(12, 6))
    teszt(tobbszorose_e(15, 1))
    teszt(tobbszorose_e(12, 0) == "Zero division")
    teszt(tobbszorose_e(0, 15))


tesztkeszlet_tenyezo_e()
tesztkeszlet_tobbszorose_e()

