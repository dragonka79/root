# 1. From the code set in Postman under Meraki Dashboard API/list_organizations
# + Same cosmetic upgrade for better readability
# 2. + Getting a Id of an organization from the response -> Meraki Dashboard API/list_networks_by_orgid
# 3. + Getting network on an organization -> Meraki Dashboard API/list_networks_by_orgid
# 4. Obtain a list of devices in a given network -> Meraki Dashboard API/list_devices_in_a_network

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.meraki.com/api/v1/organizations"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

# Save the response to a var and converting it to a python dict
response = requests.request("GET", url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2, sort_keys=True))

# 2. Getting and printing the id for 'DeLab' organization

for response_org in response:
    if response_org['name'] == 'DeLab':
        orgId = response_org['id']

# print(orgId)

# 3. List of networks of the orgId

baseURI = "https://api.meraki.com/api/v1/"
org = "/organizations/"
orgId_str = str(orgId)
net = "/networks"

url2 = baseURI + org + orgId + net

response_network = requests.request(
    "GET", url2, headers=headers, data=payload).json()

# print(json.dumps(response_network, indent=2))

# 4. Obtain a list of devices in a given network

for response_net in response_network:
    if response_net['name'] == 'DevNetLab':
        networkId = response_net['id']


url = "https://api.meraki.com/api/v1/networks/L_783626335162466320/devices"

org2 = "/networks/"
dev = "/devices"

url3 = baseURI + org2 + networkId + dev

response_devices = requests.request(
    "GET", url3, headers=headers, data=payload).json()

print(json.dumps(response_devices, indent=2))
