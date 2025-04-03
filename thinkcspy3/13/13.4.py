# A forrás file-t sorba rendezve egy új file-ba írja bele

# import sys
# sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/')

f = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/baratok.txt", "r")
xs = f.readlines() # Beolvassa f-et soronként
f.close()

xs.sort()

g = open("C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/13/rendezett.txt", "w")
for v in xs:
    g.write(v)
g.close()