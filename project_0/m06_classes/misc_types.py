class TransportType:
    NAPALM = "napalm"
    NCCLIENT = "ncclient"
    NETMIKO = "netmiko"


class DeviceType:
    IOS = "ios"
    NXOS = "nxos"
    NXOS_SSH = "nxos_ssh" # Only for NAPALM
    NEXUS = "nexus"
    CISCO_NXOS = "cisco_nxos"