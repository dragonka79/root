from unittest import teszt

napok = ['hétfő','kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap']
def nap_nev(x):
    if x in range(0, 7):
        return napok[x]
    else:
        return None


def nap_sorszam(nap):
    if nap in napok:
        return napok.index(nap)
    else:
        return None


# def napok_hozzaadasa(nap, index):
#     if nap in napok:
#         v = napok.index(nap)
#         k = v + index
#         l = k % 7
#         return 


def napok_hozzaadasa(nap, index):
    if nap in napok:
        # v = nap_sorszam(nap)
        # k = nap_sorszam(nap) + index
        # l = (nap_sorszam(nap) + index) % 7
        # n = nap_nev((nap_sorszam(nap) + index) % 7)
        return nap_nev((nap_sorszam(nap) + index) % 7)
    else:
        return None


teszt(napok_hozzaadasa("hétfő", 4) == "péntek")
teszt(napok_hozzaadasa("kedd", 0) == "kedd")
teszt(napok_hozzaadasa("kedd", 14) == "kedd")
teszt(napok_hozzaadasa("vasárnap", 100) == "kedd")
teszt(napok_hozzaadasa("vásárnap", 100) == None)
teszt(napok_hozzaadasa("vasárnap", -1) == "szombat")
teszt(napok_hozzaadasa("vasárnap", -7) == "vasárnap")
teszt(napok_hozzaadasa("kedd", -100) == "vasárnap")