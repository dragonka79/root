import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt


# 14.11.4.0.1. Tükrözzük a táblát a jobb (/) átlóra. Felcseréjük az értékeket
# és az indexeket.

def mirror_right(megoldas):
    """ Keresd meg a legkisebb értékű elemet és rakd be az új lista végére
    a 'mostani indexe' mértékkel. Menj rá a következő legkisebb
    értékre és csináld mint az előbb. Ezt addig folytasd amíg van elem a kezdeti
    listában.
    """
    mirrorright = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        mirrorright.append(megoldas.index(z)) # megoldas.index(z) = 'z' értékű elem indexe a 'megoldas' listában
        z += 1
    return mirrorright

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(mirror_right([2, 0, 3, 1]) == [1, 3, 0, 2])
    teszt(mirror_right([0, 4, 7, 5, 2, 6, 1, 3]) == [0, 6, 4, 7, 1, 3, 5, 2])

tesztkeszlet()