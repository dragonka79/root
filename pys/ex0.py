""" Generate Base64 encoding using the base64library """
import base64
encoded = base64.b64encode('devasc:strongpassword'.encode('UTF-8')).decode('ASCII')
print(encoded)
