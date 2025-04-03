import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

konyv_szavai = "az alma a fáról le esett a fűre".split()
szokincs = ["alma", "esett", "fűre", "fáról", "alá", "a", "fel"]

def teljes_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1 # Ha nincs az érték a listában, akkor a for ciklus nem ad vissza értéket; a teljes_keresés függvény teszi ezt

def ismeretlen_szavak_keresese(szoveg, szavak):
    """ Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne a szókincsben. """
    eredmeny = []
    for w in szavak:
        if (teljes_kereses(szoveg, w) == -1):
            eredmeny.append(w)
    return eredmeny

teszt(ismeretlen_szavak_keresese(szokincs, konyv_szavai) == ["az", "le"])
teszt(ismeretlen_szavak_keresese([], konyv_szavai) == konyv_szavai)
teszt(ismeretlen_szavak_keresese(szokincs, ["alma", "alá", "esett"]) == [])
