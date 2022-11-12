import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def osszefesul_kozos(xs, ys):
    """ Összefésül 2 rendezett listából a közös elemeket
        Csak azokat az elemeket adja vissza, melyek mindkét listába benne vannak.
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs) or yi >= len(ys) : # Ha a két lista valamelyikének a végére értünk
            break
        if xs[xi] == ys[yi]:
            eredmeny.append(xs[xi])
            xi += 1
            yi += 1
        elif xs[xi] < ys[yi]:
            xi += 1
        elif xs[xi] > ys[yi]:
            yi += 1
    return eredmeny # Készen vagyunk

xs = [1, 2, 3, 4, 5]
ys = [1, 3, 5, 6]

xt = [1, 2, 3, 4, 5]
yt = [1, 2, 3, 4, 5]

xn = [1, 3, 5, 7, 10]
yn = [2, 4, 6, 8, 10]

teszt(osszefesul_kozos(xs, []) == [])
teszt(osszefesul_kozos([], ys) == [])
teszt(osszefesul_kozos([], []) == [])
teszt(osszefesul_kozos(xs, ys) == [1, 3, 5])
teszt(osszefesul_kozos(xt, yt) == xt)
teszt(osszefesul_kozos(xn, yn) == [10])
teszt(osszefesul_kozos(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
["cica"])

        