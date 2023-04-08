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
    'Content-Type': 'application/json',
    # 'Cookie': 'APIC-cookie=eyJhbGciOiJSUzI1NiIsImtpZCI6Imc0ZHZ4eTA1emtqNmZhZnoxZjI5MHlkcnozYnUyYjAzIiwidHlwIjoiand0In0.eyJyYmFjIjpbeyJkb21haW4iOiJhbGwiLCJyb2xlc1IiOjAsInJvbGVzVyI6MX1dLCJpc3MiOiJBQ0kgQVBJQyIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyaWQiOjE1Mzc0LCJ1c2VyZmxhZ3MiOjAsImlhdCI6MTY4MDk2OTQ3MCwiZXhwIjoxNjgwOTcwMDcwLCJzZXNzaW9uaWQiOiIzMkppT29qZ1IrMkJYNXY4QXJ2eUZ3PT0ifQ.f-ljjQg1mrUoLW2CcgSjaUUFVeMOe2v-SyL7kZjJmknUhFwjxN76VoifJddLYe6vBr96Q6velISJT20yyDN47Kpx2qZawZkrzvtfQrFxfJ39Lt2V9wF59yPA2kRZfFlsMDhwWkWNsLXktJ6GiWwspuHgukw6OngVf9psaKt9jkFUZmcJMJr85qOW4zsQIs95v1O0JSaRWFhJr-cZr5O9E3m4iiUhpsF0ZLaAt2-_8hy8pDg2eocXa3rv9QZXHWmAnzroagz3rfcXfw3z4i0pyY0PJ-nckbEIiVLgYKGWeovzg_6JKDUgt-OyBPYY1kiR2hh76K102OaLZVs2F1qpew'
}

response = requests.request(
    "POST", url, headers=headers, data=json.dumps(payload), verify=False).json()

print(json.dumps(response, indent=2))
