import sys
def teszt(sikeres_teszt):
    """ Egy teszt eredményének megjelenítése. """
    sorszam = sys._getframe(1).f_lineno # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

def sztring_forditas(sztring):
    rev_string = sztring[::-1]
    return rev_string

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(sztring_forditas("boldog") == "godlob")
    teszt(sztring_forditas("Python") == "nohtyP")
    teszt(sztring_forditas("") == "")
    teszt(sztring_forditas("a") == "a") 

tesztkeszlet()