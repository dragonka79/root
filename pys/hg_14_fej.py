# 14.2.1 A teljes keresés algoritmusa, keressük meg egy elem első előfordulását
# egy listában és térjünk vissza a listában elfoglalt indexével

from egyseg_teszt import teszt

baratok = ["Péter", "Zoltán", "János", "Kata", "Zita", "Sándor", "Panni"]

def teljes_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(teljes_kereses(baratok, "Zoltán") == 1)
    teszt(teljes_kereses(baratok, "Péter") == 0)
    teszt(teljes_kereses(baratok, "Panni") == 6)
    teszt(teljes_kereses(baratok, "Béla") == -1)

# print(teljes_kereses(baratok, "János"))
tesztkeszlet()


# 14.3.1 A 14.2-t használja, azokat a szavakat, egy adott listából,
# amelyek nem szerepelnek a könyv_szavaiban, azokat egy külön listába rakja:
# végigmegy a szólista minden szaván, ha egy szó nincs benne a könyvben, azaz a
# linearis kereses -1-gyel tér vissza, akkor azt a szót belerakja egy új listába

from egyseg_teszt import teszt

szokincs = ["alma", "esett", "fűre", "fáról", "alá", "a", "fel"]
konyv_szavai = "az alma a fáról le esett a fűre".split()

def ismeretlen_szavak_keresese(szokincs, szavak):
    """
    Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne
    a szókincsben.
    """
    eredmeny = []
    for w in szavak:
        if (linearis_kereses(szokincs, w) == -1):
            eredmeny.append(w)
    return eredmeny

def linearis_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(ismeretlen_szavak_keresese(szokincs, konyv_szavai) == ["az", "le"])
    teszt(ismeretlen_szavak_keresese([], konyv_szavai) == konyv_szavai)
    teszt(ismeretlen_szavak_keresese(szokincs, ["alma", "alá", "esett"]) == [])


tesztkeszlet()

# 14.3.2. # Betöljük a letöltött vocab.txt-t, szétdaraboljuk szavakká és egy
# új listába rakjuk, megszámoljuk, hogy hány szó van a listában + kiíratjuk az
# első 6 szót belőle

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = tartalom.split() # szavakra szedjük a tartalom nevű listát
    return szavak

nagyobb_szokincs = szavak_betoltese_fajlbol("vocab.txt")
print("A szókincsben {0} szó található, kezdve: \n {1}"
        .format(len(nagyobb_szokincs), nagyobb_szokincs[:6]))

# 14.3.3. Szótisztítás, átalakítás során az összes nagybetűs karaktert
# kisbetűssé konvertálja, az írásjel karaktereket és a számokat pedig szóközzé.
# Ezután szavakká töri a szöveget és a 'szavak' listájába rakja őket.

from egyseg_teszt import teszt

def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(szovegbol_szavak("Az én nevem Alice!") ==
                            ["az", "én", "nevem", "alice"])
    teszt(szovegbol_szavak('"Nem, Én soha!", mondta Alice.') ==
                            ["nem", "én", "soha", "mondta", "alice"])

tesztkeszlet()


# 14.3.4. Szótisztítás, átalakítás során az összes nagybetűs karaktert
# kisbetűssé konvertálja, az írásjel karaktereket és a számokat pedig szóközzé.
# Ezután szavakká töri a szöveget és a 'szavak' listájába rakja őket.

def szavak_a_konyvbol(fajlnev):
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")

print("A könyvben {0} szó található, az első 100 a következő:\n{1}"
        .format(len(konyv_szavai), konyv_szavai[:100]))


# 14.3.4. A 13.3.3 tovább lépve, az Alice könyvől olvasom be a szavakat,
# megtisztítom és megmondom, hogy hány szó szerepel benne

def szavak_a_konyvbol(fajlnev):
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")

print("A könyvben {0} szó található, az első 100 a következő:\n{1}"
        .format(len(konyv_szavai), konyv_szavai[:100]))


# 14.3.5. A 14.3.1. brutál verziója, az Alice könyvből, tisztítás után,
# megmondja, hogy hány szó nem szerepel a vocab.txt-ből a könyvben.
# Kiíratthatom ezeket a hiányzó szavakat + megmérem, hogy a program mennyi
# ideig fut

import time


def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

def ismeretlen_szavak_keresese(szokincs, szavak):
    """
    Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne
    a szókincsben.
    """
    eredmeny = []
    for w in szavak:
        if (linearis_kereses(szokincs, w) == -1):
            eredmeny.append(w)
    return eredmeny

def linearis_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1


def szavak_a_konyvbol(fajlnev):
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")
nagyobb_szokincs = szavak_betoltese_fajlbol("vocab.txt")
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
# print(hianyzo_szavak)

t0 = time.clock()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.clock()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))


# 14.4.1 A bináris keresés alap algoritmusa

from egyseg_teszt import teszt

xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]

def binaris_kereses(xs, ertek):
    """ Keressük meg és térjünk vissza az érték indexével az xs sorozatban. """
    ah = 0          # a ROI (range of interest) alsó határa
    fh = len(xs)    # ROI felső határa

    while True:
        if ah == fh:    # üres lista
            return -1
        # A következő összehasonlítás a ROI közepén kell legyen
        kozep_index = (ah + fh) // 2

        # Fogjuk a középső indexen lévő elemet
        kozep_elem = xs[kozep_index]

        #print("ROI[{0}:{1}](méret={2}), próba='{3}', érték='{4}'"
        #       .format(ah, fh, fh-ah, kozep_elem, ertek))

        # Hasonlítsuk össze az elemet az adott pozícióban lévővel

        if kozep_elem == ertek:
            return kozep_index      # Megtaláltuk!
        if kozep_elem < ertek:
            ah = kozep_index + 1    # Használjuk a felső ROI-t
        else:
            fh = kozep_index        # Használjuk az alsó ROI-t

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(binaris_kereses(xs, 20) == -1)
    teszt(binaris_kereses(xs, 99) == -1)
    teszt(binaris_kereses(xs, 1) == -1)
    for (i, v) in enumerate(xs):
        teszt(binaris_kereses(xs, v) == i)

tesztkeszlet()


# 14.4.2. A 14.3.5 megoldása nem lineráris hanem bináris kereséssel

import time

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

def ismeretlen_szavak_keresese(szokincs, szavak):
    """
    Visszatérünk a könyv azon szavainak listájával, amelyek nincsenek benne
    a szókincsben.
    """
    eredmeny = []
    for w in szavak:
        if (binaris_kereses(szokincs, w) == -1):
            eredmeny.append(w)
    return eredmeny

def binaris_kereses(xs, ertek):
    """ Keressük meg és térjünk vissza az érték indexével az xs sorozatban. """
    ah = 0
    fh = len(xs)
    while True:
        if ah == fh:    # Ha a vizsgált terület üres
            return -1

        # A következő összehasonlítás a ROI közepén kell legyen
        kozep_index = (ah + fh) // 2

        # Fogjuk középső indexen lévő elemet
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


def szavak_a_konyvbol(fajlnev):
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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

konyv_szavai = szavak_a_konyvbol("alice_in_wonderland.txt")
nagyobb_szokincs = szavak_betoltese_fajlbol("vocab.txt")
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
# print(hianyzo_szavak)

t0 = time.clock()
hianyzo_szavak = ismeretlen_szavak_keresese(nagyobb_szokincs, konyv_szavai)
t1 = time.clock()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))


# 14.5.1. Rendezett listából szomszédos duplikátumok
# (= egymás mellett lévő azonos értékű elemek) eltávolítása, így egy olyan új
# listát kapok, amiben minden elem 1-szer szerepel

from egyseg_teszt import teszt

def szomszedos_dupl_eltavolit(xs):
    """ Visszatér egy új listával, amelyben a szomszédos
        duplikátumok el vannak távolítva az xs listából.
    """
    eredmeny = []
    aktualis_elem = None
    for e in xs:
        if e != aktualis_elem:
            eredmeny.append(e)
            aktualis_elem = e
    return eredmeny

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(szomszedos_dupl_eltavolit([1,2,3,3,3,3,5,6,9,9]) == [1,2,3,5,6,9])
    teszt(szomszedos_dupl_eltavolit([]) == [])
    teszt(szomszedos_dupl_eltavolit(["egy", "kis", "kis", "kölyök",  "kutya"]) ==
                           ["egy", "kis", "kölyök", "kutya"])

tesztkeszlet()

# 14.5.2. Alice könyvben lévő különböző szavak számlálása:
# 1. Berakom a könyv szavait egy listába.
# 2. Megtisztítom: csak betűket hagyok benne és minden karaktert kicsivé teszek
# 3. ABC szerint rendezem a megtisztított listát
# 4. Eltávolítom a duplikátumokat

def szomszedos_dupl_eltavolit(xs):
    """ Visszatér egy új listával, amelyben a szomszédos
        duplikátumok el vannak távolítva az xs listából.
    """
    eredmeny = []
    aktualis_elem = None
    for e in xs:
        if e != aktualis_elem:
            eredmeny.append(e)
            aktualis_elem = e
    return eredmeny


def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

osszes_szo = szavak_a_konyvbol("alice_in_wonderland.txt")
osszes_szo.sort()
konyv_szavai = szomszedos_dupl_eltavolit(osszes_szo)
print("A könyvben {0} szó van. Csak {1} egyedi."
                        .format(len(osszes_szo), len(konyv_szavai)))
print("Az első 100 szó\n{0}"
                        .format(konyv_szavai[:100]))


# 14.6. Sorbarendezett listák összefésülése. Van 2 rendezett listám és azokat
# egy listává fésülöm

from egyseg_teszt import teszt


xs = [1,3,5,7,9,11,13,15,17,19]
ys = [4,8,12,16,20,24]
zs = xs+ys
zs.sort()

def osszefesul(xs, ys):
    """
    Összefésüli a rendezett xs és ys listákat. Visszatér a rendezett eredménnyel.
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):       # Ha az xs lista végére értünk
            eredmeny.extend(ys[yi:]) # Az ys-ben még maradt elemeket másolom
            return eredmeny

        if yi >= len(ys):
            eredmeny.extend(xs[xi:])
            return eredmeny

        # Ha mindkét listában vannak még elemek, akkor a kisebbik elemet
        # másoljuk az eredmény listába
        if xs[xi] <= ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            eredmeny.append(ys[yi])
            yi += 1

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """

    teszt(osszefesul(xs, []) == xs)
    teszt(osszefesul([], ys) == ys)
    teszt(osszefesul([], []) == [])
    teszt(osszefesul(xs, ys) == zs)
    teszt(osszefesul([1,2,3], [3,4,5]) == [1,2,3,3,4,5])
    teszt(osszefesul(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
                    ["cica", "cica", "egér", "kakas", "kutya", "medve"])

tesztkeszlet()

# 14.7.1 Adva van 2 rendezett lista(lehetnek benne azonos elemek), visszatér egy
# olyan listával amely elemei mindkét listában szerepelnek

xs = [1,3,4,5,5,7,8,9,11,13,15,17,19,20]
ys = [4,5,5,8,12,16,17,20,24]

def osszefesul(xs, ys):
    """
    Visszatér a mindkét listában szereplő elemekkel
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):       # Ha az xs lista végére értünk
            return eredmeny
        if yi >= len(ys):
            return eredmeny

        if xs[xi] == ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        else:
            yi += 1

print(osszefesul(xs, ys))


# 14.7.2 Adva van 2 rendezett lista(lehetnek benne azonos elemek), visszatér egy
# olyan listával amely elemei csak az első listában szerepelnek

xs = [1,3,4,5,5,7,8,9,11,13,15,17,19,20,21,22,23]
ys = [4,5,5,8,12,16,17,20]

def osszefesul(xs, ys):
    """
    Visszatér a csak első(xs) listában szereplő elemekkel
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):       # Ha az xs lista végére értünk
            return eredmeny
        if yi >= len(ys):
            eredmeny.extend(xs[xi:])
            return eredmeny

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            yi += 1

print(osszefesul(xs, ys))


# 14.7.3 Adva van 2 rendezett lista(lehetnek benne azonos elemek), visszatér egy
# olyan listával amely elemei csak a második listában szerepelnek

xs = [1,3,4,5,5,7,8,9,11,13,15,17,19,20,21,22,23]
ys = [4,5,5,8,12,16,17,20]

def osszefesul(xs, ys):
    """
    Visszatér a csak a második listában(ys) szereplő elemekkel
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):       # Ha az xs lista végére értünk
            return eredmeny
        if yi >= len(ys):
            eredmeny.extend(xs[xi:])
            return eredmeny

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif ys[yi] < xs[xi]:
            eredmeny.append(ys[yi])
            yi += 1
        else:
            xi += 1

print(osszefesul(xs, ys))


# 14.7.4 Adva van 2 rendezett lista(lehetnek benne azonos elemek), visszatér egy
# olyan listával amely elemei vagy az egyik vagy a másik listában szerepel.

xs = [1,3,4,5,5,7,8,9,11,13,15,17,19,20,21,22,23]
ys = [4,5,5,8,12,16,17,20]

def osszefesul(xs, ys):
    """
    Visszatér a nem a mindkét listában szereplő elemekkel.
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):
            eredmeny.extend(ys[yi:])     # Ha az xs lista végére értünk
            return eredmeny
        if yi >= len(ys):
            eredmeny.extend(xs[xi:])
            return eredmeny

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            eredmeny.append(ys[yi])
            yi += 1

print(osszefesul(xs, ys))


# 14.7.5 Adva van 2 rendezett lista(lehetnek benne azonos elemek), visszatér egy
# olyan listával amely elemei az első listában szerepelnek, de ha egy elem
# mindkét listában szerepel, akkor annak az elemnek az előfordulási száma
# az első listában az előfordulása szám mínusz a másodikban, ha ez a szám
# pozitív
# Ez pont ugyanaz mint a 14.7.2

xs = [5,7,11,11,11,12,13]
ys = [7,8,11]

def osszefesul(xs, ys):
    """
    Visszatér a csak első(xs) listában szereplő elemekkel
    """
    eredmeny = []
    xi = 0  # Ez az index ami fut xs-en
    yi = 0  # Ez az index, ami fut ys-en

    while True:
        if xi >= len(xs):       # Ha az xs lista végére értünk
            return eredmeny
        if yi >= len(ys):
            eredmeny.extend(xs[xi:])
            return eredmeny

        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            yi += 1

print(osszefesul(xs, ys))

# 14.7.6. Az összefésült változat: Alice könyvben szereplő, de a vocab.txt-ben
# nem szereplő szavaknak.
# Ez annyiban különbözik a lineáris és a bináris megoldástól, hogy a
# duplikátumok el vannak távolítva és mehet rá az összefésülés algoritmusa.

import time


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

        if szokincs[xi] == szavak[yi]:  # A szó benne van a szókincsben
            yi += 1


        elif szokincs[xi] < szavak[yi]: # Haladjon tovább
            xi += 1

        else:                 # Találtunk olyan szót, mely nincs a szókincsben
            eredmeny.append(szavak[yi])
            yi += 1

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev, "r")
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak


def szomszedos_dupl_eltavolit(xs):
    """ Visszatér egy új listával, amelyben a szomszédos
        duplikátumok el vannak távolítva az xs listából.
    """
    eredmeny = []
    aktualis_elem = None
    for e in xs:
        if e != aktualis_elem:
            eredmeny.append(e)
            aktualis_elem = e
    return eredmeny


def szovegbol_szavak(szoveg):
    """ Visszaadja a szavak listáját, eltávolítva az összes írásjelt és minden
        szót kisbetűssé alakít.
    """
    # A maketrans egy az egyben helyettesíti a karaktereket, pl A->a, 0->' ',
    #ezért van annyi szóköz a második paraméter string végén
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
    """
    Olvassa be a könyvet a megadott fájlból, és adja vissza a szavak listáját.
    """
    f = open(fajlnev, 'r')
    tartalom = f.read()
    f.close()
    szavak = szovegbol_szavak(tartalom)
    return szavak

osszes_szo = szavak_a_konyvbol("alice_in_wonderland.txt")
t0 = time.clock()
osszes_szo.sort() # Itt ezen a ponton a könyv kitisztítva és rendezve
konyv_szavai = szomszedos_dupl_eltavolit(osszes_szo) # duplikátumok eltávolítva
nagyobb_szokincs = szavak_betoltese_fajlbol("vocab.txt")
hianyzo_szavak = ismeretlen_szavak_osszefesulessel(nagyobb_szokincs,konyv_szavai)
t1 = time.clock()
print("{0} ismeretlen szó van.".format(len(hianyzo_szavak)))
print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))


# 14.8.1 Nyolc királynő probléma, első rész.
# A királynők egy átlón állnak-e, ha adott (x, y) koordinátán állnak?

from egyseg_teszt import teszt


def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(ugyanazon_az_atlon(5,2,2,0) == False)
    teszt(ugyanazon_az_atlon(5,2,3,0) == True)
    teszt(ugyanazon_az_atlon(5,2,4,3) == True)
    teszt(ugyanazon_az_atlon(5,2,4,1) == True)

tesztkeszlet()


# 14.8.2 Nyolc királynő probléma, első rész.
# True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
# a tőle balra levőkkel.

from egyseg_teszt import teszt


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
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

tesztkeszlet()


# 14.8.3 Nyolc királynő probléma, első rész vége.
# A teljes program arra, hogy megnézzük, hogy a lerakott királynők a táblán
# nem ütik-e egymást

from egyseg_teszt import teszt


def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(van_utkozes([6,4,2,0,5,7,1,3]) == False) # A fenti megoldás
    teszt(van_utkozes([4,6,2,0,5,7,1,3]) == True)# Felcseréljük az első két sort
    teszt(van_utkozes([0,1,2,3]) == True)       # Kipróbáljuk egy 4x4 sakktáblán
    teszt(van_utkozes([2,0,3,1]) == False)       # Megoldás 4x4-es esetben


tesztkeszlet()


# 14.9.1 Nyolc királynő probléma, második rész.
# Néhány megoldás megtalálása (az össz 92-ből) a 8 királynő problémára, ezek
# között lehetnek egyformák

def main():
    import random
    rng = random.Random()

    bd = list(range(8)) # Létrehozza a [0, 1, 2, 3, 4, 5, 6, 7] kezdeti permutációt
    talalat_szama = 0
    proba = 0
    while talalat_szama <= 10:
        rng.shuffle(bd) # Véletlenszerűen keverd meg a kezdeti lista elemeit
        proba += 1
        if not van_utkozes(bd):
            print("Megoldás: {0}, próbálkozás: {1}.". format(bd, proba))
            proba = 0
            talalat_szama += 1


def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

main()


# 14.9.2. A Nyolc királynő probléma, végső változat.
# Mind a 92 különböző megoldás megtalálása a nyolc királynő problémára,
# A main() függvény while ciklusát írtam át, hogy minden megoldás meglegyen.

def main():
    """   A nyolc királynő probléma mind a 92 különböző megoldása.   """
    import random
    rng = random.Random()

    vezer_lista = []
    talalat_szama = 0
    while talalat_szama < 92:
        bd = list(range(8))
        rng.shuffle(bd)
        if not van_utkozes(bd) and not bd in vezer_lista:
            vezer_lista.append(bd)
            print(f"{talalat_szama + 1}.", bd)
            talalat_szama += 1
    vezer_lista.sort()
    return vezer_lista

def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

# print(main())
main()


# 14.11.2. A 4/12/16 királynő probléma.
# 4 x 4 = 2
# 12 x 12 = 14200

import time


def main():
    """   A nyolc királynő probléma mind a 92 különböző megoldása.   """
    import random
    rng = random.Random()

    vezer_lista = []
    talalat_szama = 0
    t0 = time.clock()
    while talalat_szama < 14200:
        bd = list(range(12))
        rng.shuffle(bd)
        if not van_utkozes(bd) and not bd in vezer_lista:
            vezer_lista.append(bd)
            print(f"{talalat_szama + 1}.", bd)
            talalat_szama += 1
    t1 = time.clock()
    print("Ez {0:.4f} másodpercet vett igénybe.".format(t1-t0))
    vezer_lista.sort()
    return vezer_lista

def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van

def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx

# print(main())
main()

# 14.11.4.a Tükrözzük az y-tengelyre (azaz a tábla függőleges) az n
# királynő probléma egy megoldását.

from egyseg_teszt import teszt

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

def y_axis(megoldas):
    yaxis = megoldas[:]
    yaxis.reverse()
    return yaxis

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(y_axis([0, 4, 7, 5, 2, 6, 1, 3]) == [3, 1, 6, 2, 5, 7, 4, 0])
    teszt(y_axis([2, 0, 3, 1]) == [1, 3, 0, 2])

tesztkeszlet()
# print(y_axis(megoldas))



# 14.11.4.b Tükrözzük az x-tengelyre (azaz a tábla vízszintes aljára) az n
# királynő probléma egy megoldását.

from egyseg_teszt import teszt


def x_axis(megoldas):
    xaxis = []
    xaxis_meg = megoldas[:]
    for i in range(len(megoldas)):
        xaxis_meg[i] = (len(megoldas) - 1) - megoldas[i]
        xaxis.append(xaxis_meg[i])
    return xaxis

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(x_axis([0, 4, 7, 5, 2, 6, 1, 3]) == [7, 3, 0, 2, 5, 1, 6, 4])
    teszt(x_axis([7, 1, 3, 0, 6, 4, 2, 5]) == [0, 6, 4, 7, 1, 3, 5, 2])
    teszt(x_axis([2, 0, 3, 1]) == [1, 3, 0, 2])
tesztkeszlet()


# 14.11.4.c.1. Forgassuk el 90 fokkal a táblát.

from egyseg_teszt import teszt

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

def rotate_90(megoldas):
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    return rotate90

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(ninety_90([2, 0, 3, 1]) == [2, 0, 3, 1])
    teszt(ninety_90([0, 4, 7, 5, 2, 6, 1, 3]) == [2, 5, 3, 1, 7, 4, 6, 0])

# tesztkeszlet()

print(rotate_90(megoldas))


# 14.11.4.c.2. Forgassuk el 180 fokkal a táblát.

from egyseg_teszt import teszt

# megoldas = [2, 0, 3, 1]

def rotate_180(megoldas):
    """ Fordítsd meg a listát és az elemek új értéke legyen:
    tábla mérete - mostani értékük
    """
    rotate180 = []
    rotate180_meg = megoldas[:]
    rotate180_meg.reverse()
    for i in rotate180_meg:
        rotate180.append(len(megoldas) - 1 - i)
    return rotate180

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(rotate_180([2, 0, 3, 1]) == [2, 0, 3, 1])
    teszt(rotate_180([0, 4, 7, 5, 2, 6, 1, 3]) == [4, 6, 1, 5, 2, 0, 3, 7])

tesztkeszlet()

# print(rotate_180(megoldas))

# 14.11.4.c.3. Alternatív megoldás 14.11.4.c.2-re, bonyolultabb.

from egyseg_teszt import teszt

# megoldas = [2, 0, 3, 1]

def rotate_180(megoldas):
    """ Keresd meg a legnagyobb indexű elemet és rakd be az új lista végére
    a 'tábla mérete - mostani értéke' mértékkel. Menj rá a következő legnagyobb
    értékre és csináld mint az előbb. Ezt addig folytasd amíg van elem a kezdeti
    listában.
    """
    rotate180 = []
    x = len(megoldas) - 1
    for i in range(x, -1, -1):
        y = megoldas[i]
        rotate180.append(x - y)
    return rotate180

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(rotate_180([2, 0, 3, 1]) == [2, 0, 3, 1])
    teszt(rotate_180([0, 4, 7, 5, 2, 6, 1, 3]) == [4, 6, 1, 5, 2, 0, 3, 7])

tesztkeszlet()

# print(rotate_180(megoldas))


# 14.11.4.c.4. Forgassuk el 270 fokkal a táblát.

from egyseg_teszt import teszt

# megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

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

# print(rotate_270(megoldas))


# 14.11.4.0.1. Tükrözzük a táblát a jobb (/) átlóra. Felcseréjük az értékeket
# és az indexeket.

from egyseg_teszt import teszt

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

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
        mirrorright.append(megoldas.index(z))
        z += 1
    return mirrorright


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(mirror_right([2, 0, 3, 1]) == [1, 3, 0, 2])
    teszt(mirror_right([0, 4, 7, 5, 2, 6, 1, 3]) == [0, 6, 4, 7, 1, 3, 5, 2])

tesztkeszlet()

# print(mirror_right(megoldas))

# 14.11.4.0.2. n királynő probléma. Tükrözzük a táblát a bal (\) átlóra.
# Keresd meg a legnagyobb
# értékű elemet és rakd az új lista végére '(n - 1) - régi index' értékkel

from egyseg_teszt import teszt

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

# print(mirror_left(megoldas))


# 14.11.4.d Az n királynő probléma egy szimmetriacsaládja

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

def n_queen_symmetries(megoldas):
    """   Az n királynő probléma egy szimmetriacsaládja   """

    symmetries = []
    symmetries.append(megoldas)

# Tükrözés az x-tengelyre
    yaxis = megoldas[:]
    yaxis.reverse()
    symmetries.append(yaxis)

# Tükrözés az y-tengelyre
    xaxis = []
    xaxis_meg = megoldas[:]
    for i in range(len(megoldas)):
        xaxis_meg[i] = (len(megoldas) - 1) - megoldas[i]
        xaxis.append(xaxis_meg[i])
    symmetries.append(xaxis)

# Elforgatás 90 fokkal
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    symmetries.append(rotate90)

# Elforgatás 180 fokkal
    rotate180 = []
    rotate180_meg = megoldas[:]
    rotate180_meg.reverse()
    for i in rotate180_meg:
        rotate180.append(len(megoldas) - 1 - i)
    symmetries.append(rotate180)

# Elforgatás 270 fokkal
    rotate270 = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        y = x - megoldas.index(z)
        rotate270.append(y)
        z += 1
    symmetries.append(rotate270)

#Tükrözés a bal(\) szimmetria átlóra
    mirrorleft = []
    x = len(megoldas) - 1
    z = x
    while z != -1:
        y = x - megoldas.index(z)
        mirrorleft.append(y)
        z -= 1
    symmetries.append(mirrorleft)

#Tükrözés a jobb(/) szimmetria főátlóra
    mirrorright = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        mirrorright.append(megoldas.index(z))
        z += 1
    symmetries.append(mirrorright)
    return symmetries

print(n_queen_symmetries(megoldas))


# 14.11.4.e Az n királynő probléma egyedi családba tartozó megoldásai
# A program listázhatja az összes megoldást, ehhez a 22-ik és 28-ik sort
# be kell kapcsolni.
#! n értékének változtatásával (20-ik sor) a 'talalat_szama' változó
# felső határát a while ciklus fejlécében (23-ik sor) is változtatni kell!
# 5 -> 10 | 6 -> 4 | 7 -> 40 | 8 -> 92 | 9 -> 352 | 10 -> 724 | 11 ->2680
# 12 -> 14200

import time


def main():
    """   Az n királynő probléma különböző megoldásai.   """
    import random
    rng = random.Random()

    global vezer_lista
    vezer_lista = []
    global n
    n = 9
    talalat_szama = 0
    # print(f"\nAz n királynő probléma összes megoldása n = {n} esetén:\n")
    while talalat_szama < 352:
        bd = list(range(n))
        rng.shuffle(bd)
        if not van_utkozes(bd) and not bd in vezer_lista:
            vezer_lista.append(bd)
            # print('{0:<4}'.format(talalat_szama + 1), bd)
            talalat_szama += 1
    vezer_lista.sort()
    return vezer_lista


def van_utkozes(sakktabla):
    """ Meghatározzuk, hogy van-e rivális az átlóban.
        Feltételezzük, hogy a sakktábla egy permutációja az oszlop számoknak,
        ezért nem kifejezetten ellenőrizzük a sor vagy oszlop ütközéseket.
    """
    for col in range(1,len(sakktabla)):
        if oszlop_utkozes(sakktabla, col):
            return True
    return False


def oszlop_utkozes(bs, c):
    """
    True-val tér vissza, hogyha a c oszlopban lévő királynő ütközik
    a tőle balra levőkkel.
    """
    for i in range(c):     # Nézd meg az összes oszlopot a c-től balra
        if ugyanazon_az_atlon(i, bs[i], c, bs[c]):
            return True

    return False           # Nincs ütközés, a c oszlopban biztonságos helyen van


def ugyanazon_az_atlon(x0, y0, x1, y1):
    """ Az (x0, y0) királynő ugyanazon az átlón van-e (x1, y1) királynővel? """
    dy = abs(y1 - y0)   # Kiszámoljuk y távolságának abszolút értékét
    dx = abs(x1 - x0)   # Kiszámoljuk x távolságának abszolút értékét
    return dy == dx     # Ütköznek, ha dy == dx


def n_queen_symmetries(megoldas):
    """   Az n királynő probléma egy szimmetriacsaládja   """

    symmetries = []
    symmetries.append(megoldas)

# Tükrözés az x-tengelyre
    yaxis = megoldas[:]
    yaxis.reverse()
    symmetries.append(yaxis)

# Tükrözés az y-tengelyre
    xaxis = []
    xaxis_meg = megoldas[:]
    for i in range(len(megoldas)):
        xaxis_meg[i] = (len(megoldas) - 1) - megoldas[i]
        xaxis.append(xaxis_meg[i])
    symmetries.append(xaxis)

# Elforgatás 90 fokkal
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    symmetries.append(rotate90)

# Elforgatás 180 fokkal
    rotate180 = []
    rotate180_meg = megoldas[:]
    rotate180_meg.reverse()
    for i in rotate180_meg:
        rotate180.append(len(megoldas) - 1 - i)
    symmetries.append(rotate180)

# Elforgatás 270 fokkal
    rotate270 = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        y = x - megoldas.index(z)
        rotate270.append(y)
        z += 1
    symmetries.append(rotate270)

#Tükrözés a bal(\) szimmetria átlóra
    mirrorleft = []
    x = len(megoldas) - 1
    z = x
    while z != -1:
        y = x - megoldas.index(z)
        mirrorleft.append(y)
        z -= 1
    symmetries.append(mirrorleft)

#Tükrözés a jobb(/) szimmetria főátlóra
    mirrorright = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        mirrorright.append(megoldas.index(z))
        z += 1
    symmetries.append(mirrorright)
    return symmetries

t0 = time.clock()
main()
# print(vezer_lista)
queen_fundamental = []
vezer_temp = vezer_lista[:]
while len(vezer_temp) != 0:
    for i in vezer_temp:
        symmetry_temp = []
        queen_fundamental.append(i)
        symmetry_temp = n_queen_symmetries(i)
        for j in symmetry_temp:
            if j in vezer_temp:
                vezer_temp.remove(j)

queen_fundamental.sort()
print(f"\nAz n királynő probléma egyedi megoldásai n = {n} esetén:\n")
for i in queen_fundamental:
    print('{0:<4}{1}'.format(queen_fundamental.index(i) + 1, i))
t1 = time.clock()
print("\nA program teljes futási ideje:{0:.4f} másodperc".format(t1-t0))


# 14.11.5.a

import random


def lotto_huzas():
    lottohuzas = []
    while len(lottohuzas) != 5:
        x = random.randint(1, 49)
        if not x in lottohuzas:
            lottohuzas.append(x)
    return lottohuzas

print(lotto_huzas())


# 14.11.5.b

import random
from egyseg_teszt import teszt


szelveny = [7, 17, 37, 19, 23, 43]

def lotto_huzas():
    lottohuzas = []
    while len(lottohuzas) != 5:
        x = random.randint(1, 49)
        if not x in lottohuzas:
            lottohuzas.append(x)
    return lottohuzas

def lotto_talalat(huzas, szelveny):
    k = 0
    for i in szelveny:
        if i in huzas:
            k += 1
    return k


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(lotto_talalat([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]) == 3)
    teszt(lotto_talalat([1, 2, 3, 4, 5, 6], [7, 17, 37, 19, 23, 43]) == 0)
    teszt(lotto_talalat([13, 17, 37, 19, 23, 43], [13, 17, 37, 19, 23, 43]) == 6)

lottohuzas = lotto_huzas()
print(lottohuzas)
print(lotto_talalat(lottohuzas, szelveny))
tesztkeszlet()

# 14.11.5.c

import random
from egyseg_teszt import teszt


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def lotto_huzas():
    lottohuzas = []
    while len(lottohuzas) != 5:
        x = random.randint(1, 49)
        if not x in lottohuzas:
            lottohuzas.append(x)
    return lottohuzas

def lotto_talalatok(huzas, my_tickets):
    nyeremeny = []
    for i in my_tickets:
        k = 0
        for j in i:
            if j in huzas:
                k += 1
        nyeremeny.append(k)
    return nyeremeny


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(lotto_talalatok([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

lottohuzas = lotto_huzas()
print(lottohuzas)
print(lotto_talalatok(lottohuzas, my_tickets))
tesztkeszlet()


# 14.11.5.d

from egyseg_teszt import teszt


szelveny = [41, 2, 7, 11, 1, 13]

def primek_szama(szelveny):
    """
    Visszaadja, hogy egy pozitív egészeket tartalmazó listában hány darab
    prímszám van
    """
    k = 0
    for i in szelveny:
        if i == 1:
            continue
        elif i == 2:
            k += 1
            continue
        else:
            for j in range(2, i + 1):
                if j == i:
                    k += 1
                elif i % j == 0:
                    break
                j += 1
    return k

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(primek_szama([42, 4, 7, 11, 1, 13]) == 3)
    teszt(primek_szama([1, 4, 8, 10, 42, 46]) == 0)
    teszt(primek_szama([1, 2, 3, 4, 5, 6]) == 3)

# print(primek_szama(szelveny))
tesztkeszlet()


# 14.11.5.e

from egyseg_teszt import teszt


my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

primek = [2,3,5,7,11,13,17,19,23,27,29,31,37,41,43,49]

def hianyzo_primek(my_tickets):
    ticket_numbers = []

    # Egy listába rakja a my_tickets elemeit és rendezi
    for i in my_tickets:
        ticket_numbers.extend(i)
        ticket_numbers.sort()
        numbers_pure = []

    #Kiszedi a duplikált elemeket a ticket_numbers-ből
    aktualis_elem = None
    for e in ticket_numbers:
        if e != aktualis_elem:
            numbers_pure.append(e)
            aktualis_elem = e

    # Visszatér a csak a második listában(primek) szereplő elemekkel
    eredmeny = []
    xi = 0  # Ez az index ami fut numbers_pure-on
    yi = 0  # Ez az index, ami fut primek-en

    while True:
        if xi >= len(numbers_pure):
            return eredmeny
        if yi >= len(primek):
            eredmeny.extend(numbers_pure[xi:])
            return eredmeny

        if numbers_pure[xi] == primek[yi]:
            xi += 1
            yi += 1
        elif primek[yi] < numbers_pure[xi]:
            eredmeny.append(primek[yi])
            yi += 1
        else:
            xi += 1
    return eredmeny
def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(hianyzo_primek(my_tickets) == [3, 27, 29])

# print(hianyzo_primek(my_tickets))
tesztkeszlet()
