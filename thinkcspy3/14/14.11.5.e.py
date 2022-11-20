import sys
sys.path.insert(0, 'C:/Users/a44793837/OneDrive - Deutsche Telekom AG/python/moduls/')
from teszt import teszt

my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

primek = [2,3,5,7,11,13,17,19,23,27,29,31,37,41,43,49]

def hianyzo_primek(my_tickets):
    ticket_numbers = []

    # Egy listába rakja a my_tickets elemeit és rendezi
    for i in my_tickets:
        ticket_numbers.extend(i)
        ticket_numbers.sort()
        numbers_pure = []

    #Kiszedi a duplikált elemeket a ticket_numbers-ből
    aktualis_elem = None
    for e in ticket_numbers:
        if e != aktualis_elem:
            numbers_pure.append(e)
            aktualis_elem = e

    # Visszatér a csak a második listában(primek) szereplő elemekkel
    eredmeny = []
    xi = 0  # Ez az index ami fut numbers_pure-on
    yi = 0  # Ez az index, ami fut primek-en

    while True:
        if xi >= len(numbers_pure):
            return eredmeny
        if yi >= len(primek):
            eredmeny.extend(numbers_pure[xi:])
            return eredmeny

        if numbers_pure[xi] == primek[yi]:
            xi += 1
            yi += 1
        elif primek[yi] < numbers_pure[xi]:
            eredmeny.append(primek[yi])
            yi += 1
        else:
            xi += 1
    return eredmeny
def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.  """
    teszt(hianyzo_primek(my_tickets) == [3, 27, 29])

# print(hianyzo_primek(my_tickets))
tesztkeszlet()
