import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def osszefesul_kivonas(xs, ys):
    """ Összefésül 2 rendezett listából a közös elemeket
        Azokat az elemeket adja vissza az első listából, amelyeket a második lista egy megegyező eleme nem
        távolít el
        Ugyanaz mint 14.11.1.b
    """
    eredmeny = []
    xi = 0
    yi = 0
    while True:
        if xi >= len(xs): # Ha az első lista végére értünk
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
            yi += 1
    return eredmeny # Készen vagyunk

xs = [1, 2, 3, 4, 5]
ys = [1, 3, 5, 6]

xt = [1, 2, 3, 4, 5]
yt = [1, 2, 3, 4, 5]

xn = [1, 3, 5, 7, 10]
yn = [2, 4, 6, 8, 10]

xz = [1, 3, 4, 5, 7, 10]
yz = [2, 4, 6, 8, 10]

xu = [5,7,11,11,11,12,13]
yu = [7,8,11]

teszt(osszefesul_kivonas(xs, []) == xs)
teszt(osszefesul_kivonas([], ys) == [])
teszt(osszefesul_kivonas([], []) == [])
teszt(osszefesul_kivonas(xs, ys) == [2, 4])
teszt(osszefesul_kivonas(xt, yt) == [])
teszt(osszefesul_kivonas(xn, yn) == [1, 3, 5, 7])
teszt(osszefesul_kivonas(xz, yz) == [1, 3, 5, 7])
teszt(osszefesul_kivonas(["cica", "egér", "kutya"], ["cica", "kakas", "medve"]) ==
["egér", "kutya"])
teszt(osszefesul_kivonas(xu, yu) == [5,11,11,12,13])

        