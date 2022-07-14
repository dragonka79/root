from unittest import teszt

def nap_nev(x):
    napok = ['hétfő','kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
    if x in range(0, 7):
        return napok[x]
    else:
        return None

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(nap_nev(3) == "csütörtök")
    teszt(nap_nev(6) == "vasárnap")
    teszt(nap_nev(42) == None)

tesztkeszlet()