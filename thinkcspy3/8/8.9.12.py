from teszt import teszt

def torles(sztring1, sztring2):
    sztring_torolt = ""
    e = sztring2.find(sztring1)
    if e != -1:
        f = sztring2.find(sztring1) + len(sztring1)
        sztring_torolt = sztring2[:e] + sztring2[f:]
        return sztring_torolt
    return sztring2

def tesztkeszlet():
    """ Az ehhez a modulhoz (fájlhoz) tartozó tesztkészlet futtatása.
    """
    teszt(torles("alma", "almafa") == "fa")
    teszt(torles("an", "banán") == "bán")
    teszt(torles("pa", "papaja") == "paja")
    teszt(torles("pa", "Papaja") == "Paja")
    teszt(torles("alma", "kerékpár") == "kerékpár")

tesztkeszlet()

# teszt(torles("alma", "kerékpár") == "kerékpár")
