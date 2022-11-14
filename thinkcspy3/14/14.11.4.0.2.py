# 14.11.4.0.2. n királynő probléma. Tükrözzük a táblát a bal (\) átlóra.
# Keresd meg a legnagyobb
# értékű elemet és rakd az új lista végére '(n - 1) - régi index' értékkel

import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

def mirror_left(megoldas):
    """ Keresd meg a nagyobb értékű elemet és rakd be az új lista végére
    az '(n - 1) - régi index' értékkel. Menj rá a következő legkisebb
    értékre és csináld mint az előbb. Ezt addig folytasd amíg van elem a kezdeti
    listában.
    """
    mirrorleft = []
    x = len(megoldas) - 1
    z = x
    while z != -1:
        y = x - megoldas.index(z)
        mirrorleft.append(y)
        z -= 1
    return mirrorleft


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(mirror_left([2, 0, 3, 1]) == [1, 3, 0, 2])
    teszt(mirror_left([0, 4, 7, 5, 2, 6, 1, 3]) == [5, 2, 4, 6, 0, 3, 1, 7])

tesztkeszlet()