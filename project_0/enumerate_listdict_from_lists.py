# Create a dictionary from two lists: using one as a "key" and the 
# second one as "values"

from pprint import pprint
from tabulate import tabulate

d0 = ["hostname", "vendor", "IP"]
d1 = [
      ["c1c1", "cisco", "192.168.1.1"],
      ["j2j2", "juniper", "172.16.1.1"],
      ["f3f3", "fortigate", "10.1.1.1"]
     ]
devices_list = list()
for device_index in range(len(d1)):
    device_dict = dict()
    for index, header in enumerate(d0):
        device_dict[header] = d1[device_index][index]
    devices_list.append(device_dict)
print('------    pretty print of the devices ----------\n')
pprint(devices_list, sort_dicts=False)
print('\n')
print('------    print of the devices in a tabulate format   ----------')
print('\n', tabulate(devices_list, headers="keys"))
