import sys

def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def szamlalas(sztring1, sztring2):
    count = 0
    i = 0
    while i <= len(sztring2) - len(sztring1):
        if sztring1 == sztring2[i:i + len(sztring1)]:
            count += 1
        i += 1
    return count

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(szamlalas("gö", "görögös") == 2)
    teszt(szamlalas("pa", "papaja") == 2)
    teszt(szamlalas("apa", "papaja") == 1)
    teszt(szamlalas("papa", "papaja") == 1)
    teszt(szamlalas("apap", "papaja") == 0)
    teszt(szamlalas("aaa", "aaaaaa") == 4)

tesztkeszlet()
