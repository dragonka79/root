from teszt import teszt

class Pont:
    """ Pont osztály (x, y) koordináták reprezentálására és manipulálására. """
    def __init__(self, x=0, y=0):
        """ Egy új, x, y koordinátán álló pont készítése. """
        self.x = x
        self.y = y
    
    def tukrozes_x_tengelyre(p):
        """Visszatér egy pont x-tengelyre vett tükrözésével"""
        return(p.x, -p.y)

p = Pont(1, -2)
q = Pont(2, 0)
# print(p.tukrozes_x_tengelyre())
# print(q.tukrozes_x_tengelyre())

teszt(p.tukrozes_x_tengelyre()) == (1, 2)
teszt(q.tukrozes_x_tengelyre()) == (2, 0)