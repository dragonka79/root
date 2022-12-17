# 14.3.3. Szótisztítás, átalakítás során az összes nagybetűs karaktert
# kisbetűssé konvertálja, az írásjel karaktereket és a számokat pedig szóközzé.
# Ezután szavakká töri a szöveget és a 'szavak' listájába rakja őket.


import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

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

teszt(szovegbol_szavak("Az én nevem Alice!") == ["az", "én", "nevem", "alice"])
teszt(szovegbol_szavak('"Nem, Én soha!", mondta Alice.') ==
["nem", "én", "soha", "mondta", "alice"])
