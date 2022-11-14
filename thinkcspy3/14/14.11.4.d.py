# 14.11.4.d Az n királynő probléma egy szimmetriacsaládja

megoldas = [0, 4, 7, 5, 2, 6, 1, 3]

def n_queen_symmetries(megoldas):
    """   Az n királynő probléma egy szimmetriacsaládja   """

    symmetries = []
    symmetries.append(megoldas)

# Tükrözés az x-tengelyre
    yaxis = megoldas[:]
    yaxis.reverse()
    symmetries.append(yaxis)

# Tükrözés az y-tengelyre
    xaxis = []
    xaxis_meg = megoldas[:]
    for i in range(len(megoldas)):
        xaxis_meg[i] = (len(megoldas) - 1) - megoldas[i]
        xaxis.append(xaxis_meg[i])
    symmetries.append(xaxis)

# Elforgatás 90 fokkal
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    symmetries.append(rotate90)

# Elforgatás 180 fokkal
    rotate180 = []
    rotate180_meg = megoldas[:]
    rotate180_meg.reverse()
    for i in rotate180_meg:
        rotate180.append(len(megoldas) - 1 - i)
    symmetries.append(rotate180)

# Elforgatás 270 fokkal
    rotate270 = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        y = x - megoldas.index(z)
        rotate270.append(y)
        z += 1
    symmetries.append(rotate270)

#Tükrözés a bal(\) szimmetria átlóra
    mirrorleft = []
    x = len(megoldas) - 1
    z = x
    while z != -1:
        y = x - megoldas.index(z)
        mirrorleft.append(y)
        z -= 1
    symmetries.append(mirrorleft)

#Tükrözés a jobb(/) szimmetria főátlóra
    mirrorright = []
    x = len(megoldas) - 1
    z = 0
    while z != x + 1:
        mirrorright.append(megoldas.index(z))
        z += 1
    symmetries.append(mirrorright)
    return symmetries

print(n_queen_symmetries(megoldas))