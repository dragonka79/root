# Csak az adott stringet tartalmazó sorok kiíratása

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/13112sample.txt",)
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


