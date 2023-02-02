
## Open and close files in a classic way: open, read and close

# readdata = open("/home/zolcs/Downloads/little_stuff/devasc/text1.txt", "r")
# print(readdata.read())
# readdata.close()

## Open and close files in an advanced way: open, read and make it closed auto.

# with open("/home/zolcs/Downloads/little_stuff/devasc/text1.txt", "r") as readdata:
#     print(readdata.read())

## Append a line to the end of the file and then read it

with open("/home/zolcs/Downloads/little_stuff/devasc/text1.txt", "a") as data:
    data.write("\nNew line is appended")

with open("/home/zolcs/Downloads/little_stuff/devasc/text1.txt", "r") as data:
    print(data.read())



