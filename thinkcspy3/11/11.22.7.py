from teszt import teszt

def skalaris_szorzat(u, v):
    """
    Két vektor(lista) skaláris szorzata
    """
    skalaris = 0
    for i in range(len(u)):
        skalaris += u[i] * v[i]
    return skalaris

teszt(skalaris_szorzat([1, 1], [1, 1]) == 2)
teszt(skalaris_szorzat([1, 2], [1, 4]) == 9)
teszt(skalaris_szorzat([1, 2, 1], [1, 4, 3]) == 12)