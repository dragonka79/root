import sys
def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def betu_eltuntetes(betu, sztring):
    betu_nelkul = ""
    for i in sztring:
        if i != betu:
            betu_nelkul += i
    return betu_nelkul

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(betu_eltuntetes("a", "alma") == "lm")
    teszt(betu_eltuntetes("a", "banán") == "bnán")
    teszt(betu_eltuntetes("z", "banán") == "banán")
    teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
    teszt(betu_eltuntetes("b", "") == "")
    teszt(betu_eltuntetes("b", "c") == "c")

tesztkeszlet()