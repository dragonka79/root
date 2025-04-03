from unittest import teszt


def paratlan_szamok_szama(lista):
    """Gives the odd numbers in a list"""
    counter = 0
    for i in lista:
        if i % 2 != 0:
            counter += 1
        continue
    return counter


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(paratlan_szamok_szama([1, 2, 3, 4, -5]) == 3)
    teszt(paratlan_szamok_szama([0]) == 0)
    teszt(paratlan_szamok_szama([12, -24, 36, -108]) == 0)

tesztkeszlet()