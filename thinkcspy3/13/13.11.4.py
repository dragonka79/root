# 1. megoldás, speciálisan az előző feladatra
# Felhasználjuk, hogy az 5-ik karakter a számozott sorokban szóköz

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/alice_sample_countered.txt")
g = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/alice_sample_not_countered.txt", "a")

while True:
    szoveg = f.readline()
    if len(szoveg) == 0:
        break
    szoveg = szoveg[5:]
    g.write(szoveg)

f.close()
g.close()

#### 2-ik megoldás, általánosan számozott soros szövegre

import locale


f = open("teszt21.txt", 'r')
h = f.readlines() # a file-t soronként bepakolom egy listába
f.close()

locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása
abc = "aábcdeéfghiíjklmnoóöőpqrtuúüűvwxyzs"
abc_upper = abc.upper()
g = open("teszt22.txt", 'w')

for v in h: # végigmegyünk a sorokon
    for i in v: # elindulunk a sorokban
        if i in abc or i in abc_upper:
            j = v.index(i)  # Az első szöveges karakter indexe a sorban
            s = v[j:] # s lista az eredeti sor első szöv. karakterétől
            g.write(s)
            break  # szakítja a belső for-t és lép a külső for-ra, azaz sorra

g.close()