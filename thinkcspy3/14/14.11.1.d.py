import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def osszefesul_kizaro(xs, ys):
    """ Összefésül 2 rendezett listából a közös elemeket
        Csak azokat az elemeket adja vissza, melyek vagy az elsőben vagy a másodikban vannak benne.
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs): # Ha az első lista végére értünk
            eredmeny.extend(ys[yi:])
            break
        if yi >= len(ys) : 
            eredmeny.extend(xs[xi:])
            break
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
        else:
            eredmeny.append(ys[yi])
            yi += 1
    return eredmeny # Készen vagyunk

xs = [1, 2, 3, 4, 5]
ys = [1, 3, 5, 6]

xt = [1, 2, 3, 4, 5]
yt = [1, 2, 3, 4, 5]

xn = [1, 3, 5, 7, 10]
yn = [2, 4, 6, 8, 10]

xz = [1, 3, 4, 5, 5, 7, 10]
yz = [2, 4, 6, 8, 10]

teszt(osszefesul_kizaro(xs, []) == xs)
teszt(osszefesul_kizaro([], ys) == ys)
teszt(osszefesul_kizaro([], []) == [])
teszt(osszefesul_kizaro(xs, ys) == [2, 4, 6])
teszt(osszefesul_kizaro(xt, yt) == [])
teszt(osszefesul_kizaro(xn, yn) == [1, 2, 3, 4, 5, 6, 7, 8])
teszt(osszefesul_kizaro(xz, yz) == [1, 2, 3, 5, 5, 6, 7, 8])
teszt(osszefesul_kizaro(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
["egér", "kakas", "kutya","medve"])

        


