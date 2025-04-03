from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print(f"If you don't want that, hit ctrl-c (^C).")
print(f"If you do want that, RETURN.")

input("?")

print("Opening the file...")

###Megnyitom a file-t írásra és lementem egy változóba.
###w" - Write - Opens a file for writing, creates the file if it does not exist
target = open(filename, 'w')

print("Truncating the file. Goodbye!")

###Letörlöm a file tartalmát úgy, hogy 0 méretűvé teszem,
### a () közé nem rakok számot, üres file-t hagyok hátra.
###Ez nem kötelező, mert 'w'-vel nyitottam meg a file-t és a file
###felülíródik
target.truncate()

print("Now I am going to ask you for three lines.")

###Bekérek 3 sort a usertől kézi inputra és azokat egyesével változókba teszem
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going to write these to the file.")

###Beíratom a bekért sorokat a változókból a file-ba, közéjük új sort török
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(f"""
{line1}
{line2}
{line3}
""")

print("And finally, we close it.")

###Lezárom a file-t, azaz mentem és kilépek belőle
target.close()

###Kiolvastatom a file tartalmát, megnézem, hogy mit írtam bele.
target2 = open(filename,'r')
print(target2.read())
target.close()
