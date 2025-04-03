#Bináris file másolása

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/SuperPuttyPortable.7z", "rb")
g = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/SuperPuttyPortable_python_cp.7z", "wb")

while True:
    buff = f.read(1024)
    if len(buff) == 0:
        break
    g.write(buff)

f.close()
g.close()