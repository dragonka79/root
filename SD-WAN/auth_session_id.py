import logging
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)  # Set the logging level

class Authentication:

    @staticmethod
    def get_jsessionid(vmanage_host, vmanage_port, username, password):
        api = "/j_security_check"
        base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
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

result = Authentication.get_jsessionid('10.10.20.90', '443', 'admin', 'C1sco12345')
if result:
    print("JSESSION ID:", result)
else:
    print("Failed to retrieve JSESSION ID")



# # Original code by Cisco (wrong)
    
# class Authentication:
# ​
#     @staticmethodclass
#     def get_jsessionid(vmanage_host, vmanage_port, username, password):
#         api = "/j_security_check"
#         base_url = "https://%s:%s"%(vmanage_host, vmanage_port)
#         url = base_url + api
#         payload = {'j_username' : username, 'j_password' : password}
        
#         response = requests.post(url=url, data=payload, verify=False)
#         try:
#             cookies = response.headers["Set-Cookie"]
#             jsessionid = cookies.split(";")
#             return(jsessionid[0])
#         except:
#             if logger is not None:
#                 logger.error("No valid JSESSION ID returned\n")
#             exit()

