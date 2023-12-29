# 52 lapos francia kártyát kérek le, ennek van egyedi azonosítja (deck_id)

import requests

# A url0-val lekérek egy új pakli kártyát
url0 = "https://deckofcardsapi.com/api/deck/new/"

# A url1-gyel lekérek a (megmaradt) pakliból 3 kártyát
# url1 = "https://deckofcardsapi.com/api/deck/tepwdcgiivgl/draw/?count=3"

payload = {}
headers = {}

response = requests.request("GET", url0, headers=headers, data=payload)

print(response.text)
