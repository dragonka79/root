import requests
import json

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback1"

payload = {}
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ=='
}

response = requests.request(
    "GET", url, headers=headers, data=payload, verify=False)

print(response.text)
