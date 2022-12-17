import sys
from teszt import teszt

def cserel(s, regi, uj):
    """  Karaktereket cserél ki egy karakterláncban  """
    split_lista = s.split(regi)
# Az eredeti stringbe íratom vissza hogy a harmadik teszt lefusson
    string = uj.join(split_lista)
    return string

def tesztkeszlet_cserel():
    s = "Kerek a gömb, gömbszerű!"
    """ A 11.22.10 a modulhoz tartozó tesztkészlet futtatása.  """
    teszt(cserel("Mississippi", "i", "I") == "MIssIssIppI")
    teszt(cserel(s, "öm", "om") == "Kerek a gomb, gombszerű!")
    teszt(cserel(s, "o", "ö") == "Kerek a gömb, gömbszerű!")

# print(cserel(string, regi, uj))
tesztkeszlet_cserel()