from math import sqrt
import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def prim_e(n):
    """ Teszteli az n számot, hogy prím-e.  """
    i = 2

    if n == 1:
        return False
    if n == 2:
        return True

    while i <= int(sqrt(n)):
        if n % i == 0:
            return False 
            break
        else:
            i+=1
    return True


def primek_szama(lista):
    prime_numbers = 0
    for i in lista:
        if prim_e(i) == True:
            prime_numbers += 1
    return prime_numbers

teszt(primek_szama([42, 4, 7, 11, 1, 13]) == 3)
teszt(primek_szama([42, 4, 7, 11, 1, 13, 2]) == 4)
teszt(primek_szama([42, 4, 7, 11, 1, 13, 4]) != 4)

