import locale
szo = input("A szavad: ")
locale.setlocale(locale.LC_ALL, "")  # a nyelv beállítása
k = locale.strcoll(szo, "banán") # a két sztring összehasonlítása
if k < 0:
    print("A szavad, a(z) " + szo + ", a banán elé jön.")
elif k > 0:
    print("A szavad, a(z) " + szo + ", a banán után jön.")
else:
    print("Nem, nincs banánunk!")