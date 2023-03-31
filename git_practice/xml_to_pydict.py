import xmltodict

## Convert XML file to a Python (ordered)dictionary

with open("/home/zolcs/git/little_tasks/git_practice/example.xml") as data:
    xml_file = data.read()

# print(type(xml_file))

xml_dict = xmltodict.parse(xml_file) # Convert from XML to Python dict


# print(type(xml_dict))
print("\n")
print(xml_dict)
print("\n")

