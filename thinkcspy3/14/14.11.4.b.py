#b. Írj egy függvényt, amely egy megoldást tükröz az X tengelyre.

def x_tengelyre_tukroz(list):
    revlistx = []
    for i in range(len(list)):
        k = int(len(list) - 1 - list[i])
        revlistx.append(k)
    return revlistx

x = [0,4,7,5,2,6,1,3]
print(x)
print(x_tengelyre_tukroz(x))
