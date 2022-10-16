from teszt import teszt

def szorzas_skalarral(s, v):
    """
    Visszadja egy v vektor(lista) s skalárral való szorzatát
    """
    skalar_szorzat = []
    for i in range(len(v)):
        skalar_szorzat.append(s * v[i])
    return skalar_szorzat

teszt(szorzas_skalarral(5, [1, 2]) == [5, 10])
teszt(szorzas_skalarral(3, [1, 0, -1]) == [3, 0, -3])
teszt(szorzas_skalarral(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])

