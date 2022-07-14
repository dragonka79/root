from unittest import teszt


def nap_nev(x):
    napok = ['hétfő','kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    if x in range(0, 7):
        return napok[x]
    else:
        return None


def nap_sorszam(nap):
    napok = ['hétfő','kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    if nap in napok:
        return napok.index(nap)
    else:
        return None


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(nap_sorszam("péntek") == 4)
    teszt(nap_sorszam("hétfő") == 0)
    teszt(nap_sorszam(nap_nev(3)) == 3)
    teszt(nap_nev(nap_sorszam("csütörtök")) == "csütörtök")

tesztkeszlet()
