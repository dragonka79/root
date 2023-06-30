from teszt import teszt
import sys
sys.path.append("C:/Users/A44793837/OneDrive - Deutsche Telekom AG/python/")


def plusz_gyumolcs(keszlet, gyumolcs, mennyiseg=0):
    if gyumolcs in keszlet:
        keszlet[gyumolcs] += mennyiseg
    else:
        keszlet[gyumolcs] = 0
        keszlet[gyumolcs] += mennyiseg
    return keszlet


uj_keszlet = {}
plusz_gyumolcs(uj_keszlet, "eper", 10)
teszt("eper" in uj_keszlet)
teszt(uj_keszlet["eper"] == 10)
plusz_gyumolcs(uj_keszlet, "eper", 25)
teszt(uj_keszlet["eper"] == 35)

plusz_gyumolcs(uj_keszlet, "alma", 20)
plusz_gyumolcs(uj_keszlet, "alma", 5)
print(uj_keszlet)
del uj_keszlet["alma"]
print(uj_keszlet)

# ubunminttt2
