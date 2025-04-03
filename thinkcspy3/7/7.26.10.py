from unittest import teszt
from math import sqrt

def prim_e(n):
    """Prime test"""
    j = None
    if n >= 2:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                j = False
                break
            else:
                j = True
    elif n == 0 or n == 1:
        j = False
    else:
        return('Pozitív számot adj meg')
    return j


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(prim_e(11) == True)
    teszt(not prim_e(35) == True)
    teszt(prim_e(19981121) == False)
    teszt(prim_e(1) == False)
    teszt(prim_e(-5) == 'Pozitív számot adj meg')
    teszt(prim_e(31636373) == True)

tesztkeszlet()  
# print(prim_e(35)) 