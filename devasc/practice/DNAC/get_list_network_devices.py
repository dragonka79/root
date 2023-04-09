import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

###### Getting the token  ########
# it does not work, the token is different to the one got by Postman

url_token = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

user = 'devnetuser'
password = 'Cisco123!'

response_token = requests.post(
    url_token, auth=(user, password), verify=False).json()
token = response_token['Token']
print(token)


url_dev = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload = {}
headers = {
    'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MjQxOTIzZTU3MjU5NTA2YTU2YjRhYTEiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYyM2YwMjlhNTcyNTk1MDZhNTZhZDljNCJdLCJ0ZW5hbnRJZCI6IjYyM2YwMjk4NTcyNTk1MDZhNTZhZDliZCIsImV4cCI6MTY4MTA0NTQ4MSwiaWF0IjoxNjgxMDQxODgxLCJqdGkiOiJmZTBkZTdmNS0zOWQyLTQ4MGYtODhjOS01YzU0ZjI5ZDcwMjEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.a9tRr5WgVrJI3dycAyIFbUWB0cDdIT6wlJuPGgC7FsV-cb1Bfg4A9AYc7ab-QCv3TeFfl0WBGcbuftMxI1lTDVGxWapLAIIciE0je_ABuvL6wUJGXHXyHnlQhWvL9mVNGE7TNIIktNDv8Q8dSIcGOzmCpp7NDdGhQcIfyaw_K9-NAdLj7-jDwsDXqBV9bSHdznf1d-f4tyvCBuLVdYgHoJzbM92ydp_d47BImHeZCMHOBi84CwzQGlE1HoLGZnCHSPdBUS1PXstkxK0MjczDyFQK7zEB4VnljB8z77RzPx4kpZh3x86RKDfk2I_SMw3Nq1EBlfB46F-sLd_UVuSJlw',
    # 'X-Auth_Token': token,
    'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response_dev = requests.request(
    "GET", url_dev, headers=headers, data=payload, verify=False).json()

print(json.dumps(response_dev, indent=2, sort_keys=True))
