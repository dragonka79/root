from unittest import teszt


def meredekseg(x1, y1, x2, y2):
    try:
        xy1 = x2 -x1
        xy2 = y2 -y1
        return xy2 / xy1
    except:
        return None

def tesztkeszlet_meredekseg():
    """ 6.9.13.1 A meredekseg modulhoz tartozó tesztkészlet. """
    teszt(meredekseg(5, 3, 4, 2) == 1.0)
    teszt(meredekseg(1, 2, 3, 2) == 0.0)
    teszt(meredekseg(1, 2, 3, 3) == 0.5)
    teszt(meredekseg(2, 4, 1, 2) == 2.0)
    teszt(meredekseg(2, 4, 2, 5) == None)


def metszespont(x1, y1, x2, y2):
    """ 6.9.13.2 Egy egyenes y tengellyel való metszésének pontja.  """
    metszespont = y1 - (meredekseg(x1, y1, x2, y2) * x1)
    return metszespont

def tesztkeszlet_metszespont():
    """ 6.9.13.2 A metszespont modulhoz tartozó tesztkészlet. """
    teszt(metszespont(1, 6, 3, 12) == 3.0)
    teszt(metszespont(6, 1, 1, 6) == 7.0)
    teszt(metszespont(4, 6, 12, 8) == 5.0)


tesztkeszlet_meredekseg()
tesztkeszlet_metszespont()