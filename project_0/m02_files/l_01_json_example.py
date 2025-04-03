from l_00_inventory import inventory
import json

# CONVERT INVENTORY TO JSON AND WRITE TO FILE
# Convert from python to json: dumps() (dump + string)
with open("l_00_inventory.json", "w") as json_out:
    json_out.write(json.dumps(inventory, indent=4))

# READ JSON INVENTORY FROM FILE
with open("l_00_inventory.json", "r") as json_in:
    json_inventory = json_in.read()
    print(json_inventory)

# CONVERT JSON INVENTORY TO PYTHON, THEN CONVERT BACK TO STRING FOR PRINTING
# Convert from json to python: loads (load + string)
print("\njson pretty version:")
print(json.dumps(json.loads(json_inventory), indent=4))

# COMPARE INVENTORY WE READ, WITH ORIGINAL INVENTORY, TO MAKE SURE THEY ARE EQUIVALENT
print("\n----- compare saved inventory with original --------------------")
saved_inventory = json.loads(json_inventory)
if saved_inventory == inventory:
    print("-- worked: saved inventory equals original")
else:
    print("-- failed: saved inventory different from original")