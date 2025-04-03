#### Teljes keresés
# 14.2 Visszatér a keresett elem listabeli indexével. Ha a keresett elem nincs a listában
# -1 értékkel tér vissza

from teszt import teszt

baratok = ["Péter", "Zoltán", "János", "Kata", "Zita", "Sándor", "Panni"]

def teljes_kereses(xs, ertek):
    """ Keresse meg és térjen vissza az érték indexével az xs sorozatban. """
    for (i, v) in enumerate(xs):
        if v == ertek:
            return i
    return -1       # Ha nincs az érték a listában, akkor a for ciklus nem ad vissza értéket; a teljes_keresés tér vissza -1-gyel


print(teszt(teljes_kereses(baratok, "Zoltán") == 1))
print(teszt(teljes_kereses(baratok, "Péter") == 0))
print(teszt(teljes_kereses(baratok, "Panni") == 6))
print(teszt(teljes_kereses(baratok, "Béla") == -1))

print(teljes_kereses(baratok, "Zoltán"))
print(teljes_kereses(baratok, "Béla"))