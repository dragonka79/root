import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt


def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0) # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0) # Kiszámoljuk x távolságának abszolút értékét
    return dx == dy # Ütköznek, ha dx == dy

def oszlop_utkozes(bs, c):
    """ True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik a tőle balra levőkkel. """
    for i in range(c): # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True
    return False # Nincs ütközés, a c oszlopban biztonságos helyen van

def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
    Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
    ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


# Olyan megoldási esetek, amikor nincsenek ütközések
teszt(oszlop_utkozes([6,4,2,0,5], 4) == False)
teszt(oszlop_utkozes([6,4,2,0,5,7,1,3], 7) == False)
# További tesztesetek, amikor többnyire ütközések vannak
teszt(oszlop_utkozes([0,1], 1) == True)
teszt(oszlop_utkozes([5,6], 1) == True)
teszt(oszlop_utkozes([6,5], 1) == True)
teszt(oszlop_utkozes([0,6,4,3], 3) == True)
teszt(oszlop_utkozes([5,0,7], 2) == True)
teszt(oszlop_utkozes([2,0,1,3], 1) == False)
teszt(oszlop_utkozes([2,0,1,3], 2) == True)

teszt(van_utkozes([6,4,2,0,5,7,1,3]) == False) # A fenti megoldás
teszt(van_utkozes([4,6,2,0,5,7,1,3]) == True) # Felcseréljük az első két sort
teszt(van_utkozes([0,1,2,3]) == True) # Kipróbáljuk egy 4x4 sakktáblán
teszt(van_utkozes([2,0,3,1]) == False) # Megoldás 4x4-es esetben