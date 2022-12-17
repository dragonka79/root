lista1 = [0, 15, 30, 40]
lista2 = ['előny_A', 'nyer_A','előny_B', 'nyer_B']
szamlalo = 1

for i in lista1:
    for j in lista1:
        print(f'{szamlalo}: ({i}, {j})')
        szamlalo += 1

for i in lista2:
    print(f'{szamlalo}: {i}')
    szamlalo += 1