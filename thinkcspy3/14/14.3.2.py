# 14.3.2. # Betöljük a letöltött szokincs.txt-t, szétdaraboljuk szavakká és egy
# új listába rakjuk, megszámoljuk, hogy hány szó van a listában + kiíratjuk az
# első 6 szót belőle

def szavak_betoltese_fajlbol(fajlnev):
    """ Szavak olvasása a megadott fájlból, visszatér a szavak listájával. """
    f = open(fajlnev)
    tartalom = f.read()
    f.close()
    szavak = tartalom.split()
    return szavak

nagyobb_szokincs = szavak_betoltese_fajlbol("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/14/szokincs.txt")
# print("A szókincsben {0} szó található, kezdve: \n {1} "
# .format(len(nagyobb_szokincs), nagyobb_szokincs[:6]))

print(f"A szókincsben {len(nagyobb_szokincs)} szó található, kezdve: \n {nagyobb_szokincs[:6]} ")