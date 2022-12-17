# Megadja, hogy hány olyan szó van, amely benne van egy adott szövegben(könyv), de
# nincs benne egy adott szólistában.
# Mindkét szöveg lista esetén azok rendezésre kerülnek és nincsenek bennük
# duplikátumok

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

def szomszedos_dupl_eltavolit(xs):
    dupl_nelkul = []
    for v in xs:
        if v not in dupl_nelkul:
            dupl_nelkul.append(v)
    return dupl_nelkul

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

def ismeretlen_szavak_osszefesulessel(szokincs, szavak):
    """ Mind a szókincs és könyv szavai rendezettek kell, legyenek.
    Visszatérünk egy új szólistával, mely szavak benne vannak a könyvben,
    de nincsenek a szókincsben.
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(szokincs):
            eredmeny.extend(szavak[yi:])
            return eredmeny
        if yi >= len(szavak):
            return eredmeny
        if szokincs[xi] == szavak[yi]: # A szó benne van a szókincsben
            yi += 1
        elif szokincs[xi] < szavak[yi]: # Haladjon tovább
            xi += 1
        else: # Találtunk olyan szót, mely nincs a szókincsben
            eredmeny.append(szavak[yi])
            yi += 1

nagyobb_szokincs = szavak_betoltese_fajlbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/szokincs.txt")
osszes_szo = szavak_a_konyvbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/alice.txt")
t0 = time.perf_counter()
osszes_szo.sort()
szavak = szomszedos_dupl_eltavolit(osszes_szo)
hianyzo_szavak = ismeretlen_szavak_osszefesulessel(nagyobb_szokincs, szavak)
t1 = time.perf_counter()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))