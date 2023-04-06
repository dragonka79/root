from ncclient import manager
from router_info import router

config_template = open(
    "/home/zolcs/git/little_tasks/devasc/practice/NX-OS/ios_config_port.xml").read()

netconf_config = config_template.format(
    interface_name="GigabitEthernet2", if_value="true")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)
