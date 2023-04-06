# This is the Postman NX-API/NX-API_GET equivalent
# Getting some show commands from NX-API Cisco sandbox

import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com:443/ins"

payload = json.dumps({
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "sid",
        "input": "show version ;show ip int br ;show int status",
        "output_format": "json"
    }
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
    'Cookie': 'nxapi_auth=dzqnf:VjCNmVhRFUDkLkNvDo2/UfGvBnw='
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False)

print(response.text)
