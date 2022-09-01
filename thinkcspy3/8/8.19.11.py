from teszt import teszt

def szamlalas(sztring1, sztring2):
    count = 0
    i = 0
    while i <= len(sztring2) - len(sztring1):
        if sztring1 == sztring2[i:i + len(sztring1)]:
            count += 1
        i += 1
    return count

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(szamlalas("gö", "görögös") == 2)
    teszt(szamlalas("pa", "papaja") == 2)
    teszt(szamlalas("apa", "papaja") == 1)
    teszt(szamlalas("papa", "papaja") == 1)
    teszt(szamlalas("apap", "papaja") == 0)
    teszt(szamlalas("aaa", "aaaaaa") == 4)

tesztkeszlet()
