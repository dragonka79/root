def tavolsag(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    negyzetosszeg = dx*dx + dy*dy
    eredmeny = negyzetosszeg**0.5
    return eredmeny
#teszt
print(tavolsag(1, 2, 4, 6))