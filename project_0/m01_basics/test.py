# NOTE: this will disable insecure HTTPS request warnings that NAPALM gets
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import napalm

def connect_napalm(hostname, username, password, port, device_type):

    driver = napalm.get_network_driver(device_type)
    if device_type == "nxos":
        napalm_device = driver(
            hostname=hostname,
            username=username,
            password=password,
        )
    elif device_type == "ios" or device_type == "nxos_ssh":
        napalm_device = driver(
            hostname=hostname,
            username=username,
            password=password,
            optional_args={"port": port},
        )
    else:
        return None

    print(f"\n\n----- Connecting to {hostname}:{port}")
    napalm_device.open()
    print(f"----- Connected! --------------------")

    return napalm_device


def disconnect_napalm(connection):
    connection.close()
    print(f"----- Disconnected! --------------------")

############################

def get_facts_napalm(connection):

    return connection.get_facts()

########################################

class Device:
    def __init__(self, name, hostname, device_type, username, password, port):
        self.name = name
        self.hostname = hostname
        self.device_type = device_type
        self.username = username
        self.password = password
        self.port = port

    def connect(self):

        self.connection = connect_napalm(
            self.hostname, 
            self.username, 
            self.password, 
            self.port, 
            self.device_type
        )

        return True

    def get_facts(self):

        return get_facts_napalm(self.connection)

    def disconnect(self):

        disconnect_napalm(self.connection)

        return

##########################x

from pprint import pprint

def create_devices():
    created_devices = dict()

    created_devices["nxos-napalm"] = Device(
        name="nxos-napalm",
        hostname="sandbox-nxos-1.cisco.com",
        device_type="nxos",
        username="admin",
        password="Admin_1234!",
        port="22"
    )

    return created_devices

for _, device in create_devices().items():

    if not device.connect(): # If the connection is not successfull, then:
        print(f"----- Connection failed: {device.name}")
        break

    facts = device.get_facts()
    print(f"----- Facts for device: {device.name}")
    pprint(facts)

    device.disconnect()
