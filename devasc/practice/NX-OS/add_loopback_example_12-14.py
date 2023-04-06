#!/usr/bin/env python
""" Add a loopback interface to a device with NETCONF """

# Does not work

from ncclient import manager

NXOS_HOST = "131.226.217.151"  # sbx-nxos-mgmt.cisco.com
NETCONF_PORT = "830"
USERNAME = "admin"
PASSWORD = "Admin_1234!"
LOOPBACK_ID = "87"
LOOPBACK_IP = "1.1.1.1/32"

# create add_loopback() method


def add_loopback():
    """
    Method that adds loopback interface and configures IP address
    """

    add_loop_interface = """<config>
    <System xmlns=”http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
            <lb-items>
                <LbRtdIf-list>
                    <id>lo{id}</id>
                    <adminSt>up</adminSt>
                    <descr>Intf configured via NETCONF</descr>
                </LbRtdIf-list>
            </lb-items>
        </intf-items>
        <ipv4-items>
            <inst-items>
                <dom-items>
                    <Dom-list>
                        <name>default</name>
                        <if-items>
                            <If-list>
                                <id>lo{id}</id>
                                <addr-items>
                                    <Addr-list>
                                        <addr>{ip}</addr>
                                    </Addr-list>
                                </addr-items>
                            </If-list>
                        </if-items>
                    </Dom-list>
                </dom-items>
            </inst-items>
        </ipv4-items>
    </System>
    </config>""".format(id=LOOPBACK_ID, ip=LOOPBACK_IP)

    with manager.connect(
        host=NXOS_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False
    ) as device:

        # Add loopback interface
        print("\n Adding Loopback {} with IP address {} to device {}...\n".
              format(LOOPBACK_ID, LOOPBACK_IP, NXOS_HOST))
        netconf_response = device.edit_config(target='running',
                                              config=add_loop_interface)
        # Print the XML response
        print(netconf_response)


if __name__ == '__main__':
    add_loopback()
