#6.1.1 Saját abs függvény

def abszolut_ertek(x):
    if x < 0:
        return -x
    return x

print(abszolut_ertek(-1))




#6.1.2. Két betűs szavak keresése egy listában

def ketbetus_szo_keresese(szolista):
    for szo in szolista:
        if len(szo) == 2:
            return szo
    return ""   #Ha nincs visszatérési érték, akkor üres stringet ad vissza.


print( ketbetus_szo_keresese(["ez",  "egy", "halott", "papagáj"]))
print( ketbetus_szo_keresese(["szeretem",  "a",  "sajtot"]))



#6.1.3. Két pont távolsága

import math
def ket_pont_tavolsaga(x1, y1, x2, y2):
    tavolsag = math.sqrt(pow(x2 -x1, 2) + pow(y2-y1, 2))
    return tavolsag

print(ket_pont_tavolsaga(0, 0, 3, 4))



#6.4.1. Kör területe

import math
def kozeppont_korpont_tavolsag(kx, ky, x, y):
    """Két pont távolsága a koordinátáik alapján"""
    sugar = math.sqrt(pow(x -kx, 2) + pow(y-ky, 2))
    return sugar
# print(kozeppont_korpont_tavolsag(0, 0, 0, 1))

def terulet(sugar):
    '''Kör területe explicit sugár alapján'''
    return pow(sugar, 2) * math.pi

# print(terulet(1))
#
def kor_terulete(kx, ky, x, y):
    '''Kör területe a fenti 2 részfüggvény meghívásával'''
    sugar = kozeppont_korpont_tavolsag(kx, ky, x, y)
    eredmeny = terulet(sugar)
    return(eredmeny)

print(kor_terulete(1, 1, 1, 2))

#6.5.1 Két szám esetén az első osztható-e a másodikkal

def oszthato_e(x, y):
    """ Annak vizsgálata, hogy x osztható-e y-nal. """
    return (x % y == 0)

print("Az első szám osztható a másodikkal?",oszthato_e(1, 3))
print(oszthato_e(6, 3))

#6.7. Egységteszt

import sys

def abszolut_ertek(x):
    """  Saját abszolútérték függvény.  """
    if x < 0:
        return -x
    return x


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(abszolut_ertek(17) == 17)
    teszt(abszolut_ertek(-17) == 17)
    teszt(abszolut_ertek(0) == 0)
    teszt(abszolut_ertek(3.14) == 3.14)
    teszt(abszolut_ertek(-3.14) == 3.14)

tesztkeszlet()


#6.9. Az összes feladat egy scriptben

import sys

egtajak = ['É', 'K', 'D', 'NY', 'É']

def fordulj_orajarasi_iranyba(egtaj):
    """  6.9.1. Égtájak szomszédja az óramutató járása szerint  """
    if egtaj in egtajak:
        i = egtajak.index(egtaj)
        e = egtajak[i+1]
        return e
    return

# print(fordulj_orajarasi_iranyba('É'))


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def tesztkeszlet_fordulj_orajarasi_iranyba():
    """ 6.9.1. A fordulj_orajarasi_iranyba modulhoz tartozó tesztkészlet. """
    teszt(fordulj_orajarasi_iranyba("É") == "K")
    teszt(fordulj_orajarasi_iranyba("NY") == "É")
    teszt(fordulj_orajarasi_iranyba(42) == None)
    teszt(fordulj_orajarasi_iranyba("ostobaság") == None)

#6.9. Az összes feladat egy scriptben

import sys

egtajak = ['É', 'K', 'D', 'NY', 'É']
napok = ['hétfő','kedd','szerda','csütörtök','péntek','szombat','vasárnap']
honapok28 = ['február']
honapok30 = ['április', 'június', 'szeptember', 'november']
honapok31 = ['január','március','május','július','augusztus','október','december']


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno   # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


def fordulj_orajarasi_iranyba(egtaj):
    """  6.9.1. Égtájak szomszédja az óramutató járása szerint  """
    if egtaj in egtajak:
        i = egtajak.index(egtaj)
        e = egtajak[i+1]
        return e
    return


def tesztkeszlet_fordulj_orajarasi_iranyba():
    """ 6.9.1. A fordulj_orajarasi_iranyba modulhoz tartozó tesztkészlet. """
    teszt(fordulj_orajarasi_iranyba("É") == "K")
    teszt(fordulj_orajarasi_iranyba("NY") == "É")
    teszt(fordulj_orajarasi_iranyba(42) == None)
    teszt(fordulj_orajarasi_iranyba("ostobaság") == None)


def nap_nev(nap_szam):
    """ 6.9.2. A hét napjának neve a sorszáma alapján. """
    if nap_szam in range(7):
        return napok[nap_szam]
    return


def tesztkeszlet_nap_nev():
    """ 6.9.2. A nap_nev modulhoz tartozó tesztkészlet. """
    teszt(nap_nev(3) == "csütörtök")
    teszt(nap_nev(6) == "vasárnap")
    teszt(nap_nev(42) == None)

def nap_sorszam(nap):
    """ 6.9.3 A hét napjának sorszáma a neve alapján"""
    if nap in napok:
        return napok.index(nap)
    return


def tesztkeszlet_nap_sorszam():
    """ 6.9.3. A nap_sorszam modulhoz tartozó tesztkészlet. """
    teszt(nap_sorszam("péntek") == 4)
    teszt(nap_sorszam("hétfő") == 0)
    teszt(nap_sorszam(nap_nev(3)) == 3)
    teszt(nap_nev(nap_sorszam("csütörtök")) == "csütörtök")
    teszt(nap_sorszam("Halloween") == None)


def napok_hozzaadasa(nap, hany_nap_mulva):
    """  6.9.4 A hét melyik napján megyek nyaralni ha x nap múlva indulok.  """
    nyaral_sorszam = (nap_sorszam(nap) + hany_nap_mulva) % 7
    nyaral_nap = nap_nev(nyaral_sorszam)
    return nyaral_nap


def tesztkeszlet_napok_hozzaadasa():
    """ 6.9.4. A napok_hozzaadasa modulhoz tartozó tesztkészlet. """
    teszt(napok_hozzaadasa("hétfő", 4) ==  "péntek")
    teszt(napok_hozzaadasa("kedd", 0) == "kedd")
    teszt(napok_hozzaadasa("kedd", 14) == "kedd")
    teszt(napok_hozzaadasa("vasárnap", 100) == "kedd")
    teszt(napok_hozzaadasa("vasárnap", -1) == "szombat")
    teszt(napok_hozzaadasa("vasárnap", -7) == "vasárnap")
    teszt(napok_hozzaadasa("kedd", -100) == "vasárnap")


def honap_napja(honap):
    """6.9.6. A hónap neve alapján megadja, hogy hány nap van abban a hónapban."""
    if honap in honapok28:
        return 28
    elif honap in honapok30:
        return 30
    elif honap in honapok31:
        return 31
    return


def tesztkeszlet_honap_napja():
    """ 6.9.6. A honap_napja modulhoz tartozó tesztkészlet. """
    teszt(honap_napja("február") == 28)
    teszt(honap_napja("november") == 30)
    teszt(honap_napja("december") == 31)

def masodpercre_valtas(ora, perc, masodperc):
    """  6.9.8. Órák, percek, másodpercek átváltása másodpercekké.  """
    ora_masodperc = ora * 3600
    perc_masodperc = perc * 60
    return int(ora_masodperc + perc_masodperc + masodperc)

def tesztkeszlet_masodpercre_valtas():
    """ 6.9.8. A masodpercre_valtas modulhoz tartozó tesztkészlet. """
    teszt(masodpercre_valtas(2, 30, 10) == 9010)
    teszt(masodpercre_valtas(2, 0, 0) == 7200)
    teszt(masodpercre_valtas(0, 2, 0) == 120)
    teszt(masodpercre_valtas(0, 0, 42) == 42)
    teszt(masodpercre_valtas(0, -10, 10) == -590)
    teszt(masodpercre_valtas(2.5, 0, 10.71) == 9010)
    teszt(masodpercre_valtas(2.433,0,0) == 8758)


def orakra_valtas(masodperc):
    """  6.9.9.1 Másodpercek átváltása egész órákká.  """
    masodperc_ora = int(masodperc / 3600)
    return masodperc_ora


def tesztkeszlet_orakra_valtas():
    """ 6.9.9.1 Az orakra_valtas modulhoz tartozó tesztkészlet. """
    teszt(orakra_valtas(9010) == 2)
    teszt(orakra_valtas(7200) == 2)
    teszt(orakra_valtas(3599) == 0)

def percekre_valtas(masodperc):
    """  6.9.9.2 Percekre váltása az órákon felüli másodperceknek.  """
    masodperc_perc = int((masodperc % 3600) / 60)
    return masodperc_perc


def tesztkeszlet_percekre_valtas():
    """ 6.9.9.2 A percekre_valtas modulhoz tartozó tesztkészlet. """
    teszt(percekre_valtas(9010) == 30)
    teszt(percekre_valtas(3599) == 59)
    teszt(percekre_valtas(3601) == 0)
    teszt(percekre_valtas(3661) == 1)


def masodpercekre_valtas(masodpercek):
    """  6.9.9.3 Csak a másodpercek megadása az órák és percek felett.  """
    masodperc_ora = masodpercek % 3600
    masodperc_perc = masodperc_ora % 60
    return int(masodperc_perc)


def tesztkeszlet_masodpercekre_valtas():
    """ 6.9.9.3 A masodpercekre_valtas modulhoz tartozó tesztkészlet. """
    teszt(masodpercekre_valtas(9010) == 10)
    teszt(masodpercekre_valtas(3599) == 59)
    teszt(masodpercekre_valtas(7200) == 0)
    teszt(masodpercekre_valtas(3601) == 1)

def osszehasonlitas(a, b):
    """  6.9.11. Összehasonlít két számot, így add vissza kimeneteket.  """

    if a > b:
        return 1
    if a == b:
        return 0
    return -1


def tesztkeszlet_osszehasonlitas():
    """ 6.9.11. Az osszehasonlitas modulhoz tartozó tesztkészlet. """
    teszt(osszehasonlitas(5, 4) == 1)
    teszt(osszehasonlitas(7, 7) == 0)
    teszt(osszehasonlitas(2, 3) == -1)
    teszt(osszehasonlitas(42, 1) == 1)


def atfogo(a, b):
    """6.9.12. Derékszögű háromszög átfogójának kiszámítása a befogók alapján."""
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def tesztkeszlet_atfogo():
    """ 6.9.12. Az atfogo modulhoz tartozó tesztkészlet. """
    teszt(atfogo(3, 4) == 5.0)
    teszt(atfogo(12, 5) == 13.0)
    teszt(atfogo(24, 7) == 25.0)
    teszt(atfogo(9, 12) == 15.0)


def meredekseg(x1, y1, x2, y2):
    """ 6.9.13.1 Az (x1, y1), (x2, y2) pontokon átmenő egyenes meredeksége. """
    v1 = x2 - x1
    v2 = y2 - y1
    if v1 != 0:
        m = v2 / v1
        return m
    return


def tesztkeszlet_meredekseg():
    """ 6.9.13.1 A meredekseg modulhoz tartozó tesztkészlet. """
    teszt(meredekseg(5, 3, 4, 2) == 1.0)
    teszt(meredekseg(1, 2, 3, 2) == 0.0)
    teszt(meredekseg(1, 2, 3, 3) == 0.5)
    teszt(meredekseg(2, 4, 1, 2) == 2.0)
    teszt(meredekseg(2, 4, 2, 5) == None)


def metszespont(x1, y1, x2, y2):
    """ 6.9.13.2 Egy egyenes y tengellyel való metszésének pontja.  """
    metszespont = y1 - (meredekseg(x1, y1, x2, y2) * x1)
    return metszespont


def tesztkeszlet_metszespont():
    """ 6.9.13.2 A metszespont modulhoz tartozó tesztkészlet. """
    teszt(metszespont(1, 6, 3, 12) == 3.0)
    teszt(metszespont(6, 1, 1, 6) == 7.0)
    teszt(metszespont(4, 6, 12, 8) == 5.0)


def paros_e(n):
    """   6.9.14. Egészek páros/páratlan vizsgálata.   """
    return(n % 2 == 0)


def tesztkeszlet_paros_e():
    """ 6.9.14. A paros_e modulhoz tartozó tesztkészlet. """
    teszt(paros_e(0) == True)
    teszt(paros_e(1) == False)
    teszt(paros_e(8) == True)
    teszt(paros_e(-6) == True)
    teszt(paros_e(-11) == False)


def paratlan_e(n):
    """   6.9.15.1 Egészek páros/páratlan vizsgálata.   """
    return(n % 2 != 0)


def tesztkeszlet_paratlan_e():
    """ 6.9.15.1 A paratlan_e modulhoz tartozó tesztkészlet. """
    teszt(paratlan_e(0) == False)
    teszt(paratlan_e(1) == True)
    teszt(paratlan_e(8) == False)
    teszt(paratlan_e(-6) == False)
    teszt(paratlan_e(-11) == True)


def paratlan_e_2(n):
    """   6.9.15.2 Egészek páros/páratlan vizsgálata.   """
    return not paros_e(n)


def tesztkeszlet_paratlan_e_2():
    """ 6.9.15.2 A paratlan_e_2 modulhoz tartozó tesztkészlet. """
    teszt(paratlan_e_2(0) == False)
    teszt(paratlan_e_2(1) == True)
    teszt(paratlan_e_2(8) == False)
    teszt(paratlan_e_2(-6) == False)
    teszt(paratlan_e_2(-11) == True)


def tenyezo_e(t, n):
    """   6.9.16. Osztható-e n t-vel egész számszor.  """
    if t != 0:
        return (n % t == 0)
    return "A nullával való osztás értelmetlen"


def tesztkeszlet_tenyezo_e():
    """   6.9.16. A tenyezo_e modulhoz tartozó tesztkészlet.  """
    teszt(tenyezo_e(3, 12))
    teszt(not tenyezo_e(5, 12))
    teszt(tenyezo_e(7, 14))
    teszt(not tenyezo_e(7, 15))
    teszt(tenyezo_e(1, 15))
    teszt(tenyezo_e(15, 15))
    teszt(not tenyezo_e(25, 15))
    teszt(tenyezo_e(0, 8))


def tobbszorose_e(n, t):
    """   6.9.17. n a t-nek egész számú többszöröse-e.  """
    return tenyezo_e(t, n)


def tesztkeszlet_tobbszorose_e():
    """   6.9.17. A tobbszorose_e modulhoz tartozó tesztkészlet.  """
    teszt(tobbszorose_e(12, 3))
    teszt(tobbszorose_e(12, 4))
    teszt(not tobbszorose_e(12, 5))
    teszt(tobbszorose_e(12, 6))
    teszt(not tobbszorose_e(12, 7))
    teszt(tobbszorose_e(12, 0))
    teszt(tobbszorose_e(0, 12))


def celsiusra_valtas(f):
    """   6.9.18. Celsiusra váltja a Fahrenheitben megadott értéket.   """
    C = round((f -32) * 5/9)
    return C


def tesztkeszlet_celsiusra_valtas():
    """   6.9.18. A celsiusra_valtas modulhoz tartozó tesztkészlet.  """
    teszt(celsiusra_valtas(212) == 100)     # A víz forráspontja
    teszt(celsiusra_valtas(32) == 0)        # A víz fagyáspontja
    teszt(celsiusra_valtas(-40) == -40)     # Ó, micsoda érdekes eset!
    teszt(celsiusra_valtas(36) == 2)
    teszt(celsiusra_valtas(37) == 3)
    teszt(celsiusra_valtas(38) == 3)
    teszt(celsiusra_valtas(39) == 4)


def fahrenheitre_valtas(C):
    """   6.9.19. Fahrenheitre váltja a Celsiusban megadott értéket.   """
    f = round((9/5) * C + 32)
    return f


def tesztkeszlet_fahrenheitre_valtas():
    """   6.9.19. A fahrenheitre_valtas modulhoz tartozó tesztkészlet.  """
    teszt(fahrenheitre_valtas(0) == 32)
    teszt(fahrenheitre_valtas(100) == 212)
    teszt(fahrenheitre_valtas(-40) == -40)
    teszt(fahrenheitre_valtas(12) == 54)
    teszt(fahrenheitre_valtas(18) == 64)
    teszt(fahrenheitre_valtas(-48) == -54)


# print(fordulj_orajarasi_iranyba('É'))
tesztkeszlet_fordulj_orajarasi_iranyba()

# print(nap_nev(6))
tesztkeszlet_nap_nev()

# print(nap_sorszam('hétfő'))
tesztkeszlet_nap_sorszam()

# print(napok_hozzaadasa('szerda', 14))
tesztkeszlet_napok_hozzaadasa()

# print(honap_napja('november'))
tesztkeszlet_honap_napja()

# print(masodpercre_valtas(2, 30, 10))
tesztkeszlet_masodpercre_valtas()

# print(orakra_valtas(10799))
tesztkeszlet_orakra_valtas()

# print(percekre_valtas(3661))
tesztkeszlet_percekre_valtas()

# print(masodpercekre_valtas(3599))
tesztkeszlet_masodpercekre_valtas()

# print(osszehasonlitas(1, 2))
tesztkeszlet_osszehasonlitas()

# print(atfogo(3, 4))
tesztkeszlet_atfogo()

# print(meredekseg(5, 3, 4, 2))
tesztkeszlet_meredekseg()

# print(metszespont(1, 6, 3, 12))
tesztkeszlet_metszespont()

# print(paros_e(-3))
tesztkeszlet_paros_e()

# print(paratlan_e(-3))
tesztkeszlet_paratlan_e()

# print(paratlan_e_2(-3))
tesztkeszlet_paratlan_e_2()

# print(tenyezo_e(0, 0))
tesztkeszlet_tenyezo_e()

# print(tobbszorose_e(12, 0))
tesztkeszlet_tobbszorose_e()

# print(celsiusra_valtas(-40))
tesztkeszlet_celsiusra_valtas()

# print(fahrenheitre_valtas(-40))
tesztkeszlet_fahrenheitre_valtas()
