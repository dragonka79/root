import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set URL and login body
# Note the body is a python dict - NOT a JSON body
base_url = 'https://10.10.20.90:8443/'
api = 'j_security_check'
login_body = {
    'j_username': 'admin',
    'j_password': 'C1sco12345'
}

login_url = base_url + api
url = base_url + 'dataservice/device'
# MUST use a session for SD-WAN
session = requests.session()
response = session.post(login_url, data=login_body, verify=False)

# Response returns a 200 OK no matter what
# IF the response body contains any text then auth failed
if not response.ok or response.text:
    print('login failure')
    import sys
    sys.exit(1)
else:
    print('login worked!')

