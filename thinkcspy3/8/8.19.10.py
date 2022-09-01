import sys
def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def palindrom_e(sztring):
    if len(sztring) > 0:
        for i in range((len(sztring) // 2) + 1):
            if sztring[i] == sztring[-i-1]:
                return True
            return False
    return True

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(palindrom_e("abba"))
    teszt(not palindrom_e("abab"))
    teszt(palindrom_e("teret"))
    teszt(not palindrom_e("banán"))
    teszt(palindrom_e("mesék késem"))
    teszt(palindrom_e("a"))
    teszt(palindrom_e("")) # Egy üres sztring palindrom-e?

tesztkeszlet()
# teszt(palindrom_e("aa"))

