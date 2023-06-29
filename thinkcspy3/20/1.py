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
hun2esp2['egy'] += 2


hun2esp2['négy'] = 'quatros'
# print(hun2esp2)

# for k in hun2esp2.keys():
#     print(f'A(z) {k} metódus leképezi a {hun2esp2[k]} értéket')
print('\t')
# for k in hun2esp2:
#     print(f'A(z) {k} metódus leképezi a {hun2esp2[k]} értéket')

print(list(hun2esp2.keys()))
print(list(hun2esp2.values()))
print(list(hun2esp2.items()))
