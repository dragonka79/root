from cmath import sqrt
from unittest import teszt
from math import sqrt
from math import pow

def atfogo(a, b):
    if a > 0 and b > 0:
        return sqrt(pow(a, 2) + pow(b, 2))
    else:
        return None

teszt(atfogo(3, 4) == 5.0)
teszt(atfogo(12, 5) == 13.0)
teszt(atfogo(24, 7) == 25.0)
teszt(atfogo(9, 12) == 15.0)
teszt(atfogo(0, 12) == None)
teszt(atfogo(-9, 12) == None)