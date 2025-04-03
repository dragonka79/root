#! /usr/bin/env python
import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Specify Cisco vManage IP, username and password
VMANAGE_IP = 'sandbox-sdwan-1.cisco.com'
USERNAME = 'devnetuser'
PASSWORD = 'Cisco123!'

BASE_URL_STR ='https://{}/'.format(VMANAGE_IP)

# Login API resource and login credentials
LOGIN_ACTION = 'j_security_check'
LOGIN_DATA = {'j_username' : USERNAME, 'j_password' : PASSWORD}
# URL for posting login data
LOGIN_URL = BASE_URL_STR + LOGIN_ACTION

# Establish a new session and connect to Cisco vManage
SESS = requests.session()
LOGIN_RESPONSE = SESS.post(url=LOGIN_URL, data=LOGIN_DATA, verify=False)

# Get list of devices that are part of the fabric and display them
DEVICE_RESOURCE = 'dataservice/device'
# URL for device API resource
DEVICE_URL = BASE_URL_STR + DEVICE_RESOURCE

DEVICE_RESPONSE = SESS.get(DEVICE_URL, verify=False)
DEVICE_ITEMS = json.loads(DEVICE_RESPONSE.content)['data']
