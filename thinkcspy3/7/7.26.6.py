from unittest import teszt

def count_nem(lista):
    """
    Megszámolja a szavakat az első 'nem'-ig egy listában(a 'nem' benne van).
    """
    counter = 0
    for i in lista:
        counter += 1
        if i != "nem":
            continue
        else:
            break
    return counter

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(count_nem(['igen', 'nem']) == 2)
    teszt(count_nem(['igen','igen','igen','nem','igen']) == 4)
    teszt(count_nem([]) == 0)
    teszt(count_nem(['nem', 'nem']) == 1)

tesztkeszlet()   

