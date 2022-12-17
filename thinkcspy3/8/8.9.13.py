from teszt import teszt

def alapos_torles(sztring1, sztring2):
    while True:
        e = sztring2.find(sztring1)
        if e != -1:
            f = sztring2.find(sztring1) + len(sztring1)
            sztring2 = sztring2[:e] + sztring2[f:]
        else:
            return sztring2

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(alapos_torles("an", "banán") == "bán")
    teszt(alapos_torles("pa", "papaja") == "ja")
    teszt(alapos_torles("pa", "Papaja") == "Paja")
    teszt(alapos_torles("alma", "kerékpár") == "kerékpár")
    teszt(alapos_torles("pa", "ppapaa" ) == "")   

tesztkeszlet()