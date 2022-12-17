# 14.11.4.c.3 Forgassuk el 270 fokkal a táblát.

import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def rotate_270(megoldas):
    """ Keresd meg a legkisebb értékű elemet és rakd be az új lista végére
    a 'tábla mérete - mostani indexe' mértékkel. Menj rá a következő legkisebb
    értékre és csináld mint az előbb. Ezt addig folytasd amíg van elem a kezdeti
    listában.
    """
    rotate270 = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        y = x - megoldas.index(z)
        rotate270.append(y)
        z += 1
    return rotate270

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(rotate_270([2, 0, 3, 1]) == [2, 0, 3, 1])
    teszt(rotate_270([0, 4, 7, 5, 2, 6, 1, 3]) == [7, 1, 3, 0, 6, 4, 2, 5])

tesztkeszlet()