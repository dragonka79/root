class Pont:
    """ Pont osztály (x, y) koordináták reprezentálására és manipulálására. """
    def __init__(self, x=0, y=0):
        """ Egy új, x, y koordinátán álló pont készítése. """
        self.x = x
        self.y = y
    
    def tavolsag(p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        negyzetosszeg = dx*dx + dy*dy
        eredmeny = negyzetosszeg**0.5
        return eredmeny

p1 = Pont(1, 2)
p2 = Pont(4, 6)
d = p1.tavolsag(p2)
print(d)