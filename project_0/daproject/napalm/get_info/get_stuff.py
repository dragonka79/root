# https://napalm.readthedocs.io/en/latest/support/

import napalm
import json
import copy
from devices import sandbox_devices
from pprint import pprint
import urllib3

# this will disable insecure HTTPS request warning messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


NS = " This cannot be retrieved, might be not supported for"

def ns():
    return print(f"{NS} {device['hostname']}:{device['port']}, error: {e}\n")

devices_copy = copy.deepcopy(sandbox_devices)  # a save copy only

pprint(devices_copy, sort_dicts=False)

for os, device in devices_copy.items():

    print(f"\n +++ connecting to device {os}: {device['hostname']} +++")
    driver = napalm.get_network_driver(os)
    napalm_device = driver(
        hostname=device["hostname"],
        username=device["username"],
        password=device["password"],
        optional_args={"port": device["port"]},
        )

    napalm_device.open()

    print("\n    +++ Is the connection established?... +++")
    print(json.dumps(napalm_device.is_alive(), 
            sort_keys=True, indent=4))

    print("\n    +++ Gathering facts... +++")
    print(json.dumps(napalm_device.get_facts(), 
            sort_keys=True, indent=4))

    print("\n    +++ Gathering interface informations... +++")
    print(json.dumps(napalm_device.get_interfaces(), 
            sort_keys=True, indent=4))

    print("\n    +++ Gathering vlan informations... +++")
    try: 
        print(json.dumps(napalm_device.get_vlans(), 
            sort_keys=True, indent=4))
    except NotImplementedError as e:
        ns()

    print("\n    +++ Gathering snmp informations... +++")
    print(json.dumps(napalm_device.get_snmp_information(), 
            sort_keys=True, indent=4))

    print("\n    +++ Gathering interface counters... +++\n")
    try:
        print(json.dumps(napalm_device.get_interfaces_counters(), 
            sort_keys=True, indent=4))
    except Exception as e:
        ns()

    print("\n    +++ Gathering environment informations... +++\n")
    try:
        print(json.dumps(napalm_device.get_environment(), 
            sort_keys=True, indent=4))
    except Exception as e:
        ns()
    
    print("\n    +++ Gathering users... +++")
    print(json.dumps(napalm_device.get_users(), 
            sort_keys=True, indent=4))
      
    print("\n    +++ Gathering NTP servers... +++")
    print(json.dumps(napalm_device.get_ntp_servers(), 
            sort_keys=True, indent=4))

#    Should be fixed, the format of the output is not correct 
    print("\n    +++ Getting the running configuration... +++")
    print(json.dumps(napalm_device.get_config(), sort_keys=True, indent=4))


    napalm_device.close()