from unittest import teszt

def karakter_szamlalas(string, karakter):
    darab = 0
    x = string.find(karakter, 0)
    if x != -1:
        while x <= len(string) - len(karakter):
            x = string.find(karakter, x)
            x += len(karakter)
            darab += 1
    return darab

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(karakter_szamlalas("banán", "n") == 2)
    teszt(not karakter_szamlalas("bakony","ny") == 0)
    teszt(karakter_szamlalas("bakonnyeny","ny") == 2)
    teszt(karakter_szamlalas("eaee", "e") == 3)
    teszt(karakter_szamlalas("szöszi", "zs") == 0)

tesztkeszlet()  