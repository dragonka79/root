from unittest import teszt

def sum_even_list(lista):
    """Sums up all the even numbers in a list"""
    sumup = 0
    for i in lista:
        if  i % 2 == 0:
            sumup += i
        continue
    return sumup

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(sum_even_list([1, 2, 3, 4, -5]) == 6)
    teszt(sum_even_list([0]) == 0)
    teszt(sum_even_list([3, 12, -24, 36, -108]) == -84)
    teszt(sum_even_list([1, -1, -2]) == -2)

tesztkeszlet()