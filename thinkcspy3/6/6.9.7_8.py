from unittest import teszt

def masodpercre_valtas(ora, perc, masodperc):
    return int(ora * 3600 + perc * 60 + masodperc)

teszt(masodpercre_valtas(2, 30, 10) == 9010)
teszt(masodpercre_valtas(2, 0, 0) == 7200)
teszt(masodpercre_valtas(0, 2, 0) == 120)
teszt(masodpercre_valtas(0, 0, 42) == 42)
teszt(masodpercre_valtas(0, -10, 10) == -590)
teszt(masodpercre_valtas(2.5, 0, 10.71) == 9010)
teszt(masodpercre_valtas(2.433,0,0) == 8758)