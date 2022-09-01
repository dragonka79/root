from teszt import teszt

def betu_eltuntetes(betu, sztring):
    betu_nelkul = ""
    for i in sztring:
        if i != betu:
            betu_nelkul += i
    return betu_nelkul

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(betu_eltuntetes("a", "alma") == "lm")
    teszt(betu_eltuntetes("a", "banán") == "bnán")
    teszt(betu_eltuntetes("z", "banán") == "banán")
    teszt(betu_eltuntetes("e", "Kerepes") == "Krps")
    teszt(betu_eltuntetes("b", "") == "")
    teszt(betu_eltuntetes("b", "c") == "c")

tesztkeszlet()