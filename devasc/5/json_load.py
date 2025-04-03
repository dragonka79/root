## JSON. load = Teljes JSON file-t vár bementre és azt
## Python szótárrá konvertálja
## https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/

import json

with open("/home/zolcs/Downloads/little_stuff/devasc/5/gigabitethernet2.json", "r") as data_read:
    datajson = json.load(data_read)

print(datajson)
print(type(datajson))