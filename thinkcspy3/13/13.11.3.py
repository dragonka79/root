###### 1. Megoldás

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/alice_sample.txt")
g = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/alice_sample_countered.txt", "a")

i = 1

while True:
    l = "{:04d}".format(i)
    n = l + ' '
    szoveg = f.readline()
    if len(szoveg) == 0:
        break
    g.write(str(n))
    g.write(szoveg)
    i += 1

f.close()
g.close()


###### 2. Megoldás

f = open("teszt20.txt", 'r')
h = f.readlines() # a file-t soronként bepakolom egy listába
e = len(h)
f.close()
# print(e)

g = open("teszt21.txt", 'w')
k = 1
while k <= e:
    for v in h:
        l = "{:04d}".format(k) #balról nullákkal töltöm fel a sorszámot
        n = l + ' '
        g.write(n + v)
        k += 1
g.close()