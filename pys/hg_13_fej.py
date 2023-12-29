# 13.2 Első file-unk

sajat_fajl = open("elso.txt", 'w')
sajat_fajl.write("Az első python fájlom!\n")
sajat_fajl.write("-------------------\n")
sajat_fajl.write("Hello Világ!\n")
sajat_fajl.close()


# 13.3.Fájl soronkénti olvasása

uj_kezelo = open("elso.txt", 'r') # File megnyitása olvasásra
while True:
    sor = uj_kezelo.readline()     # Olvas be a következő sort
    if len(sor) == 0:  # Ha nincs több olyan sor, amiben sortörés van
        break           # lépj ki a ciklusból
    # A láthatatlan else ág, itt dolgozza fel az aktuális sort
    print(sor, end = "")

uj_kezelo.close()   #Zárd be a file-t


# 13.4.Fájl átalakítása sorok listájává
# Elolvasunk egy file-t, berakjuk a sorokat egy listába, azokat már tudjuk ABC
# szerint rendezni és a rendezet listát berakjuk egy másik file-ba, így kapunk
# egy ABC szerint rendezett file-t

f = open("baratok.txt", 'r')
xs = f.readlines() #beolvassa az összes sort, és visszatér a sztringek listájával.
f.close()
print(xs)

xs.sort()
print(xs)

g = open("rendezett_baratok.txt", 'w')
for v in xs:
    g.write(v)
g.close()


# 13.5. A teljes fájl beolvasása
# Hány szó van a szövegben?

f = open("ext19a.txt")
tartalom = f.read()
f.close()

szavak = tartalom.split()
print("A file szavainak száma: {0}.".format(len(szavak)))

# 13.6.Bináris fájlok kezelése. Egy bináris file (kép, video, zip, stb) másolása

f = open("bin_copy_teszt.png", 'rb')    # rb = read binary
g = open("bin_copy_masolt.png", 'wb')   # wb = write binary

while True:
    buf = f.read(1024) # 1024 byte-nyi adatot másoljon egyszerre
    if len(buf) == 0:
        break           # ha a buffer üres akkor elfogyott a file
    g.write(buf)

f.close()
g.close()

# 13.7. Egy példa, szűrők. Soronként olvassa be a file-t, végez vmi szűrést.

import locale

locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása

def szuro(regifile, ujfile):
    bemenet = open(regifile, 'r')
    kimenet = open(ujfile, 'w')
    while True:
        szoveg = bemenet.readline()
        if len(szoveg) == 0:
            break
        if szoveg[0] == '#':
            continue
        szoveg = szoveg[0].upper() + szoveg[1:] # Nagy kezdőbetű
        kimenet.write(szoveg)


    bemenet.close()
    kimenet.close()


szuro("teszt20.txt", "teszt20_new.txt")

# 13.9.1 Egy pdf file letöltése a netről

import urllib.request

url = "http://www.ict.ru.ac.za/Resources/cspw/thinkcspy3/thinkcspy3.pdf"
cel_fajlnev = "thinkcspy3.pdf"

# urlretrieve: Elméletileg bármely tartalom letöltésésre használható, de
# pl. html-t nem tudok letölteni
urllib.request.urlretrieve(url, cel_fajlnev)


# 13.9.2 Egy netes file sztringbe olvasása és nyomtatása a képernyőre

import urllib.request

def weboldal(url):
    """ Visszatér a weboldal tartalmával.
        A tartalmat sztringgé alakítja, mielőtt visszatérne.
    """
    socket = urllib.request.urlopen(url)
    tartalom = str(socket.read())
    url_open.close()
    return tartalom

szoveg = weboldal("http://www.gnu.org/software/make/manual/make.txt")
print(szoveg)


# 13.11.1. Egy file-t beolvas és sorait fordított sorrendben írja be egy
# másik file-ba.

f = open("teszt20.txt", 'r')
h = f.readlines() # a file-t soronként bepakolom egy listába
h.reverse() # megfordítom a lista elemeinek, azaz a sorok sorrendjét
f.close()

g = open("teszt21.txt", 'w')
for i in h:
    g.write(i)
g.close()


# 13.11.2. beolvas egy fájlt, és csak azokat a sorait írja ki,
# melyek tartalmazzák az 'info' részsztringet

f = open("teszt20.txt", 'r')
h = f.readlines() # a file-t soronként bepakolom egy listába
f.close()
j = 'info'

for i in h:
    if j in i:
        print(i)


# 13.11.3. Sorszámozzunk be egy file-t, 4 karakter hosszan, a sorszámot balról
# 0-kal töltsük fel, az eredeti file sorai között legyen egy szóköz, ezt mentsük
# egy új file-ba.
# pl.: 0004 Eredeti negyedik sor


f = open("teszt20.txt", 'r')
h = f.readlines() # a file-t soronként bepakolom egy listába
e = len(h)
f.close()
# print(e)

g = open("teszt21.txt", 'w')
k = 1
while k <= e:
    for v in h:
        l = "{:04d}".format(k) #balról nullákkal töltöm fel a sorszámot
        n = l + ' '
        g.write(n + v)
        k += 1
g.close()


# 13.11.4. megszünteti az előző gyakorlat számozását: ennek egy beszámozott
# sorokat tartalmazó fájlt kellene beolvasnia, és egy másik fájlt előállítani
# a sorszámok nélkül.

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
