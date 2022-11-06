# Szöveg sorainak fordított sorrendben való beírása új file-ba

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/pelda.txt",)
h = f.readlines()
h.reverse()
f.close()

g = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/pelda_ford.txt", "w")

for i in h:
    g.write(i)
g.close()

