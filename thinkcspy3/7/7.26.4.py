from unittest import teszt

n = 5


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
    
    teszt(count_n_words(['egy', 'három', 'öt']) == 1)
    teszt(count_n_words([55555, 'három']) == 1)
    teszt(count_n_words(['nyugi', 'nyulak', 'tyukok']) == 1)


tesztkeszlet()