# This is the Postman NX-API REST/NX-API REST_token and NX-API REST/NX-API REST SET_eth1/35 descr equivalent
# Getting the token first then modify interface eth1/35 desription

########################    1.Getting the token     #######################

from pprint import pprint
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = json.dumps({
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "Admin_1234!"
        }
    }
})
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'APIC-cookie=iSWc5SbdQyh8r8fcE6X8blY6yirZ/JcXAEgLVC8KwDdorPAlT7mathIGD2i9euknvXavwarFqcPhessR2uQAPMVpW2CtQlARf+XhlqBg94/Ia8n/+yJo+BChjyHZ2ZwJLNn/EeaMNM5pHA3qhyLkTHBEUjRz0GqGxxwDcRTBlwc='
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False).json()

# pprint(response)

token = response['imdata'][0]['aaaLogin']['attributes']['token']
print('\n', token, '\n')

# The token should be in a form of cookie
cookies = {}
cookies['APIC-cookie'] = token

############    2.Modify the description on interface eth1/35   ########


url = "https://sbx-nxos-mgmt.cisco.com:443/api/node/mo/sys/intf/phys-[eth1/35].json?"

payload = "{\n    \"l1PhysIf\": {\n        \"attributes\": {\n            \"descr\": \"dragonka was here by pys\",\n            }\n    }\n}"
headers = {
    'Content-Type': 'application/json',
}

put_response = requests.put(
    url, headers=headers, data=payload, cookies=cookies, verify=False).json()

pprint(put_response)
