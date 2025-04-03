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

##########  LOGIN WITH NX-API REST, JUMPING FROM NX-API CLI TO NX-API REST    ###############

auth_url = 'https://sandbox-nxos-1.cisco.com/api/mo/aaaLogin.json'
auth_body = {"aaaUser": {"attributes": {
    "name": switchuser, "pwd": switchpassword}}}

auth_response = requests.post(auth_url, data=json.dumps(
    auth_body), timeout=5, verify=False).json()
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
cookies = {}
cookies['APIC-cookie'] = token
print(cookies)
