## 1.1 Parsing csv file to python and read it

import csv

datacsv = open("/home/zolcs/Downloads/little_stuff/devasc/5/routerlist.csv")
datacsvreader = csv.reader(datacsv)
csvpy = list(datacsvreader)
datacsv.close()

# print(f"\n{csvpy}\n")

## 1.2 Displaying csv in a more user friendly manner

with open("/home/zolcs/Downloads/little_stuff/devasc/5/routerlist.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        ip = row[1]
        location = row[2]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")
    print("\t")

## The rstrip() method removes any characters at the end a string,
## space is the default trailing character to remove.

## 2.1 Write a new entry to the csv file and then read the whole file

print("Please add a new router to the list")
newhostname = input("What is the hostname? ")
newip = input("What is the ip address? ")
newlocation = input("What is the location? ")

newrouter = [ newhostname, newip, newlocation ]

with open("/home/zolcs/Downloads/little_stuff/devasc/5/routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(newrouter)

with open("/home/zolcs/Downloads/little_stuff/devasc/5/routerlist.csv") as data:
    csv_list = csv.reader(data)
    for row in csv_list:
        device = row[0]
        ip = row[1]
        location = row[2]
        print(f"{device} is in {location.rstrip()} and has IP {ip}.")
    print("\t")




