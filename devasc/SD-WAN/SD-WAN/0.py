import requests
import auth_base
from texttable import Texttable

def device_list():
    """Retrieve and return network devices list.
       Returns information about each device that is part of the fabric.
    """
    url = auth_base.base_url + '/device'
    response = requests.request("GET", url, headers=auth_base.header, data=auth_base.payload, verify=False)

    if response.status_code == 200:
        items = response.json()['data']
    else:
        print("Failed to get list of devices " + str(response.text))
        exit()
 
    headers = ["Host-Name", "Device Type", "Device ID", "System IP", "Site ID", "Version", "Device Model", "State", "Uptime                   "]
    t = Texttable(max_width=140)
    t.header(headers)
    l = list()
    for i in items:
        l.append(float(i['uptime-date'])) 
    for i in range(len(l)):    
        for item in items:
            tr = [item['host-name'], item['device-type'], item['uuid'], item['system-ip'], item['site-id'], item['version'], item['device-model'], item['state'], l[i]]
            t.add_row(tr)
        return(t.draw())



# print(device_list())

with open('output_get_device_table.txt', 'w') as f:
    f.write(device_list())
