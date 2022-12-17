# Csak az adott stringet tartalmazó sorok kiíratása

#### 1. Megoldás

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/13112sample.txt")
j = 'info'

while True:
    sorbe = f.readline()
    if j in sorbe:
        print(sorbe, end ='')
    if len(sorbe) == 0:
        break
    else:
        continue

f.close()

#### 2. (egyszerűbb) Megoldás

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/13112sample.txt")
h = f.readlines() # a file-t soronként bepakolom egy listába
f.close()
j = 'info'

for i in h:
    if j in i:
        print(i, end='')


