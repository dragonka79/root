from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#We could do these two on one line, how?

###A következő kettő sor helyettesíthető az alattuk lévő 3ikkal.
#in_file = open(from_file)
#indata = in_file.read()
indata = open(from_file).read()
#ez 2x olvassa ki a from_file tartalmát és rakja bele az indata-ba
#indata = open(from_file).read() *2 
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exists? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTRL-C to abort.")
input()


###A következő kettő sor helyettesíthető az alattuk lévő 3ikkal.
#out_file = open(to_file,'w')
#out_file .write(indata)
out_file = open(to_file,'w').write(indata)


print("Alright, all done.")

###Az out_file-t le kell zárni, hogy a to_file mentődjön,de ha az out_file-t
# egy sorba írom akkor a python zárja ha a sor lefut, így a close ekkor nem kell
#out_file.close()

#Nem kell lezárni az in_file-t ha az indata változóban kinyitom és olvasom
# a file-t egyszerre.
#in_file.close()


###A következő kettő sor helyettesíthető az alattuk lévő 3ikkal.
#out_file_again = open(to_file)
#print(out_file_again.read())
print(open(to_file).read())
