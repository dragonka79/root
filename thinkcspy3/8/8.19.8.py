from teszt import teszt

def tukor(sztring):
    tukor_string = sztring + sztring[::-1]
    return tukor_string

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(tukor("jo") == "jooj")
    teszt(tukor("Python") == "PythonnohtyP")
    teszt(tukor("") == "")
    teszt(tukor("a") == "aa")

tesztkeszlet()