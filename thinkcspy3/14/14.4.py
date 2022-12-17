# Bináris keresés rendezett listára a 14.3.4-ben alkalmazott teljes/lineáris kereséssel szemben.

import time

def binaris_kereses(xs, ertek):
    """ Keressük meg és térjünk vissza az érték indexével az xs sorozatban. """
    ah = 0       # indexek alsó határa
    fh = len(xs) # indexek felső határa
    while True:
        if ah == fh:
            return -1
        # A következő összehasonlítás a ROI közepén kell legyen
        kozep_index = (ah + fh) // 2

        # Meghatározzuk középső indexen lévő elemet
        kozep_elem = xs[kozep_index]

        # print("ROI[{0}:{1}](méret={2}), próba='{3}', érték='{4}'"
        # .format(ah, fh, fh-ah, kozep_elem, ertek))

        # Hasonlítsuk össze az elemet az adott pozícióban lévővel

        if kozep_elem == ertek:
            return kozep_index      # Megtaláltuk!
        if kozep_elem < ertek:
            ah = kozep_index + 1    # Használjuk a felső ROI-t
        else:
            fh = kozep_index        # Használjuk az alsó ROI-t

def ismeretlen_szavak_keresese(szoveg, szavak):
    """ Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne a szókincsben. """
    eredmeny = []
    for w in szavak:
        if (binaris_kereses(szoveg, w) == -1):
            eredmeny.append(w)
    return eredmeny


def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

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

nagyobb_szokincs = szavak_betoltese_fajlbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/szokincs.txt")
konyv_szavai = szavak_a_konyvbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/alice.txt")

t0 = time.perf_counter()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.perf_counter()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))

# print(binaris_kereses(nagyobb_szokincs, "magic"))