from unittest import teszt

n = 5

lista1 = ['egy', 'három', 'öt']
lista2 = [55555, 'három']
lista3 = ['nyugi', 'nyulak', 'tyukok']

def count_n_words(lista):
    """Counts the n letter words in a list"""
    counter = 0
    for i in lista:
        try:
            if len(i) == n:
                counter += 1
        except:
            continue
    return counter


def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása."""
    
    teszt(count_n_words(lista1) == 1)
    teszt(count_n_words(lista2) == 1)
    teszt(count_n_words(lista3) == 1)


tesztkeszlet()