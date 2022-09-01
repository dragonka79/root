import sys
def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def tukor(sztring):
    tukor_string = sztring + sztring[::-1]
    return tukor_string

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(tukor("jo") == "jooj")
    teszt(tukor("Python") == "PythonnohtyP")
    teszt(tukor("") == "")
    teszt(tukor("a") == "aa")

tesztkeszlet()