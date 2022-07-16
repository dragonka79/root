from unittest import teszt

def celsiusra_valtas(f):
    """Fahrenheitben megadott értéket Celsius fokra vált át"""
    return round((f - 32) * 5 /9)


def tesztkeszlet_celsiusra_valtas():
    teszt(celsiusra_valtas(212) == 100) # A víz forráspontja
    teszt(celsiusra_valtas(32) == 0) # A víz fagyáspontja
    teszt(celsiusra_valtas(-40) == -40) # Ó, micsoda érdekes eset!
    teszt(celsiusra_valtas(36) == 2)
    teszt(celsiusra_valtas(37) == 3)
    teszt(celsiusra_valtas(38) == 3)
    teszt(celsiusra_valtas(39) == 4)


def fahrenheitre_valtas(c):
    """ Celsiusban megadott értéket Fahrenheit fokra vált át"""
    return round((9 / 5 * c + 32))


def tesztkeszlet_fahrenheitre_valtas():
    teszt(fahrenheitre_valtas(0) == 32)
    teszt(fahrenheitre_valtas(100) == 212)
    teszt(fahrenheitre_valtas(-40) == -40)
    teszt(fahrenheitre_valtas(12) == 54)
    teszt(fahrenheitre_valtas(18) == 64)
    teszt(fahrenheitre_valtas(-48) == -54)


tesztkeszlet_celsiusra_valtas()
tesztkeszlet_fahrenheitre_valtas()