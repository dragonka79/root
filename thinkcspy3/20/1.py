# hun2esp = {}
# hun2esp["egy"] = "uno"
# hun2esp["kettő"] = "dos"

# print(hun2esp)


# lista = [('egy', 'uno'), ('kettő', 'dos')]

# print(lista)


hun2esp2 = {'egy': 1, 'kettő': 'dos'}

# print(hun2esp2)
# print(hun2esp2['kettő'])
# print(type(hun2esp2['kettő']))
# print(type(hun2esp2['egy']))
# print(type(hun2esp2))

# del hun2esp2['egy']
# hun2esp2['egy'] += 2


# hun2esp2['négy'] = 'quatros'
# print(hun2esp2)

# for k in hun2esp2.keys():
#     print(f'A(z) {k} metódus leképezi a {hun2esp2[k]} értéket')
print('\t')
# for k in hun2esp2:
#     print(f'A(z) {k} metódus leképezi a {hun2esp2[k]} értéket')

# print(list(hun2esp2.keys()))
# print(list(hun2esp2.values()))
# print(list(hun2esp2.items()))

# print('egy' in hun2esp2)
# print('egy' in hun2esp2.keys())
# print('dos' in hun2esp2.values())

# hun2esp3 = hun2esp2
# hun2esp4 = hun2esp2.copy()

# print(hun2esp2 is hun2esp3)
# print(hun2esp2 is hun2esp4)

# hun2esp2["öt"] = 'cing'
# print(hun2esp2, hun2esp3, hun2esp4)


# list2 = [(1, 'egy'), (2, 'kettő')]
# list3 = list2
# list4 = list2.copy()
# print(list3 is list2)
# print(list4 is list2)

known_elements = {0: 0, 1: 1}


def fib(n):
    if n not in known_elements:
        known_elements[n] = fib(n-2) + fib(n-1)
    return known_elements[n]


n = 100
print(fib(n))
