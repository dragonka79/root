# This is the NX-API_GET equivalent
# Getting some show commands from NX-API Cisco sandbox


import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

target = "https://sbx-nxos-mgmt.cisco.com:443/ins"
username = 'admin'
password = 'Admin_1234!'

requestheaders = {'content-type': 'application/json'}
showcmd = {
    "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "sid",
        "input": "show version ;show ip int br ;show int status",
        "output_format": "json"
    }
}
response = requests.post(      # Not a REST API, therefore everything should be POST-ed
    target,
    data=json.dumps(showcmd),
    headers=requestheaders,
    auth=(username, password),
    verify=False,
).json()

print(json.dumps(response, indent=2, sort_keys=True))
