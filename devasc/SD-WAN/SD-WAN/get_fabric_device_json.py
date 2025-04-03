import requests
import json
import auth_base

""" Getting basic information on devices in the fabric """

url = auth_base.base_url + '/device'
response = requests.request("GET", url, headers=auth_base.header, data=auth_base.payload, verify=False)
device_response = response.json()['data']
json_dumps = json.dumps(device_response, indent=4)
with open('output_get_device_json.txt', 'w') as f:
    f.write(json_dumps)

