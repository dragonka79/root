import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

########## Login, getting the token ##############

url = "https://sandboxapicdc.cisco.com:443/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "name": "admin",
            "pwd": "!v3G@!4@Y"
        }
    }
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.request(
    "POST", url, headers=headers, data=json.dumps(payload), verify=False).json()

# print(json.dumps(response, indent=2))

####### Parse token and set cookie ############

token = response['imdata'][0]['aaaLogin']['attributes']['token']
cookie = {}
cookie['APIC-cookie'] = token

####### GET the Application Profile ###########

url = "https://sandboxapicdc.cisco.com:443/api/node/mo/uni/tn-PAWAN/ap-AP1.json"

headers = {
    'cache-control': 'no-cache'
}

get_response = requests.request(
    "GET", url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2))

########### Update the description of the AP above #############

post_payload = {
    "fvAp": {
        "attributes": {
            "descr": "dragonka was here",
            "dn": "uni/tn-PAWAN/ap-AP1"
        }
    }
}

post_response = requests.request(
    "POST", url, headers=headers, cookies=cookie, verify=False, data=json.dumps(post_payload)).json()

get_response = requests.request(
    "GET", url, headers=headers, cookies=cookie, verify=False).json()

print(json.dumps(get_response, indent=2))
