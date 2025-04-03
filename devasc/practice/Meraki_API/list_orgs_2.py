### This is the expanded version of 'list_orgs_networks_devices_clients.py', extended with
###  writing out the outputs to files, too.

# # 1. From the code set in Postman under Meraki Dashboard API/list_organizations
# # + Same cosmetic upgrade for better readability
# # 2. + Getting a Id of an organization from the response -> Meraki Dashboard API/list_networks_by_orgid
# # 3. + Getting network on an organization -> Meraki Dashboard API/list_networks_by_orgid
# # 4. Obtain a list of devices in a given network -> Meraki Dashboard API/list_devices_in_a_network
# # 5. Obtain a list of clients in a given network

import json
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://api.meraki.com/api/v1/organizations"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

# # Save the response to a var and converting it to a python dict
response = requests.request("GET", url, headers=headers, data=payload).json()

# print(json.dumps(response, indent=2, sort_keys=True))

# # Writing out the sorted output to a json file:
# org_list = (json.dumps(response, indent=2, sort_keys=True))
# with open("./little_tasks/devasc/practice/Meraki_API/list_orgs.json", "w") as outfile:
#     outfile.write(org_list)
    
# 2. Getting and printing the id for 'DeLab' organization

for response_org in response:
    if response_org['name'] == 'DeLab':
        orgId = response_org['id']

print(orgId)


# 3. List of networks of the orgId

baseURI = "https://api.meraki.com/api/v1/"
org = "/organizations/"
orgId_str = str(orgId)
net = "/networks"

url2 = baseURI + org + orgId + net

response_network = requests.request(
    "GET", url2, headers=headers, data=payload).json()

# print(json.dumps(response_network, indent=2))

# # Writing out the list of the networks to a json file:
# network_list = (json.dumps(response_network, indent=2))
# with open("./little_tasks/devasc/practice/Meraki_API/list_networks.json", "w") as outfile:
#     outfile.write(network_list)


# 4. Obtain a list of devices in a given network

netname = 'DevNetLab'
for response_net in response_network:
    if response_net['name'] == netname:
        networkId = response_net['id']

org2 = "/networks/"
dev = "/devices"

url3 = baseURI + org2 + networkId + dev

response_devices = requests.request(
    "GET", url3, headers=headers, data=payload).json()

sep = '#' * 30
# print(f"\n{sep} Devices on {netname} network {sep}\n")
# print(json.dumps(response_devices, indent=2))

# # Writing out the list of the devices on the network to a json file:
# device_list = json.dumps(response_devices, indent=2)
# with open("./little_tasks/devasc/practice/Meraki_API/list_devices.json", "w") as outfile:
#     outfile.write(device_list)

# 5. Obtain a list of clients in a given network

clients = "/clients/"

url4 = baseURI + org2 + networkId + clients

response_clients = requests.request(
    "GET", url4, headers=headers, data=payload).json()

# print(f"\n{sep} Clients on {netname} network {sep}\n")
# print(json.dumps(response_clients, indent=2))
# print("\n")

# # Writing out the list of the clients on the network to a json file:
# client_list = json.dumps(response_clients, indent=2)
# with open("./little_tasks/devasc/practice/Meraki_API/list_clients.json", "w") as outfile:
#     outfile.write(client_list)