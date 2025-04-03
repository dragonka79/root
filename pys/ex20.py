from sys import argv

script, input_file = argv

### A print_all függvény definíciója, aminek argumentuma a mgnyitott input_file.
###Aztán az f.read()-del elolvasom az egész file-t és kiprintelem.
def print_all(f):
    print(f.read())

### A rewind def-je. Az f.seek(0)-val visszaugrok a file elejére (0 byte)
###mert mivel
###fenn kiírattam teljesen,
###az f tárolja a pozit, mivel totál kiírattam, ezért a file végén van,
###ezért most a képzeletbeli kurzor a file végén villog.
def rewind(f):
    f.seek(0)

###A print_a_line defje, megadom a 2 argumentumot.
###Kiíratom a line sorszámát(current_line, lenn) és a line-t magát a sor végén
##lévő enterrel, ezért alapban üres sorok vannak a sorok között.
###fontos: a readline onnan tudja, hogy melyik sor következik, hogy a readline
# a sor elolvasása után a következő sor elejére ugrik
def print_a_line(line_count, f):
    print(line_count, f.readline(),end = "")

###Megnyitom a txt file-t aminek a sorait ki akarom íratni.
current_file = open(input_file)
#end

###Kiíratom a teljes doksit
print("First let's print the whole file:\n")

###Melyik file legyen a print_all argumentuma(az f mint file)
print_all(current_file)
#

print("Now let's rewind kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)



#Át vannak a részek mozgatva, jobban lehet látni mi mihez tartozik.


from sys import argv
script, input_file = argv


#itt kinyomtatom a print_all argumentumát, ami a megnyitott input_file file
def print_all(f):
    print(f.read())
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)



#visszamegyek a megnyitott input_file(=current_file) 0-ik byte-jára
def rewind(f):
    f.seek(0)
print("Now let's rewind, kind of like a tape.")
rewind(current_file)




def print_a_line(line_count, f):
    #f.readline() elolvassa az első sort,és TOVÁBBUGRIK A KÖVETKEZŐ SOR ELEJÉRE
    print(line_count, f.readline())
print("Let's print three lines:")
# a sorok sorszáma manuálisan van megadva.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#Magyar változat

from sys import argv
script, könyv = argv

def teljesen_elolvas(argumentum):
    print(argumentum.read())
nyitott_könyv= open(könyv)
teljesen_elolvas(nyitott_könyv)

def visszateker(argumentum2):
    argumentum2.seek(0)
visszateker(nyitott_könyv)


def soronként(sorszám, sor):
    print(sorszám, sor.readline())

sorszám = 1
soronként(sorszám, nyitott_könyv)

sorszám +=1
soronként(sorszám, nyitott_könyv)

sorszám += 1
soronként(sorszám, nyitott_könyv)



#teljes szöveg kiíratása, sorokat megszámolja, ehhez tudni kell hány soros a
#szöveg

from sys import argv
script, file = argv

def függ(line_count, f):
    print(line_count, f.readline(), end='')
open = open(file)
for i in range(1, 7):
    line_count = i
    függ(line_count, open)
