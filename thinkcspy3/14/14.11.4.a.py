# a. Írj egy függvényt, amely egy megoldást tükröz az Y tengelyre.

def y_tengelyre_tukroz(megoldas):
    revmegoldasy = megoldas[::-1]
    return revmegoldasy

x = [0,4,7,5,2,6,1,3]
print(x)
print(y_tengelyre_tukroz(x))
