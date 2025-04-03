from sys import exit
import random

print("Ez egy játék amely a heroes of might and magic 3 játékhoz \
kapcsolódik. A játék során kérdésekre kell válaszolnod, a válaszokat kis \
betűvel írd.")

print("\nAz út végén egy koponyára emlékeztető bejárat áll, amely a mélybe \
vezet. Az Angelic Alliance kardját ezen belül találod. Hat próbát kell kiállnod, \
ha megszerezted a kard mind a hat részét, össze tudod rakni.\n")

print("A bejárat mögött két ajtót találsz, egyet balra, egyet jobbra. \
A balra lévő előtt egy gremlin áll, elég morcosan néz rád, a jobbra lévőt nem \
őrzi senki. Melyiket választod?")

def azúr4():
    print("Bizony, smaragdok. Elcserélném veled az erszényt és a drágaköveket. \
Tudom, hogy a szövetség kardját keresed, nálam van a szárnyas sisak.")
    print("Egy másodpercig sem tétovázol, kiveszed az erszényt a zsákodból és \
átadom a sárkánynak. Ő átnyújta neked a sisakot. Végre, megszerezted az \
utolsó darabot is, nagy megelégedettséggel teszed a fejedre. Alap képességeid \
immár hattal nőttek, nem beszélve arról, hogy bármilyen egységet toborozhatsz \
harci kedv vesztése nélkül. De az igazi ajándék a prayer varázslat, amit \
minden harci egységed megkap a csata elején. Nincs más hátra, elköszönsz a \
sárkánytól és kimész a barlangból.")
    dead()


def azúr2():
    print("Igen, ha nálad van akkor mondd meg, hogy milyen drágakövek vannak \
benne")
    válasz = input("> ")
    if 'smaragd' in válasz:
        azúr4()
    else:
        print("Blöffölni akartál, nem jött be. Erre a sárkány közelebb lép \
hozzád és egyszerűen leharapja a fejed.")
        dead()


def azúr_sárkány():
    print("Az azúr sárkány barlangjához érsz, a sárkány érdeklődve figyel \
téged. Elmondod neki, hogy a szövetség kardját keresed.")
    print("Nálam van a sisak - mondja, és megszerezheted, de előbb a fekete \
sárkánytól hozd el a koboldok szent erszényét. Nálad van?")
    azúr3()

def azúr3():
    válasz = input("> ")
    if válasz == 'igen':
        azúr2()
    elif válasz == 'nem' or válasz == 'nincs':
        print("Keresd fel akkor a fekete sárkány és az erszély nélkül vissza \
ne gyere - dörgi. Hátrafordulsz és elindulsz vissza az útkereszteződésig.")
        elag41()
    else:
        print("Nem értem, próbáld újra1.")
        azúr3()


def sárkány_vacsora():
    print("\nEz a próbád nem sikerült - mondja vigyorogva a sárkány. Kitátja a \
száját és tűzet fúj rád. Ropogósra sülsz.")
    dead()


def fs01():
    válaszlista0 = []
    válaszlista1 = ['kő', 'fa', 'kristály', 'kén', 'higany', 'gyémánt']
    válasz = input("> ")
    if válasz in válaszlista1:
        válaszlista0.append(válasz)
        print(f"Eddig ez 1, és még?")
    else:
        sárkány_vacsora()
    for i in range(2,6):
        válasz = input("> ")
        if válasz in válaszlista0:
            print("\nEz már volt, nem figyelsz.")
            sárkány_vacsora()
        elif válasz in válaszlista1:
            válaszlista0.append(válasz)
            print(f"Eddig ez {i}, és még?")

    print("Eddig jó, és az utolsó?")
    válasz = input("> ")
    if válasz in válaszlista1:
        print("\nSzuper, felsoroltad mind.")
        print("\nKiálltad a próbát, tiéd a kard - mondja a sárkány. Adok hozzá \
ajándékba egy erszélyt is, van benne egy marék smaragd. Tudod engem csak az \
arany érdekel.")
        print("Kezedbe veszed a kardot és irdatlan erő jár át, öttel nőttek \
az alapképességeid. Már csak a sisak hiányzik a szövetség kardjához. Az biztos \
az azúr sárkánynál lesz - morfondírozol. Megköszönöd az erszélyt, \
visszamész az elágazáshoz és jobbra tartasz az úton.")
        azúr_sárkány()
    else:
        sárkány_vacsora()


def fekete_sárkány():
    print("\nA fekete sárkány barlangjához értél. A sárkány ott fekszik egy \
halom arany alatt. Megszólítod, és elmondod neki, hogy a szövetség kardját \
keresed.")
    print("\nVan itt valami kard a sarokban - feleli. Attól a hőstől vettem el, \
aki a múltkor el akarta lopni az aranyamból. Neked adhatom, ha gondolod.")
    print("A sárkány előcipel egy ezüstösen csillogó kardot.")
    print("\nAzonnal kiszúrod, hogy ez a Sword of Judgement. Mit kérsz érte - \
kérdezed.")
    print("Nekem ez a kard értéktelen, de ha akarod akkor megkaphatod, ha egy \
kérdésemre válaszolsz. De ha rosszul válaszolsz, megeszlek vacsorára.")
    print("Rendben, mi a kérdésed?")
    print("Milyen nyersanyagokat lehet a játékban bányászni? Sorold fel mind \
a hatot egyesével.")
    fs01()


def elag4():
    print("\nJól válaszoltál - mondja a tündér. Átadja a varázstárgyat és \
kinyitja az ajtót. Sok szerencsét! - kiáltja utánad. Kezedbe veszed a pajzsot.\
Erősebb vagy mint valaha, alapképességeid néggyel nőttek. Hosszú gyaloglás \
egy újabb útkereszteződéshez érsz.")
    elag41()

def elag41():
    print("Az útjelző tábla szerint erre sárkányok tanyáznak. Balra van a \
fekete sárkány barlangja, jobbra az azúr sárkányé. Merre mész tovább?")
    elag42()

def elag42():
    válasz = input("> ")
    válasz_fekete = ['bal', 'balra', 'fekete']
    válasz_azúr = ['jobb', 'jobbra', 'azúr', 'azure']
    if válasz in válasz_fekete:
        fekete_sárkány()
    elif válasz in válasz_azúr:
        azúr_sárkány()
    else:
        print("Nem értem, próbáld újra.")
        elag42()

def tündér():
    print("\n\nTöbb órás fárasztó gyaloglás után a tündér kuckójához érsz. \
Közelebb lépsz hozzá mosolyogva, elmondod neki, hogy a szövetség kardját \
keresed és át szeretnél menni az ajtón amit ő őriz. Megpillantasz egy arany \
színű pajzsot ágaskodó vörös oroszlánnal díszítve a tündér mellé letámasztva.")
    print("\nMennyiért adod a pajzsot? - kérdezed.")
    print("\nA pajzs nem eladó, de megkaphatod, ehhez válaszolnod kell egy \
kérdésemre. Ha helyesen válaszolsz, tovább mehetsz, ha nem, büntetés a \
jutalmad.")
    print("\nRendben, mondod, hallgatom a kérdésed.\n")
    print("A kérdés: Mi volt a neve annak a számítógépes játéknak, amellyel \
a Heroes of Might and Magic sorozat elindult?")
    válasz = input("> ")

    if válasz == "king's bounty":
        elag4()
        elag41()
    else:
        print("\nErre az egyszerű kérdésre sem tudod a választ? - ordít a \
tündér. Rádfúj valami varázsport és békává változol, de ez már egy másik mese.")
        dead()


def minotaurusz3():
    print("Igen? - kiált fel. Akkor biztosan láttál egy köpenyt nála. Igen, \
feleled. No és milyen szinű volt? - kérdezi.")
    válasz = input("> ")
    if válasz == "barna":

        print(f"""\nA minotaurusz elégedetten hümmög. Igen, {válasz}. Tudod, \
régebben az az enyém volt, csak az a galád medúza ellopta tőlem.\n""")
        print("Itt van nálam - mondod. Beletúrsz a zsákodba és megmutatod neki.\
 Kikerekedett szemekkel néz rád. Mit kérsz cserébe érte? - kérdezi. Tetszik a \
nyakláncod - feleled, cserélhetnénk.")
        print("Ez egy nagyon értékes nyaklánc, ez a Celestial Necklace \
of Bliss. Csak úgy nem cserélhetem el veled, de ha válaszolsz egy kérdésemre \
akkor tied lehet a nyaklánc és te nekem adod a köpenyt. \
\n\nRendben, mi a kérdésed?")
        print("\nEgyszerre maximum hány hőse lehet a játékban egy játékosnak \
a váron kívül? 6, 8, 12 vagy 15?")
        minotaurusz4()
    else:
        print("\nHazudtál nekem, kétszer is - ordítja. Felkapja a kétfejű \
bárdját és lecsapja a fejed.")
        dead()


def minotaurusz4():

        válasz = input("> ")
        lista = ['6', '8', '12', '15']
        if válasz in lista:

            if válasz == '8':
                print("\n8, ez a helyes válasz. Leveszi a nyakláncot és átadja, \
te pedig átnyújtom neki a köpenyt. Ezzel a cserével mindketten elégedettek \
vagytok.")
                print("\nFelteszed a nyakláncot és megint erősebb lettél: \
alapképességeid most hárommal nőttek. Jókedvűen indulsz tovább az úton.")
                tündér()

            else:
#Meghatározom, hogy a válasz a listának melyik indexű eleme és kiveszem azt az
#elemet a listából
                index = lista.index(válasz)
                válasz = lista.pop(index)
                #print(lista)
                print(f"""\nNem, a helyes válasz nem {válasz}, de kapsz még \
egy esélyt.Tehát egyszerre maximum hány hőse lehet játékban egy játékosnak \
a váron kívül? {lista[0]}, {lista[1]} vagy {lista[2]}?""")
                minotaurusz5()

        else:
            print("\nNem figyeltél eléggé, próbáld meg újra.")
            minotaurusz4()


def minotaurusz5():
    válasz = input("> ")
    if válasz == '8':
        print("\n8, ez a helyes válasz. Leveszi a nyakláncot és átadja, \
te pedig átnyújtom neki a köpenyt. Ezzel a cserével mindketten elégedettek \
vagytok.")
        print("\nFelteszed a nyakláncot és megint erősebb lettél: \
alapképességeid most hárommal nőttek. Jókedvűen indulsz tovább az úton.")
        tündér()
    else:
        print("\nMásodjára sem találtad el. Felkapja a kétfejű \
bárdját és lecsapja a fejed.")
        dead()


def medúza():
    print("\nA medúza kápolnájánál találod magad. Belépsz és meglátod őt. \
Elmondod neki, hogy a szövetség kardját keresed. Azt nem tudom, hogy hány \
varázstárgyad van már eddig hozzá - szólal meg, de nálam van a Sandals of the \
Saint, itt van rajtam. Kicsit furcsálod a dolgot, hiszen a medúzáknak \
nincsenek lábaik, de aztán legyintesz.\n")
    print("\nMegkaphatod, de ehhez ki kell állnod egy próbát. Ha elbuksz, \
meghalsz. Nyelsz egy nagyot, de belemész a játékba.")
    print("\nÍgy szól a medúza: Egy kérdésem van, erre felelj: Melyik a \
leggyorsabb lény az egész heroes 3 játékban?")
    válasz = input("> ")
    if válasz == "phoenix" or válasz == "főnix":
        print("\nJó a válaszod. Tessék, itt a szent szandálja és adok mellé egy \
barna színű köpenyt is, még jól jöhet. Elégedetten gyűröd be a palástot a \
zsákodba. Felveszed a szandált és újra erősebbnek érzed magad: az alap \
képességeid kettővel nőttek. Visszamész az útkereszteződésig és a minotaurusz \
felé vezed az irányt.\n")
        minotaurusz()
    else:
        print("\nPedig nem kérdeztem nehezet. Rálehel az arcodra, ezzel kővé \
változol.")
        dead()


def minotaurusz():
    print("\nPár percen belül eléred a minotaurusz barlangját, előtte a \
a minotaurusz strázsál. Még mielőtt bármit is szólhatnál így szól hozzád: \
Ha kiálltad a medúza próbáját akkor én is átengedlek. Voltál már a medúzánál?")
    minotaurusz2()


def minotaurusz2():

    válasz = input("> ")
    if 'gen' in válasz:
        minotaurusz3()
    if 'em' in válasz:
        print("\nMenj vissza a kereszteződésig ahonnan jöttél. Hátrafordulsz és \
elindulsz az úton vissza.")
        elag21()
    else:
        print("\nNem értem, próbáld újra.")
        minotaurusz2()


def elag21():
    print("\nAz útjelző tábla szerint balra \
van a medúza kápolnája, jobbra a minotaurusz barlangja. Merre mész tovább?")
    elag22()


def elag22():

    választ = input("> ")
    bal = ['bal', 'balra']
    jobb = ['jobb', 'jobbra']

    if 'bal' in választ:
        medúza()
    elif 'jobb' in választ:
        minotaurusz()
        minotaurusz2()
    else:
        print("Nem értem, próbáld újra.")
        elag22()


def kocka_dobás():
    válasz = input('')
    kocka1 = random.randint(1,6)
    kocka1 = random.randint(1,6)
    kocka1 = kocka11 + kocka12
    print(f"{kocka1} és {kocka1}-t dobtál, ez összesen {kocka1}")

def gremlin2():
    print("Helyes. Dobj a két kockával, üss entert.")
    válasz = input('')
    kocka1 = random.randint(1,6)
    kocka2 = random.randint(1,6)
    kocka = kocka1 + kocka2
    print(f"{kocka1}-t és {kocka2}-t dobtál, ez összesen {kocka}")
    if kocka == 7:
        print("Micsoda piszok szerencse - kiáltja a gremlin, már elsőre \
sikerült. De amit ígértem, azt megtartom. Átadja a varázstárgyat és \
kinyitja az ajtót. További sok szerencsét! - kiáltja utánad. Felveszed az \
arany színű mellvértet. Erősebbnek érzed magad tőle, nem is csoda, hiszen mind \
a négy alapképességed egyel javult. Fél óra gyaloglás után egy \
útkereszteződéshez érsz.")
        elag21()
    else:
        print("Hát ez nem sikerült. Sebaj, egyszer még próbálkozhatsz. Dobj \
újra, üss entert.")
        válasz = input('')
        kocka1 = random.randint(1,6)
        kocka2 = random.randint(1,6)
        kocka = kocka1 + kocka2
        print(f"{kocka1}-t és {kocka2}-t dobtál, ez összesen {kocka}")
        if kocka == 7:
            print("\nSzerencséd lett végül - kiáltja a gremlin. \
Amit ígértem, azt megtartom. Átadja a varázstárgyat és kinyitja az ajtót. \
További sok szerencsét! - kiáltja utánad. Felveszed az arany színű mellvértet. \
Erősebbnek érzed magad tőle, nem is csoda, hiszen mind a négy alapképességed \
egyel javult. Fél óra gyaloglás után egy útkereszteződéshez érsz.")
            elag21()
        else:
            print("\nNincs szerencséd. A gremlin fogja a láncos vasgolyóját és \
fejbever vele.")
            dead()


def gremlin1():
    válasz = input("> ")
    válaszlist = ['igen', '']
    if válasz in válaszlist:
        gremlin2()
    elif válasz == 'nem':
        print("\nNeeem? A gremlin értetlenül néz rád, majd fog egy láncos \
vasgolyót és fejbever vele.")
        dead()
    else:
        print("\nNem értem mit motyogsz, próbáld újra.")
        gremlin1()


def gremlin():
    print("\n\nKözelebb lépsz mosolyogva, de a gremlin még mindig szigorúan néz \
rád. Elmondod neki, hogy a szövetség kardját keresed és át szeretnél \
menni az ajtón.\n")
    print("Szerencséd van, az Armor of Wonder nálam van - mondja - épp a minap \
szereztem egy balektől, aki pont úgy nézett ki mint te. Átengedlek és a \
varázstárgyat is megkapod, de ehhez játszanod kell velem. Ha nyersz, tovább \
mehetsz, ha nem, büntetés a jutalmad.\n")

    print("Rendben, mondod, miről van szó?\n")
    print("Itt van két hatos dobókocka, hetest kell dobnod, kétszer \
próbálozhatsz. Készen állsz?")
    gremlin1()


def jobb_ajtó():
    print("\nAz ajtó nyikorogva kinyílik, egy lépcső vezet egy barlang mélyére.\
 Teljesen sötét van. Ahogy botorkálsz le a lépcsőn, megbotlasz és leesel. \
Kitörik a nyakad. Így jár az, aki a könnyebik utat választja.")

def dead():
    print("Kalandod itt véget ért.")
    exit(0)


def start():
    válasz = input("> ")

    bal = ['bal', 'balra', 'gremlin']
    jobb = ['jobb', 'jobbra']
    #
    # for h in range(len(balra)):
    if válasz in bal:
        gremlin()
    # for h in range(len(jobbra)):
    elif válasz in jobb:
        jobb_ajtó()
        dead()

    else:
        print("Nem értem, próbáld újra.")
        start()

start()
