#!/usr/bin/env python
""" Get the capabilities of a remote device with NETCONF """

from ncclient import manager

# https://devnetsandbox.cisco.com/RM/Diagram/Index/27d9747a-db48-4565-8d44-df318fce37ad?diagramType=Topology
NXOS_HOST = "131.226.217.149"
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
