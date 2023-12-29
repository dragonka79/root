from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

# Create an empty list for the devices
devices = list()

# Generating devices with 'For' loop

for index in range(1,10):
    # Create emtpy device dictionary
    device = dict()

    # Name of the device of the key: value pair in the dict; random device name of 3 parts
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # Some vendors of Cisco, Juniper, Arista
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.45"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    device["ip"] = "10.0.0." + str(index)

    # Pretty print of this one device
    # print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")
    print("\n")
        # Add the device to the 'device's list
    devices.append(device)
# Printing the devices as-is
print("\n----- DEVICES AS LIST OF DICTS -------------\n")
pprint(devices)

# Print single device
print("\n ---------- A single device ----------\n")
print(f"{devices[5]}, \n")
pprint(devices[5])

# Printing devices in a table format

print("\n----- DEVICES IN TABULAR FORMAT -------------")
# Sorting the devices first
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
# Printing the sorted devices in a tabular format
print(tabulate(sorted_devices, headers="keys"))