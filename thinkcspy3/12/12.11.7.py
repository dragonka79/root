import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

def cserel(regi, uj, s):
    """ Cseréld az s-ben a regi paraméter összes előfordulását az uj-ra. """
    return(uj.join(s.split(regi)))

teszt(cserel(",", ";", "ez, az, és valami más dolog") == "ez; az; és valami más dolog")
teszt(cserel(" ", "**", "A szavak most csillaggal vannak elválasztva.") == "A**szavak**most**csillaggal**vannak**elválasztva.")

