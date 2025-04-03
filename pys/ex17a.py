###Hogyan lehet file-t másolni egy soros paranccsal

from sys import argv
script, from_file, to_file = argv

open(to_file,'w').write(open(from_file).read())
print(open(to_file).read())
