#Ez a program bekéri, hogy hogyan érzed magad, a kulcs szavakat egy listából
#szedi ki. For és while ciklussal megoldva.

from sys import exit

pozlista = ['jó', 'kiváló', 'prím', "nagyszerű"]
neglista = ['nem', 'szar', 'rossz']

#print("Neglista hossza:",len(neglista))
#print("Pozlista hossza:",len(pozlista))

def die(arg):
    print(arg, "Csáó")
    exit(0)

def negatív():
    print("Szomorúan hallom.")
    exit(0)
def pozitív():
    print("Ezt örömmel hallom")
    exit(0)

print("Hogy érzed magad?")
válasz = input("> ")

#1.for ciklussal

for h in range(len(neglista)):
    if neglista[h] in válasz:
        negatív()

for h in range(len(pozlista)):
    if pozlista[h] in válasz:
        pozitív()

die("Nem ez volt a kérdés.")


#2.while ciklussal

h = 0
while h <len(neglista):
    if neglista[h] in válasz:
        negatív()
    else:
        h+=1

j = 0
while j <len(pozlista):
    if pozlista[j] in válasz:
        pozitív()
    else:
        j+=1

die("Nem ez volt a kérdés.")
