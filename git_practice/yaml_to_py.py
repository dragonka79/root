import yaml

with open("/home/zolcs/git/little_tasks/git_practice/example.yaml") as data:
    yaml_data = data.read()

# Convert YAML to python dict

yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

print(type(yaml_dict))
print(yaml_dict)
print(yaml_dict['addresses'][1])  # Print the second element in yaml list
print(yaml_dict['addresses'][2]['netmask'])  # Print 'netmask' value of the third element in the list

# Let us do some modifications

yaml_dict["addresses"][2]['Id'] = 4

# print(yaml_dict)

## Write the change to a new YAML file

with open("/home/zolcs/git/little_tasks/git_practice/example.yaml", "w") as data_new:
    data_new.write(yaml.dump(yaml_dict, default_flow_style=False, sort_keys=False))

