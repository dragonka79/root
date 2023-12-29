from sys import exit

def die(arg):
    print(arg, "Csáó")
    exit(0)

def negatív():
    print("Szomorúan hallom.")

def pozitív():
    print("Ezt örömmel hallom")


print("Hogy érzed magad?")
válasz = input("> ")
if "nem" in válasz:
    negatív()
elif "rossz" in válasz:
    negatív()
elif "szar" in válasz:
    negatív()
elif "jó" in válasz:
    pozitív()
else:
    die("Nem ez volt a kérdés.")
