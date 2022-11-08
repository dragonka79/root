# 14.3.4. A 13.3.3 tovább lépve, az Alice könyvől olvasom be a szavakat,
# megtisztítom és megmondom, hogy hány szó szerepel benne

# import sys
# sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/')

import time
def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden szót kisbetűssé alakít. """
    helyettesites = szoveg.maketrans(
    # Ha bármelyikükkel találkozol
    "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTUÚÜŰVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
    # Cseréld őket ezekre
    "aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz                                          "
    )
    # Most alakítsd át a szöveget
    tisztitott_szoveg = szoveg.translate(helyettesites)
    szavak = tisztitott_szoveg.split()
    return szavak

def szavak_a_konyvbol(fajlnev):
    """ Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját."""
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

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

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

nagyobb_szokincs = szavak_betoltese_fajlbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/szokincs.txt")

konyv_szavai = szavak_a_konyvbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/alice.txt")
print(f"A könyvben {len(konyv_szavai)} szó található, az első 100 a következő:\n{konyv_szavai[:100]}")

# hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
# print(hianyzo_szavak)
# print("Hiányzó szavak száma: ", len(hianyzo_szavak))

t0 = time.perf_counter()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.perf_counter()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))



