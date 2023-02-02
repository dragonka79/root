import json

# https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/
# https://www.geeksforgeeks.org/python-difference-between-json-dump-and-json-dumps/


with open("/home/zolcs/Downloads/little_stuff/devasc/5/gigabitethernet2.json", "r") as data:
    json_data = data.read()

print(json_data)
print(type(json_data))   # So I have now the JSON string

## Convert the JSON string to Python dictionary with loads

python_dict = json.loads(json_data)
print(python_dict)
print(type(python_dict))

## Change the ip from 172.16.0.2 to 172.16.0.4

python_dict["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"] = "172.16.0.4"
print(python_dict)

## Add a new key/value pair to the Python dictionary, under adress: "MAC" = "005e.efef.abcd"

python_dict["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["MAC"] = "005e.efef.abcd"
print(python_dict)
print(type(python_dict))

## Now write the 'python_dict' dictionary to a JSON file using JSON dump

with open("/home/zolcs/Downloads/little_stuff/devasc/5/gigabitethernet2_new.json", "w") as data_new:
    json.dump(python_dict, data_new, indent = 4)


## Parse aka convert the 'python_dict' python dictionary to a JSON string by dumps

json_string = json.dumps(python_dict, indent = 4)
print(json_string)
print(type(json_string))

