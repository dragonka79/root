
xs = [12, 16, 17, 24, 29, 30]
def paros_szamok_kivalogat(xs):
    """
    Kiválogatja a páros számokat egy listából és egy másik listában tárolja
    """
    paros = []
    for i in xs:
        if i % 2 == 1: # Ha a szám páratlan ...
            continue # ... ne dolgozd fel
        else:
            paros.append(i)
    return paros

print(paros_szamok_kivalogat(xs))