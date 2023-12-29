from collections import namedtuple
from pprint import pprint

Location = namedtuple('Location', ["country","region","city", "postcode", "street", "house_number", "door", "year"])
location_1 = Location("Hungary","Hajdú-Bihar","Debrecen",4028, "Kossuth",22, 32, 2021)
location_2 = Location("Hungary","Baranya","Pécs",7600, "Petőfi",102, 48, 2019)

print(" --- Printing location_1 --- \n")

print(location_1.country)
print(location_1.region)
print(location_1.city)
print(location_1.postcode)
print(location_1.street)
print(location_1.house_number)
print(location_1.door)
print(location_1.year)

print(" --- Printing location_2 --- \n")

print(location_2.country)
print(location_2.region)
print(location_2.city)
print(location_2.postcode)
print(location_2.street)
print(location_2.house_number)
print(location_2.door)
print(location_2.year)

print(" --- Pretty printing location_1  --- \n")
pprint(location_1)