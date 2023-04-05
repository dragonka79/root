import requests
import json
from pprint import pprint

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=Loopback10"

payload = {}
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ=='
}

response = requests.request(
    "GET", url, headers=headers, data=payload, verify=False)
api_data = response.json()
pprint(api_data)
