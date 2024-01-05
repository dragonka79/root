import requests
import auth_base
import json
from texttable import Texttable


def feature_template_list():
    
    """
       Retrieves all the feature templates:
       #1: Unfiltered list in json format
       #2: Filtered list in a table format
    """
    
    url = auth_base.base_url + '/template/feature'
    response = requests.request("GET", url, headers=auth_base.header, data=auth_base.payload, verify=False)
    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of feature templates " + str(response.text))
        exit()

  ##1: Unfiltered list in json format
    
    # device_response = response.json()['data']
    # json_dumps = json.dumps(device_response, indent=4)
    # with open('output_get_feature_template_json.txt', 'w') as f:
    #     f.write(json_dumps)
    # return(json_dumps)
    
    ##2: Filtered list in a table format
    
    headers = ["templateId", "templateName", "templateDescription", "templateType", "deviceType", "devicesAttached"]
    t = Texttable(max_width=240)
    t.header(headers)
    
    for item in items:
        tr = [item['templateId'], item['templateName'], item['templateDescription'], item['templateType'], item['deviceType'], item['devicesAttached']]
        t.add_row(tr)
    return(t.draw())    


with open('output_get_feature_template_table.txt', 'w') as f:
    f.write(feature_template_list())

feature_template_list()