from teszt import teszt

class Pont:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def atmeno_egyenes(self, p2):
        """ Két ponton átmenő egyenes egyenlete """
        if self.x != p2.x:
            m = int((p2.y - self.y) / (p2.x - self.x))
            c = int(( (self.y * p2.x) - (p2.y * self.x) ) / (p2.x - self.x))
            return(m, c)
        elif (self.x, self.y) == (p2.x, p2.y):
            return("A két pont azonos")
        else:
            return("x = {0}".format(self.x))

p = Pont(4, 11)
q = Pont(6, 15)
# print(p.atmeno_egyenes(q))

teszt(p.atmeno_egyenes(q)) == (2,3 )