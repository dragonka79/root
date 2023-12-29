import requests
import json

switchuser = 'admin'
switchpassword = 'Admin_1234!'

url = 'https://sandbox-nxos-1.cisco.com/ins'
myheader = {'content-type': 'application/json'}
payload = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "sid",
        "input": "sh cdp neigh",
        "output_format": "json"
    }
}

response = requests.post(url, data=json.dumps(payload), headers=myheader, auth=(
    switchuser, switchpassword), verify=False).json()

print(response)
