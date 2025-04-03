# Dict methods

hun2esp = {"egy": "uno", "kettő": "dos", "három": "tres"}

for k in hun2esp.keys():
    print("A(z)", k, "kulcs leképezi a(z)", hun2esp[k], "értéket.")

ks = list(hun2esp.keys())   # Gives back the list of the keys
vs = list(hun2esp.values()) # Gives back the list of the values
ns = list(hun2esp.items())  # Gives back the n-list of the key:value pairs

print(ks)
print(vs)
print(ns)

# Checking whether a key is in the dict

print("egy" in hun2esp.keys())  
print("egy" in hun2esp)   # The same as #16

print("hat" in hun2esp)

###

h = "háron"
if h in hun2esp.keys():
    print(hun2esp[h])
else:
    print("Such key does not exist")

