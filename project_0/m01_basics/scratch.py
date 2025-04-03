names = [ "zaultschy", "zolcs", "zolcsi" ]

# i = 0
# for name in range(len(names)):
#     print("my name is", names[i])
#     i +=1

# for name in names:
#     print("the current name is", name)

    ## List with two intems, which are dictionaries of three items 

persons = [{"name": "david", "location": "UK", "handsome": True, "intelligent": "maybe"},
           {"name": "chuck", "location": "UK", "California": False, "intelligent": "the jury is still out"}]

for person in persons:
    print("\n")
    print(f"the current person is {person}")


