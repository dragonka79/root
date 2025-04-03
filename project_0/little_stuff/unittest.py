import sys

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)
