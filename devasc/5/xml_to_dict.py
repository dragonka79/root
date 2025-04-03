import xmltodict

## Convert XML file to a Python (ordered)dictionary

with open("/home/zolcs/Downloads/little_stuff/devasc/5/gigabit.xml") as data:
    xml_file = data.read()

print(type(xml_file))

xml_dict = xmltodict.parse(xml_file) # Convert from XML to Python dict


print(type(xml_dict))
print(xml_dict)
print("\n")

## Modify the ip address to 172.16.0.3 and add MAC=005e.efef.abcd

xml_dict["interface"]["ipv4"]["address"]["ip"] = "172.16.0.3"
xml_dict["interface"]["ipv4"]["address"]["MAC"] = "005e.efef.abcd"

print(xmltodict.unparse(xml_dict, pretty=True)) # How it looks like as XML

## Write the modified python dict to XML file

with open("/home/zolcs/Downloads/little_stuff/devasc/5/gigabit_new.xml", "w") as data_new:
    data_new.write(xmltodict.unparse(xml_dict, pretty=True))
