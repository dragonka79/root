# lottóhúzás, 6 a 49-ből

from random import shuffle

szamsor = list(range(1,50))
shuffle(szamsor)
print(szamsor[:6])