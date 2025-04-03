#! /usr/bin/env python
# A köv 3 sorban beimportálom a dnacentersdk útját
import sys
sys.path.append(r'/home/zolcs/.local/lib/python2.7/site-packages')
sys.path

from dnacentersdk import api
# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password
DNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!",
base_url="https://sandboxdnac2.cisco.com")
# Find all devices
DEVICES = DNAC.devices.get_device_list()
# Print select information about the retrieved devices
print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name", "|", \
"Device Type", "|", "Up Time"))
print('-'*95)
for DEVICE in DEVICES.response:
    #Ide kell az if mert van pár 'None' eszköz és azok kivételek
    if str(DEVICE.hostname) != 'None':
        print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, \
        "|", DEVICE.type, "|", DEVICE.upTime))
print('-'*95)
# Get the health of all clients on Thursday, August 22, 2019 8:41:29 PM GMT
CLIENTS = DNAC.clients.get_overall_client_health(timestamp="1631291287000")
# Print select information about the retrieved client health statistics
print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Client Category", "|",\
"Number of Clients", "|", "Clients Score"))
print('-'*95)
for CLIENT in CLIENTS.response:
    for score in CLIENT.scoreDetail:
        print('{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}'.format
        (score.scoreCategory.value, "|", score.clientCount, "|", \
        score.scoreValue))
print('-'*95)
