from unittest import teszt

def orakra_valtas(masodperc):
    return int(masodperc // 3600)


def percekre_valtas(masodperc):
    a = masodperc - (orakra_valtas(masodperc) * 3600)
    return int(a // 60)


def masodpercekre_valtas(masodperc):
    a = masodperc - (orakra_valtas(masodperc) * 3600)
    b = a - (percekre_valtas(a) * 60)
    return b

teszt(orakra_valtas(9010) == 2)
teszt(percekre_valtas(9010) == 30)
teszt(masodpercekre_valtas(9010) == 10)