
###Definiálok egy függvényt 2 argumentummal, és néhány kinyomtatni való
###sorral. Itt csak definiálok, a nyomtatás akkor lesz ha majd a függvényre
###az argumentumaival hivatkozok
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
###Megadom a függvényt az argumentumaival, így a definícióban lévő értékek
###lefutnak, a 4 sor nyomtatása is
cheese_and_crackers(20, 30)

###A függvény argumentumai lehetnek változók is
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

###Hivatkozok a függvényre, az argumentumok változók, hivatkozok rá, tehát
### a függvény definíciója lefut, így a printek is
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

###A függvény argumentumainak értékei lehetnek matematikai összegek is
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

###A függvényel argumentumainak értékei lehetnek egy változó és egy szám
###összege
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)






from math import sqrt
def függvény(arg1, arg2):
    print(f"1 argumentum: {arg1}, 2 argumentum: {arg2}")
#1
függvény(2020,2021)

#2
argum1 = 2022
argum2 = 2023
függvény(argum1, argum2)

#3
függvény(argum1 + 2, argum2 + 2)

#4
függvény(sqrt(argum1), sqrt(argum2))

#5
függvény(sqrt(int(argum1)), sqrt(int(argum2)))

#6

print("Add meg a függvény 2 argumentumát" )
argg1 = input('első argumentum: ')
argg2 = input('második argumentum: ')
függvény(argg1, argg2)


#7

print("Add meg a függvény 2 argumentumát, legyen 2 szám" )
argg1 = float(input('első argumentum: '))
argg2 = float(input('második argumentum: '))
függvény(sqrt(argg1), sqrt(argg2))
