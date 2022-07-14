from unittest import teszt

# 6.9.1

egtajak = ['É' , 'K' , 'D', 'Ny', 'É']

def fordulj_orajarasi_iranyba(x):
    """Visszadja a következő égtáj rövidítését órajárás szerint"""
    
    if x in egtajak:
        y = egtajak.index(x) # x indexe a listában
        return egtajak[y +1] # x-nél egyel nagyobb indexű elem a listában
    else:
        return None


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(fordulj_orajarasi_iranyba('É') == 'K')
    teszt(fordulj_orajarasi_iranyba('D') == 'Ny')
    teszt(fordulj_orajarasi_iranyba('Ny') == 'É')
    teszt(fordulj_orajarasi_iranyba('ny') == None)
    teszt(fordulj_orajarasi_iranyba(-3.14) == None)
    teszt(fordulj_orajarasi_iranyba(42) == None)
    teszt(fordulj_orajarasi_iranyba("ostobaság") == None)

tesztkeszlet()

