import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt
from random import shuffle

szamsor = list(range(1,50))
shuffle(szamsor)
huzas = szamsor[:6]

szelveny = [1, 2, 3, 4, 5]

def lotto_talalat(szelveny, huzas):
    j = 0
    for i in huzas:
        if i in szelveny:
            j += 1
    return j

# teszt(lotto_talalat([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)
print(huzas)
print(f"Találatok száma: {lotto_talalat(szelveny, huzas)}")
