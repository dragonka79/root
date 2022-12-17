from teszt import teszt

def vektorok_osszege(u, v):
    """
    Visszatér 2 azonosan hosszú lista esetén olyan listával, amely elemei az azonos indexeken lévő bemeneti listák elemeinek összegéből keletkezett
    """

    osszeg = []
    for i in range(len(u)):
        osszeg.append(u[i] + v[i])
    return osszeg

teszt(vektorok_osszege([1, 1], [1, 1]) == [2, 2])
teszt(vektorok_osszege([1, 2], [1, 4]) == [2, 6])
teszt(vektorok_osszege([1, 2, 1], [1, 4, 3]) == [2, 6, 4])