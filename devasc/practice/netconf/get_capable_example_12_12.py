#!/usr/bin/env python
""" Get the capabilities of a remote device with NETCONF """

from ncclient import manager

NXOS_HOST = "131.226.217.149"   # sandbox-iosxe-recomm-1.cisco.com
NETCONF_PORT = "830"
USERNAME = "developer"
PASSWORD = "lastorangerestoreball8876"
# create a get_capabilities() method


def get_capabilities():
    """
    Method that prints NETCONF capabilities of remote device.
    """
    with manager.connect(
        host=NXOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:

        # print all NETCONF capabilities
        print('\n***NETCONF Capabilities for device {}***\n'.format(NXOS_HOST))
        for capability in device.server_capabilities:
            print(capability)


if __name__ == '__main__':
    get_capabilities()
