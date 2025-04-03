from ncclient import manager
# import logging
# logging.basicConfig(level=logging.DEBUG)

router = {"host": "sandbox-iosxe-recomm-1.cisco.com", "port": "830",
          "username": "developer", "password": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
