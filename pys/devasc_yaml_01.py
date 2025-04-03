import yaml

with open("yaml_sample.yaml") as data:
    yaml_sample = data.read()
yaml_dict = yaml.load(yaml_sample)
print(yaml_dict)

# 2.1 itt megváltoztatjuk az interface nevét a python szótárban és
#kinyomtatjuk
yaml_dict["interface"]["name"] = "GigabitEthernet1"
print(yaml.dump(yaml_dict))

#2.2 Itt visszaírjuk az interface új nevét az eredeti yaml file-ba
with open("yaml_sample.yaml", "w") as data:
    data.write(yaml.dump(yaml_dict))
#nézzük meg az eredeti yaml file-t, az interface régi nevét kitörölte fenntről és
# berakta alulra
