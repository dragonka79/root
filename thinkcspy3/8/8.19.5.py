from nyelv import irasjelek

hajnal_enek = """
Elkártyáztam a gyenge szívem,
Suhogasd le a szoknyád, hajnal!
Pálinkát lehelek rád szelíden,
Megháglak nehezen, halkan.

Jöjj, Oroszország, vodka-virág,
Nevetés nékem a véred,
Pince-fehérek a volgai fák,
Tejszínű, szűz ez az ének.

Lebukik fejem és úgy zokogok,
Haloványul bennem a bánat,
Veretik körülöttem az ősi dobot,
Szaladok, hajnal, utánad!

Ez a csont-pufogás, ez a hanti rege
Hitemet hirdeti híven,
Kataton bálvány, légy fekete,
Hiszen elkártyáztam a szívem!
"""

szoveg = hajnal_enek
karakter = "ű"

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in irasjelek:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

szavakra_bontas = irasjel_eltavolitas(szoveg).split()
#print(szavakra_bontas)

def karakter_szamlalas(string, karakter):
    szamlalo = 0
    szavak_lista = []
    for ch in string:
        x = ch.lower().find(karakter)
        if x != -1:
            szavak_lista.append(ch)
            szamlalo += 1
    # print(szavak_lista)
    return szamlalo, szavak_lista # Két értékkel tér vissza a függvény

# szamlalo, szavak_lista = karakter_szamlalas(szoveg, karakter)
# print(szamlalo)
# print(szavak_lista)


szam = karakter_szamlalas(szavakra_bontas, karakter)[0]
szo = karakter_szamlalas(szavakra_bontas, karakter)[1]
szazalek = (len(szo) / len(szavakra_bontas)) * 100

print("A szövegben {0} szó áll, melyből {1} szó {2:.2f}%-ban tartalmaz {3} betűt."
.format(len(szavakra_bontas), len(szo), szazalek, karakter))
print(f"A szavak listája a következő: {szo}")