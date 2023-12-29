from enum import Enum

CISCO = "Cisco"


class Vendor:
    CISCO = "Cisco Systems"
    JUNIPER = "juniper"
    ARISTA = "arista"

print(CISCO)
print(Vendor.CISCO)

#  Enum
# https://docs.python.org/3/library/enum.html

class Vendors(Enum):
    CISCO = 1
    JUNIPER = 2
    ARISTA = 3

print(Vendors.CISCO.name)
print(Vendors.CISCO.value)

# Printing all items using * just as in a for loop

for vendors in Vendors:
    print(vendors)
print('\n')

print(*Vendors, sep='\n')   
print('\n')


L = [['some'], ['lists'], ['here']]
print('The lists are:', *L, sep='\n')