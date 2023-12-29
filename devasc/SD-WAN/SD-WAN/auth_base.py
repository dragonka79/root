import logging
import requests
import urllib3
import credentials

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Set the logging level


class Authentication:

    @staticmethod
    def get_jsessionid(vmanage_host, vmanage_port, username, password):
        api = "/j_security_check"
        # base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
        base_url = "https://{0}:{1}".format(vmanage_host, vmanage_port)
        url = base_url + api
        payload = {'j_username' : username, 'j_password' : password}      
        response = requests.post(url=url, data=payload, verify=False)
        try:
            cookies = response.headers["Set-Cookie"]
            jsessionid = cookies.split(";")
            return(jsessionid[0])
        except:
            if logger is not None:
                logger.error("No valid JSESSION ID returned\n")
            exit()
       
    @staticmethod
    def get_token(vmanage_host, vmanage_port, jsessionid):
        headers = {'Cookie': jsessionid}
        # base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
        base_url = "https://{0}:{1}".format(vmanage_host, vmanage_port)
        api = "/dataservice/client/token"
        url = base_url + api      
        response = requests.get(url=url, headers=headers, verify=False)
        if response.status_code == 200:
            return(response.text)
        else:
            return None

Auth = Authentication()
jsessionid = Auth.get_jsessionid(credentials.vmanage_host,credentials.vmanage_port,credentials.vmanage_username,credentials.vmanage_password)
token = Auth.get_token(credentials.vmanage_host,credentials.vmanage_port,jsessionid)
payload = {}
# base_url = "https://%s:%s/dataservice"%(credentials.vmanage_host, credentials.vmanage_port)
base_url = "https://{0}:{1}/dataservice".format(credentials.vmanage_host, credentials.vmanage_port)

if token is not None:
    header = {'Content-Type': "application/json",'Cookie': jsessionid, 'X-XSRF-TOKEN': token}
else:
    header = {'Content-Type': "application/json",'Cookie': jsessionid}