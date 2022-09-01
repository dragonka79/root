from teszt import teszt

def sztring_forditas(sztring):
    rev_string = sztring[::-1]
    return rev_string

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(sztring_forditas("boldog") == "godlob")
    teszt(sztring_forditas("Python") == "nohtyP")
    teszt(sztring_forditas("") == "")
    teszt(sztring_forditas("a") == "a") 

tesztkeszlet()