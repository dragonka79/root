from unittest import teszt

def sum_negative_list(lista):
    """Sums up all the negative numbers in a list"""
    sumup = 0
    for i in lista:
        if  i < 0:
            sumup += i
        continue
    return sumup

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(sum_negative_list([1, 2, 3, 4, -5]) == -5)
    teszt(sum_negative_list([0]) == 0)
    teszt(sum_negative_list([3, 12, -24, 36, -108]) == -132)
    teszt(sum_negative_list([1, -1, -2]) == -3)

tesztkeszlet()