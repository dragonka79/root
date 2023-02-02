## 1.1 Parsing csv file to python and read it

import csv

datacsv = open("/home/zolcs/Downloads/little_stuff/devasc/5/routerlist.csv")
datacsvreader = csv.reader(datacsv)
csvpy = list(datacsvreader)
datacsv.close()

print(f"\n{csvpy}\n")

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

