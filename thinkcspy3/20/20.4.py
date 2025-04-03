matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print(matrix[(0,3)])

# De mi van akkor, ha a kért indexen nincs elem (azaz az az elem 0) ?

print(matrix.get((0, 3), 0))  # mivel létezik érték a (0,3)-on ezért annak értékével tér vissza
print(matrix.get((1, 3), 0))  # nem létezik érték (1, 3)-on ezért a 0-val tér vissza a get metódus