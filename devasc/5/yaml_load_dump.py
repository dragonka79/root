import yaml

with open("/home/zolcs/Downloads/little_stuff/devasc/5/interfaces.yaml") as data:
    yaml_data = data.read()

# Convert YAML to python dict

yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

print(type(yaml_dict))
print(yaml_dict)

# Let us do some modifications

yaml_dict["interface"]["name"] = "GigabitEthernet3"  # Modification

# print(yaml_dict)

## Write the change to a new YAML file

with open("/home/zolcs/Downloads/little_stuff/devasc/5/interfaces_new.yaml", "w") as data_new:
    data_new.write(yaml.dump(yaml_dict, default_flow_style=False, sort_keys=False))

