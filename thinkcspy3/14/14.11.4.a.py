
from audioop import reverse


# a. Írj egy függvényt, amely egy megoldást tükröz az Y tengelyre.

def y_tengelyre_tukroz(list):
    revlist = list[::-1]
    return revlist

x = [0,4,7,5,2,6,1,3]
print(x)
print(y_tengelyre_tukroz(x))