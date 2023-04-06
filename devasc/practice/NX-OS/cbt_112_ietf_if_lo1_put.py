from pprint import pprint
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

payload = json.dumps({
    "ietf-interfaces:interface": [
        {
            "name": "Loopback1",
            "type": "iana-if-type:softwareLoopback",
            "description": "dragonka was here",
            "ietf-ip:ipv4": {},
            "ietf-ip:ipv6": {}
        }
    ]
})
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ=='
}

response = requests.request(
    "PUT", url, headers=headers, data=payload, verify=False)
print(response)
