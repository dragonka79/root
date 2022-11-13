#b. Írj egy függvényt, amely egy megoldást tükröz az X tengelyre.

def x_tengelyre_tukroz(megoldas):
    revmegoldasx = []
    for i in range(len(megoldas)):
        k = int(len(megoldas) - 1 - megoldas[i])
        revmegoldasx.append(k)
    return revmegoldasx

x = [0,4,7,5,2,6,1,3]
print(x)
print(x_tengelyre_tukroz(x))
