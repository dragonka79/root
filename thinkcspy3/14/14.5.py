# Duplikált elemek eltávolítása rendezett listából

def szomszedos_dupl_eltavolit(xs):
    dupl_nelkul = []
    for v in xs:
        if v not in dupl_nelkul:
            dupl_nelkul.append(v)
    return dupl_nelkul

# print(szomszedos_dupl_eltavolit([1,2,3,3,3,3,5,6,9,9]))

def szavak_a_konyvbol(fajlnev):
    """ Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját."""
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
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
    
osszes_szo = szavak_a_konyvbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/alice.txt")
osszes_szo.sort()
konyv_szavai = szomszedos_dupl_eltavolit(osszes_szo)
print("A könyvben {0} szó van. Csak {1} egyedi.".
format(len(osszes_szo), len(konyv_szavai)))
print("Az első 100 szó\n{0}".
format(konyv_szavai[:100]))