# From the code set in Postman under Meraki Dashboard API/list_organizations
# + Same cosmetic upgrade for better readability
# + Getting a Id of an organization from the response

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

print(json.dumps(response, indent=2, sort_keys=True))

# 2. Getting and printing the id for 'DeLab' organization

for response_org in response:
    if response_org['name'] == 'DeLab':
        orgId = response_org['id']

print(orgId)
