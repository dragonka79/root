keszlet = {"alma": 430, "banán": 312, "narancs": 525, "körte": 217}
print(keszlet)

# del(keszlet["körte"])  # Remove key:value pair
# keszlet["körte"] = 0   # Modify a value to a certain value
keszlet["banán"] += 200  # Change a value
print(keszlet)

print(len(keszlet))      # The number of key:value pairs