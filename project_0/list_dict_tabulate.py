from pprint import pprint
from tabulate import tabulate


l = [
    {'ip': '10.1.1.1',
    'subnet': '32',
    'name': 'loopback'},
    {'ip': '12.12.12.12',
    'subnet': '24',
    'name': 'internal'}
]

print(l, '\n')
pprint(l)
print('\n')

# for (key,value) in l.items():
    # print(f'{key:>12} : {value:>15}')
print(tabulate(l, headers = 'keys'))