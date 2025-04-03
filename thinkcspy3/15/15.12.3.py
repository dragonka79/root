from teszt import teszt

class Pont:
    """ Pont osztály (x, y) koordináták reprezentálására és manipulálására. """
    def __init__(self, x=0, y=0):
        """ Egy új, x, y koordinátán álló pont készítése. """
        self.x = x
        self.y = y
    
    def origotol_mert_meredekseg(p):
        """Visszatér egy pont és az origó által meghat. szakasz meredségével"""
        if p.x != 0:
            tg = p.y / p.x
        else:
            tg = 0
        return tg

p = Pont(4, 10)
q = Pont(0, 3)
# print(p.origotol_mert_meredekseg())
# print(q.origotol_mert_meredekseg())

teszt(p.origotol_mert_meredekseg()) == (2.5)
teszt(p.origotol_mert_meredekseg()) == (0)