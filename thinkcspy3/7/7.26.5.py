from unittest import teszt

def sum_before_even(lista):
    sumup = 0
    for i in lista:
        if i % 2 != 0:
            sumup += i
        else:
            break
    return sumup

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(sum_before_even([1, 3, 5, 7]) == 16)
    teszt(sum_before_even([2, 3]) == 0)
    teszt(sum_before_even([-1, 1, 2, 1]) == 0)


tesztkeszlet()

