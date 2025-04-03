from l_03_functions import create_devices
from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap

devices = create_devices(10) # = num_devices=10, num_subnets=1 (default value)

print("\n\nUSING PRINT\n")
print(devices)

print("\n\nUSING PPRINT\n")
pprint(devices)

print("\n\nUSING LOOP\n")
for device in devices:
    sleep(0.1)  # Waiting 0.1 sec for the execution
    device["last_heard"] = str(datetime.now())
    print(device)

print("\n\nUSING TABULATE\n")
print(
    tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys") # Sorted by vendor first, then os then version
)

print("\n\nUSING LOOP AND F-STRING\n")
print("   NAME      VENDOR : OS      IP ADDRESS       LAST HEARD")
print("  -----     -------   -----   --------------   ----------------------")
for device in devices:
    print(
        f'{device["name"]:>7}  '
        f'{device["vendor"]:>10} : '
        f'{device["os"]:<6}  '
        f'{device["ip"]:<15}  '
        f'{device["last_heard"][:-4]}'
    )

print("\nSame thing, but sorted descending by last_heard\n")
for device in sorted(devices, key=itemgetter("last_heard"), reverse=True):
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["last_heard"][:-4]}'
    )

print("\n\nMULTIPLE PRINT STATEMENTS, SAME LINE\n")
print("Testing Devices:")
for device in devices:
    print(f"--- testing device {device['name']} ... ", end="")
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print("done.")
print("Testing completed")

nm = nmap.PortScanner()
while True:

    ip = input("\nInput IP address to scan: ")
    if not ip: # if the ip = empty, meaning hitting enter
        break

    print(f"\n--- beginning scan of {ip}")
    output = nm.scan(ip, '22-1024')
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output -------------------")
    pprint(output)

