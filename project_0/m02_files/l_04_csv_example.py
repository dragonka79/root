from l_00_inventory import csv_inventory
import csv
from pprint import pprint
from tabulate import tabulate
import filecmp

# PART I: ----- Same procedure as for JSON, YAML, XML --------------------

# CONVERT INVENTORY TO CSV AND WRITE TO FILE
with open("m02_files/l_00_inventory.csv", "w") as csv_out:
    csv_writer = csv.writer(csv_out)
    csv_writer.writerows(csv_inventory)

# READ CSV INVENTORY FROM FILE
# A saved_csv_inventory egy beágyazott lista, a lista elemei listák, amely elemek 
# egy-egy iterációval kerülnek be.

with open("m02_files/l_00_inventory.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    saved_csv_inventory = list()
    for device in csv_reader:
        saved_csv_inventory.append(device)

# PRINT CSV INVENTORY STRING
print("l_00_inventory.csv file:\n", saved_csv_inventory)

# PRETTY PRINT
print("\ncsv pretty version:")
pprint(saved_csv_inventory)

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
if saved_csv_inventory == csv_inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")

# TURN LIST OF LISTS INTO DICTIONARY
devices = list()
for device_index in range(1, len(csv_inventory)): # len(csv_inventory) = nr. of items(lists)
    device = dict()
    for index, header in enumerate(csv_inventory[0]):
        device[header] = csv_inventory[device_index][index] # The key: value pairs
    devices.append(device)

# PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices as list of dicts --------------------")
pprint(devices)

# PART II: ----- Read CSV file created by spreadsheet --------------------

# READ FROM CSV FILE CREATED BY SPREADSHEET
with open("m02_files/devices_for_csv_example - Sheet1.csv", "r") as csv_in:
    csv_reader = csv.reader(csv_in)
    from_spreadsheet_csv_inventory = list()
    for device in csv_reader:
        from_spreadsheet_csv_inventory.append(device)

# TURN LIST OF LISTS INTO DICTIONARY
devices = list()
for device_index in range(1, len(from_spreadsheet_csv_inventory)):
    device = dict()
    for index, header in enumerate(from_spreadsheet_csv_inventory[0]):
        device[header] = from_spreadsheet_csv_inventory[device_index][index]
    devices.append(device)

# PRETTY PRINT DEVICES AS LIST OF DICTS
print("\n----- Devices from spreadsheet --------------------")
pprint(devices)

print("\n----- tabulate output of devices from spreadsheet --------------------")
print("\n", tabulate(devices, headers="keys"))

# CONVERT PYTHON DATA BACK INTO CSV
headers = devices[0].keys()
with open("l_00_inventory_back_to_csv.csv", "w") as csv_out:
    csv_writer = csv.DictWriter(csv_out, headers)
    csv_writer.writeheader()
    csv_writer.writerows(devices)

print("\n----- compare spreadsheet data with our version --------------------")
if filecmp.cmp("m02_files/devices_for_csv_example - Sheet1.csv", "l_00_inventory_back_to_csv.csv"):
    print("-- worked: spreadsheet devices equals our version")
else:
    print("-- failed BUT EXPECTED TO FAIL: spreadsheet devices different from our version")