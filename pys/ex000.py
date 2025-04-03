import json
with open("json_native_sample.json") as data:
    json_data = data.read()
json_dict = json.loads(json_data)
print(json_dict)
