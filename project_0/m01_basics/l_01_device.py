from pprint import pprint

#Dictionary representing a device

device = {
    "name": "quokka_nx_os",
    "vendor": "cisco",
    "model": "CSR1000V (VXE)",
    "os": "Cisco IOS XE ",
    "version": "16.07.01",
    "ip": "192.168.95.133",
}

# Simple print

print("\n__________ SIMPLE PRINT __________________\n")
print("device:", device)
print("device name:", device["name"])

# Pretty print

print("\n__________ PRETTY PRINT __________________\n")

pprint(device, sort_dicts=False)

# For loop, nicely formatted print

print("\n__________ FOR LOOP, USING F-STRING __________________\n")
    #Create a list of iterable items (key, value pairs) of the dictionary 
for (key, value) in device.items():
    print(f"{key:>16s} : {value}")