import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def osszefesul_masodik(xs, ys):
    """ Összefésül 2 rendezett listából a közös elemeket
        Csak azokat az elemeket adja vissza, melyek benne vannak a második listában, de nincsenek az
        elsőben.
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if yi >= len(ys): # Ha a második lista végére értünk
            break
        if xi >= len(xs) : 
            eredmeny.extend(ys[yi:])
            break
        if xs[xi] == ys[yi]:
            xi += 1
            yi += 1
        elif ys[yi] < xs[xi]:
            eredmeny.append(ys[yi])
            yi += 1
        else:
            xi += 1
    return eredmeny # Készen vagyunk

xs = [1, 2, 3, 4, 5]
ys = [1, 3, 5, 6]

xt = [1, 2, 3, 4, 5]
yt = [1, 2, 3, 4, 5]

xn = [1, 3, 5, 7, 10]
yn = [2, 4, 6, 8, 10]

xz = [1, 3, 4, 5, 7, 10]
yz = [2, 4, 6, 8, 10]

teszt(osszefesul_masodik(xs, []) == [])
teszt(osszefesul_masodik([], ys) == ys)
teszt(osszefesul_masodik([], []) == [])
teszt(osszefesul_masodik(xs, ys) == [6])
teszt(osszefesul_masodik(xt, yt) == [])
teszt(osszefesul_masodik(xn, yn) == [2, 4, 6, 8])
teszt(osszefesul_masodik(xz, yz) == [2, 6, 8])
teszt(osszefesul_masodik(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
["kakas", "medve"])

        