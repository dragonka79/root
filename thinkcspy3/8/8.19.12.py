import sys

def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def torles(sztring1, sztring2):
    sztring_torolt = ""
    e = sztring2.find(sztring1)
    if e != -1:
        f = sztring2.find(sztring1) + len(sztring1)
        sztring_torolt = sztring2[:e] + sztring2[f:]
        return sztring_torolt
    return sztring2

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(torles("alma", "almafa") == "fa")
    teszt(torles("an", "banán") == "bán")
    teszt(torles("pa", "papaja") == "paja")
    teszt(torles("pa", "Papaja") == "Paja")
    teszt(torles("alma", "kerékpár") == "kerékpár")

tesztkeszlet()

# teszt(torles("alma", "kerékpár") == "kerékpár")
