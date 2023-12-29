s1 = "name: zoli, age: 42"
dict_s1 = {item.split(":")[0].strip(): item.split(":")[1].strip() for item in s1.split(",")}
print(dict_s1)

