# 8.2.1 Csupa nagybetűre változtat karaktersorozatot

ss = "Hello, World!"
tt = ss.upper()
print(tt)


# 8.2.2 Csupa kisbetűre változtat karaktersorozatot

ss = "Hello, World!"
tt = ss.lower()
print(tt)


# 8.2.3 Nagy kezdőbetűsre változtat karaktersorozatot

ss = "Hello, World!"
tt = ss.capitalize()
print(tt)


# 8.2.4 Betűnagyságot cserél (kisbetűt nagybetűre, nagybetűt kisbetűre)
# egy karaktersorozatban

ss = "Hello, World!"
tt = ss.swapcase()
print(tt)


# 8.3.1 Kiírja egy karakterláncban az első karakterét

gyumolcs = "banán"
t = gyumolcs[0]     # 0-tól kezdődik az indexelés számozása
print(t)


# 8.3.2. Kiírja, azaz párokba szedi, hogy a karaktereknek egy karakter
# sorozatban mi az indexe

gyumolcs = "banán"
index_lista = list(enumerate(gyumolcs))
print(index_lista)


# 8.3.4. Visszaadja egy listában az x-ik indexű elemet


primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
p4 = primek[4]
print(p4)

baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
b3 = baratok[3]
print(b3)


# 8.3.5. Visszaadja egy listában az utolsó indexű elemet, 2 változat


primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
hossz = len(primek)
utolso = primek[hossz - 1]
print(utolso)


baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
utolso = baratok[-1]    # negatív index, visszafele számol
print(utolso)


# 8.5.1 Lista bejárása, 2 változat

i = 0
gyumolcs = "banán"

while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1


for c in gyumolcs:
    print(c)


# 8.5.2 Karakersorozat és lista összefűzése

elotagok = 'kék '
utotagok_listaja = ['bicikli', 'esernyő', 'labda']


for utotagok in utotagok_listaja:
        print(elotagok + utotagok)


# 8.6.1 Szeletelés karakter sorozatban

s = "A Karib-tenger kalózai"
print(s[0:1])   # A 0-ik indexű karakter benne van de az első már nem
print(s[2:14])  # Karektersorozat szelet [2,14) között
print(s[:7])    # Karaktersorozat szelet [0,7) között
print(s[7:])   # Karaktersorozat szelet a 7-ik karaktertől az utolsóig
print(s[:])    # A teljes lista, 0 indextől a végéig

# 8.6.2 Szeletelés listában

baratok = ["Misi","Petra","Botond","Jani","Csilla","Peti","Norbi"]
print(baratok[2:4]) # ["Botond","Jani"]
print(baratok[:3])  # ["Misi","Petra","Botond"]
print(baratok[3:])  # ["Jani","Csilla","Peti","Norbi"]



# 8.7. Sztringek összehasonlítása, itt megmondja, hogy a szótárban a szó, amit
# begépelek előrébb vagy hátrébb van mint a szó amihez hasonlítok.

import locale

# Minden karaktert kicsivé teszünk, mert a nagy karakterek előznek.

be = input("A szavad: ")
be_lower = be.lower()
szo = "banán"
szo_lower = szo.lower()


locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása

k = locale.strcoll(be_lower, szo_lower)  # a két sztring összehasonlítása
if k < 0:
    print("A szavad, a(z) " + be + ", a banán elé jön.")
elif k > 0:
    print("A szavad, a(z) " + be + ", a banán után jön.")
else:

    print("Nem, nincs banánunk!")


# 8.8. 'Jello, World!' létrehozása a 'Hello, World!'-ből.
# Karakter láncban nem lehet karaktert cserélni.

h = 'Hello, World!'
j = 'J' + h[1:]
print(h)
print(j)


# 8.9. Not in operátor.

import sys


s = "Hogyan Gondolkodj Úgy Mint Egy Programozó"

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)



def maganhangzo_torles(s):
    """  Kiszedi  egy stringből a magánhangzókat.  """
    maganhangzok = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
    massalhangzos_s = ""
    for k in s:
        if k not in maganhangzok:
            massalhangzos_s += k
    return massalhangzos_s


def tesztkeszlet_maganhangzo_torles():
    """ A 8.8 modulhoz tartozó tesztkészlet futtatása.  """
    teszt(maganhangzo_torles("informatika") == "nfrmtk")
    teszt(maganhangzo_torles("aábeéiífoóöőujúüűpAÁEÉIÍOÓÖŐUÚÜŰs") == "bfjps")


# print(maganhangzo_torles(s))
tesztkeszlet_maganhangzo_torles()


# 8.10 Teljes keresés, aka Heuréka keresés aka rövidzár kiértékelés.
# Ha megtalálja az adott karaktert először egy sztringben akkor visszaadja az
# indexét és kilép

import sys

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


szoveg = "python"
k = "o"


def kereses(szoveg, k):
    """
      Megkeresi a k karaktert a szövegben (szoveg) és visszatér annak indexével.
      A visszatérési érték -1, ha a k karakter nem szerepel a szövegben.
    """
    i = 0
    while i < len(szoveg):
        if szoveg[i] == k:
            return i
        i += 1
    return -1


def tesztkeszlet_kereses():
    """ A 8.9 modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(kereses("Informatika", "o") == 3)
    teszt(kereses("Informatika", "I") == 0)
    teszt(kereses("Informatika", "a") == 6)
    teszt(kereses("Informatika", "x") == -1)


# print(kereses(szoveg, k))
tesztkeszlet_kereses()


# 8.11.1 Karakterek számlálása egy karakterláncban

szoveg = "banana"
k = 'a'

def betuk_szama(szoveg, k):
    darab = 0
    for i in szoveg:
        if i == k:
            darab += 1
    return darab

print(betuk_szama(szoveg, k))


# 8.11.2 Számjegyek számlálása 2.0

szam = 123456

def szamjegyek_szama(szam):
    darab = 0
    for i in str(szam):
        darab += 1
    return darab

print(szamjegyek_szama(szam))


# 8.11.3 Számjegyek számlálása 3.0

szam = "007"

def szamjegyek_szama(szam):
    darab = 0
    for i in szam:
        darab += 1
    return darab

print(szamjegyek_szama(szam))



# 8.13.1 Find, melyik indexen fordul elő előszőr egy x karakter egy sztringben.

ss = "Érdekes metódusai vannak a Python sztringeknek."

e = ss.find("e")
print(e)


# 8.13.2 Find, melyik indexen fordul elő előszőr egy x karakter egy sztringben
# ha a keresés egy adott index pozíciótól indul és nem a sztring kezdetétől

ss = "Érdekes metódusai vannak a Python sztringeknek."

e = ss.find("e", 4) # 5, mivel a bejárt szakasz a 'de'
print(e)


# 8.13.3 Find, melyik indexen fordul elő előszőr egy x karakter egy sztringben
# ha a keresés egy adott index interallumban történik

ss = "Érdekes metódusai vannak a Python sztringeknek."

e = ss.find("e", 18, 34 ) # -1, mivel a bejárt szakaszon nincs 'e'
print(e)


# 8.13.4 Find, melyik indexen fordul elő előszőr egy sztring egy másik sztringben.

ss = "banánán"

e = ss.find("nán") # 2, mivel a 'nán' kezdő 'n'-je a 2-ik indexű karakter
print(e)


# 8.14. Split, egy stringet szavakra bont, a köztük lévő whitespace, azaz
# (szóközöket, tabulátorokat, újsor) karaktereket eltávolítja.

ss = "Nos én sose csináltam mondta Alice"
szavak = ss.split()
print(szavak)


ss2 = "Nos, én sose csináltam, mondta Alice."
szavak2 = ss2.split()
print(szavak2)


# 8.15.1 Írásjelek eltávolítása szövegből

import string

szoveg = '"Nos, én sose csináltam!" - mondta Alice'


def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

print(irasjel_eltavolitas(szoveg))

# 8.15.2 Szöveg tisztítása , azaz csak a szavak listába pakolása,
# mentesen a whitespace-től és az írásjelektől. Először kiszedjük az írásjeleket,
# aztán szavakba tördeljük a whitespace-es szöveget és egy listába rakjuk őket.

import string


a_tortenetem = """
A pitonok nem méreggel ölnek, hanem kiszorítják a szuszt az áldozatukból.
A prédájuk köré tekerik magukat, minden egyes lélegzeténél egy kicsit
szorosabban, egészen addig, amíg a légzése abba nem marad. Amint megáll
a zsákmány szíve, lenyelik az egészet. A bunda és a tollazat kivételével
az egész állat a kígyó gyomrába lesz temetve. Mit gondolsz, mi történik
a lenyelt bundával, tollakkal, csőrökkel és tojáshéjakkal? A felesleges
'dolgok' távoznak, -- jól gondolod -- kígyó ÜRÜLÉK lesz belőlük!"""


def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli


szavak = irasjel_eltavolitas(a_tortenetem).split()
print(szavak)


# 8.16.1 Sztringek formázása 1.0

# {n} = A format metódusban az n-ik indexű helyen szereplő attribútum,
# azaz helyettesítő mezők vagy más néven formázó mezők

s1 = "A nevem {0}".format('Zoli')
print(s1)

# 8.16.2 Sztringek formázása 2.0

nev = 'Feri'
kor = 32
s2 = "A neve {1} és {0} éves.".format(kor, nev)
print(s2)

# 8.16.3 Sztringek formázása 3.0
#A {n} formázó mezők tartalmazhatnak formátum leírót, amely ':'-tal kezdődik,
# pl a lenti példában {:f}, azaz float típusra formázza a számot, amire az előtte
# lévő formátum mező indexe mutat, azaz az (n1 * n2)-t

n1 = 4
n2 = 5

s3 = "2**10 = {0} és {1} * {2} = {3:f}".format(2 ** 10, n1, n2, n1 * n2)
print(s3)


# 8.16.4 Sztringek formázása 4.0. A pi értéke 3 tizedesjegyig
#!figyel: .3f!
import math

print("A pi értéke 3 tizedesjegyig: {0:.3f}".format(math.pi))

# 8.16.5 Sztringek formázása 5.0.
#Igazítás balra, középre, jobbra illetve 12 hosszúságú mező
#lefoglalása az argumentumok számára

n0 = "Paris"
n1 = "Whitney"
n2 = "Hilton"

print("||| {0:<12} ||| {1:^12} ||| {2:>12} ||| Születési év: {3} |||"
        .format(n0, n1, n2, 1981))

# 8.16.6. Sztringek formázása 6.0.
# Decimális érték konvertálása hexadecimálissá

szam = 255
print("A decimális szám {0} hexadeximális értéke: {0:x}".format(szam))


# 8.16.7 Sztringek formázása 7.0.

nev = 'Zoli'
kor = 42

bemutatkozas = """
A nevem {0} és {1} éves vagyok.
"""

print(bemutatkozas.format(nev, kor))


# 8.16.8 Sztringek formázása 8.0

level = """
Kedves {0} {2}!

{0}, van egy rendkívüli üzleti ajánlatom az Ön számára.
Amennyiben küld 10 millió dollárt a bankszámlámra, megduplázom a pénzét...
"""

print(level.format("Paris", "Whitney", "Hilton"))
print(level.format("Bill", "Henry", "Gates"))


# 8.16.9 Sztringek formázása 9.0.

# Először a formázatlan változat:

print("i\ti**2\ti**3\ti**5\ti**10\ti**20")
for i in range(1, 11):
    print(i, "\t", i**2, "\t", i**3, "\t", i**5, "\t",
                                            i**10, "\t", i**20, sep='')



# A fenti táblázat megformázva:

elrendezes = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"

print(elrendezes.format("i", "i**2", "i**3", "i**5", "i**10", "i**20"))
for i in range(1, 11):
    print(elrendezes.format(i, i ** 2, i ** 3, i ** 5, i ** 10, i ** 20))


# 8.19.2.

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]

for utotag in utotagok_listaja:
    if utotag[0] != 'p':
        print(elotag + utotag)
    else:
        print(elotag + utotag[1:])



    # 8.19.3. Egy k karaktert keressünk, hogy hányszor szerepel egy gyümölcsben

    gyumolcs = "banán"
    k = 'n'

    def karakter_szamlalas(gyumolcs, k):
        darab = 0
        for karakter in gyumolcs:
            if karakter == k:
                darab += 1
        return darab

    print(karakter_szamlalas(gyumolcs, k))


# 8.19.4. Find, egy k karaktert keressünk, hogy hányszor szerepel egy gyümölcsben

gyumolcs = "banán"
k = 'n'


def karakter_szamlalas(gyumolcs, k):
    """
    Megszámolja a find fügyvénnyel, hogy egy k karakter hányszor szerepel
    egy karaktersorozatban.
    """

    i = 0
    for _ in range(len(gyumolcs)):
        f = gyumolcs.find(k, i)
        i = f
    return i

print(karakter_szamlalas(gyumolcs, k))

# 8.19.5.

import string


book_of_blood = """
...And so, lockeed beyond the Gateway of Blood and past the Hall of Fire,
 Valor awaits for the Hero of Light to awaken...
 """

def irasjelek_eltavolitasa(book_of_blood):
    """
    Az írásjelek kiszedése a book_of_blood szövegből és a bob_0-ba való mentése.
    """
    bob_0 = ""
    for k in book_of_blood:
        if k not in string.punctuation:
            bob_0 += k
    return bob_0


def karakter_szamlalas(ss, kk):
    "Megszámolja, hogy a kk karakter hányszor fordul elő a szövegben"
    d = 0
    for i in ss:
        if kk in i:
            d +=1
    return d

ss = irasjelek_eltavolitasa(book_of_blood).split()
kk = 'e'
h = len(ss)
d = karakter_szamlalas(ss, kk)
sz = (d / h) * 100

print("A szövegben {0} szó áll, melyből {1}({2:.2f}%) tartalmaz '{3}' betűt."
        .format(h, karakter_szamlalas(ss, kk), sz, kk))


# 8.19.6. Szorzótábla

n = 13

def tabla():
    """
    Kiírja a sorokat: a számozást, a kettős pontot minden sorban és a szorzat
    értékeit.
    """
    for i in range(1, n):
        print(f"{i:>2}", end='')
        print(':  ', end ='')

        for j in range(1,n):
            print(f"{i * j:>4}", end='')
        print('\n')


def vizszintes():
    """
    A fejlécet írja ki a számokkal, a kezdő kettőspontot,
    illetve a szaggatott vonalat.
    """
    print('\n')
    print(5 * ' ', end=''.format(''))
    for i in range(1, n):
        print(f"{i:>4}", end='')
    print('\n', ' :', end='')
    for i in range((4 * n) - 2):
        print('-', end ='')
    print('\n')
    tabla()


vizszintes()


# 8.19.7. Egy sztring visszafele olvasva.

import sys

s = "rád rohan a hordár"


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def sztring_forditas(s):
    """
    Visszafele járok be egy s sztringet és azt egy új f változóba teszem.
    """
    f = s[::-1]
    return f


def tesztkeszlet_sztring_forditas():
    """ A 8.19.7  modulhoz tartozó tesztkészlet futtatása.  """
    teszt(sztring_forditas("boldog") == "godlob")
    teszt(sztring_forditas("Python") == "nohtyP")
    teszt(sztring_forditas("") == "")
    teszt(sztring_forditas("a") == "a")

# print(sztring_forditas(s))
tesztkeszlet_sztring_forditas()



# 8.19.8. Egy sztring és annak tükörképe összefűzve

import sys

s = "mozi"


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def sztring_tukor(s):
    """
    Egy sztring és annak tükörképe összefűzve.
    """
    t = ""
    f = s[::-1]
    t = s + f
    return t


def tesztkeszlet_sztring_tukor():
    """ A 8.19.8  modulhoz tartozó tesztkészlet futtatása.  """
    teszt(sztring_tukor("jo") == "jooj")
    teszt(sztring_tukor("Python") == "PythonnohtyP")
    teszt(sztring_tukor("") == "")
    teszt(sztring_tukor("a") == "aa")

# print(sztring_tukor(s))
tesztkeszlet_sztring_tukor()


# 8.19.9. Karakter eltávolítása sztringből

import sys

s = "Quantum Fireball"
k = "a"

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def betu_eltuntetes(k, s):
    """
    Egy k karaktert kiszed egy s sztringből.
    """
    uj_s = ''
    for i in s:
        if i != k:
            uj_s = uj_s + i
    return uj_s


def tesztkeszlet_betu_eltuntetes():
    """ A 8.19.9  modulhoz tartozó tesztkészlet futtatása.  """
    teszt(betu_eltuntetes("a", "alma") == "lm")
    teszt(betu_eltuntetes("a", "banán") == "bnán")
    teszt(betu_eltuntetes("z", "banán") == "banán")
    teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
    teszt(betu_eltuntetes("b", "") == "")
    teszt(betu_eltuntetes("b", "c") == "c")

print(betu_eltuntetes(k, s))
# tesztkeszlet_betu_eltuntetes()


# 8.19.10. Megnézi, hogy egy sztring palindrom-e.

import sys

s = "erődösödőre"

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def palindrom_e(s):
    """ Megnézi, hogy egy sztring palindrom-e. """
    f = s[::-1]
    if f == s:
        return True
    return False


def tesztkeszlet_palindrom_e():
    """ A 8.19.10  modulhoz tartozó tesztkészlet futtatása.  """
    teszt(palindrom_e("abba"))
    teszt(not palindrom_e("abab"))
    teszt(palindrom_e("teret"))
    teszt(not palindrom_e("banán"))
    teszt(palindrom_e("mesék késem"))
    teszt(palindrom_e("a"))
    # teszt(palindrom_e(""))    # Egy üres sztring palindrom-e?

# print(palindrom_e(s))
tesztkeszlet_palindrom_e()


# 8.19.12. Eltávolítja egy sztringből egy másik sztring első előfordulását.

import sys

s = "almafa"
k = "alma"

def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def torles(k, s):
    """
    Eltávolítja egy s sztringből egy másik k sztring első előfordulását.
    """
    new = ""
    if k in s:
        d = s.find(k)
        for j in range(d):
            new = new + s[j]
        for j in range(d + len(k), len(s)):
            new = new + s[j]
        return new
    return s


def tesztkeszlet_torles():
    """ A 8.19.12  modulhoz tartozó tesztkészlet futtatása.  """
    teszt(torles("alma", "almafa") == "fa")
    teszt(torles("an", "banán") == "bán")
    teszt(torles("pa", "papaja") == "paja")
    teszt(torles("pa", "Papaja") == "Paja")
    teszt(torles("alma", "kerékpár") == "kerékpár")

# print(torles(k, s))
tesztkeszlet_torles()
