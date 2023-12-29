print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you are {age} old, {height} tall and {weight} heavy.")

magos = input("Mily magos vagy ecsém? ")
széles = input("Milyen széles vagy ecsém? ")
haj = input("Milyen szinű a hajad? ")
#print(f"{magos} centi magas vagy.")
print(magos + " centi magas vagy, " + széles + " centi széles vagy, és " + haj +
" színű a hajad.")
print(f"{magos} centi magas vagy, {széles} centi széles vagy, és {haj} színű a hajad.")

print('Enter your name:')
x = input()
print('Hello, ' + x)


print("Adjunk össze 2 számot mert az buli.")
print("Mi az első szám?", end = ' ')
elso_szam = float(input())
print("Add meg a második számot:", end = ' ')
masodik_szam = float(input())
osszeg = elso_szam + masodik_szam
print(f"A megadott {elso_szam} és {masodik_szam} összege {osszeg}.")
