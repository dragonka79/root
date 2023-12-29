#37.Keywords

#1.and
import random
print("Pénzérmét dobsz fel kétszer")
dobas1 = random.randint(1,2)
dobas2 = random.randint(1,2)
print(f"{dobas1}, {dobas2}")
if dobas1 == 1 and dobas2 == 1:
    print("A két fejet dobtál.")
elif dobas1 == 2 and dobas2 == 2:
    print("A két írást dobtál.")
else:
    print("Egy fejet és egy írást dobtál.")

#2. with as

from sys import argv
script, to_file = argv

test = open(to_file,'w')
test.write("Hello\n")
test.close()

#A test.write során történhet kivétel, amely meggátolhatja hogy a file
#szabályosan bezáródjon, ami bugokat idézhet elő illetve pl. nem minden
#változás íródik be a file-ba. Az with as-zel ilyen nem fordulhat elő. Itt ugye
#nincs .close(), de nincs is rá szükség, így a file biztosan bezárul
#szabályosan.
#https://www.geeksforgeeks.org/with-statement-in-python/

with open(to_file,'w') as test:
    test.write("Hello\n")

#3. assert. Az assert egy állítás, a mögé írt feltétel igazság állapotát
#vizsgálja. Akkor ad vissza Assertionerror-t ha a feltétel hamis, ha igaz
#akkor nem dob vissza semmit. Lehet
#üzenetet is írni mögé, vesszővel elválasztva a feltételtől, zárójel nem kell.
#https://www.w3schools.com/python/ref_keyword_assert.asp


#3.1

x = '17'
assert x == "17", "x should be '42'"

#3.2

assert 2 + 2 == 5, "Houston we've got a problem"


#4. break. A break for vagy while loop esetén megszakítja a loopot.
#https://www.w3schools.com/python/ref_keyword_break.asp

#Melyik az a legkisebb szám 500 és 600 között, amely osztható 31-gyel?

for i in range(500, 601):
    if i % 31 == 0:
        print(i)
        break


#5. continue. A continue kulcsszó for vagy while ciklus esetén megszakítja az
#iterációt majd folytatja, kihagyva az a lépést, amire a ciklus feltétele
#megszakítja a ciklust.
#https://www.w3schools.com/python/ref_keyword_continue.asp

#1 és 10 között írd ki a páratlan számokat egymás mellé.

for i in range(1,11):
    if i % 2 == 0:
        continue

    print(i, end = ' ')
print('\r')


#6. try - except block. Kivételkezelés. Ha a try blokkban a feltétel teljesül és
#úgy hibára futna a program, akkor nem omlik össze a program, hanem az except
#ágban szereplő utasítás fog lefutni.
#https://pythonbasics.org/try-except/

#6.1 kis program a 0-val való osztásra. A Hello üzenet nem fog kiíródni, mert a
#program ZeroDivisionError-ral elszáll mielőtt kiíródhatna

x = 1 / 0
print(x)
print("Hello")

#6.2. Két véletlenül szám, amelyek [1,5] közé esnek, 5-tel van elosztva a
#különbségük. Ha a két szám egyforma, akkor a különbségük nulla, de a
#kivételkezelés miatt csak egy szöveget ír ki, és a program végén a szöveg
# is kiíródik.

import random

for _ in range(10):
    x = random.randint(1,5)
    y = random.randint(1,5)
    print(x,y)
    z = x - y
    try:
        u = 5 / z
        print(u)
    except ZeroDivisionError:
        print('Divided by zero')

print("Hello")




#6.3 A bemenetre kér egy egész számot és megszorozza 17-tel. Ha nem egész
#számot kap, akkor kiír egy szöveget és nem az alapban generál hibát dobja.

print("Adj meg egy egész számot és megszorzom 17-tel")
i = input("> ")
try:
    print(int(i) * 17)
except:
    print("Nem egész számot adtál meg, a program kilép.")


#7. finally keyword a try-except-finally blokkban. A finally részben lévő
#utasítás mindenképpen lefut attól függetlenül, hogy a program hibára fut-e
#vagy sem.

#7.1. Írassuk ki egy x változó értékét, vagy ha a változó nem létezik, dobjon
#hibaüzenetet. Egy végső üzenet mindkét esetben fusson le.

x = 'Hello'

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

 #Érdekes probléma: a test.txt file-ba nincs írásjogom. Ha írással akarom
 #megnyitni akkor nem fut le az except rész, de ha olvasással akkor igen.
 #Miért?


 try:
   f = open("test.txt", 'r')
   f.write("Lorum Ipsum")
 except:
   print("Something went wrong when writing to the file")
 finally:
   f.close()

#zolcs@zolcs-CM:~/Dropbox/python/pys$ python3.6 ex0.py
#Something went wrong when writing to the file
#zolcs@zolcs-CM:~/Dropbox/python/pys$


try:
  f = open("test.txt", 'w')
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()


# zolcs@zolcs-CM:~/Dropbox/python/pys$ python3.6 ex0.py
# Something went wrong when writing to the file
# Traceback (most recent call last):
#   File "ex0.py", line 7, in <module>
#     f.close()
# NameError: name 'f' is not defined
# zolcs@zolcs-CM:~/Dropbox/python/pys$





 #8. global keyword. A global kulcsszóval létre tudok hozni egy globális
 #változót egy függvényen belül, és annak az értékét tudom a függvényen belül
 #változtatni és kívülről meghívni.
#https://www.programiz.com/python-programming/global-keyword

 c = 0
 print("c kezdeti globális értéke:", c)
 def függvény1():
     global c
     c += 2
     print("c értéke függvény1-ben:", c)
     függvény2()

 def függvény2():
     global c
     c += 3

 függvény1()

 print("c értéke függvény2-ben:", c)
 c += 4
 print("c végső globális értéke:", c)





 #9. is keyword. Azt nézi, hogy 2 objektum ugyanaz-e. Nem azt nézi, hogy az
 #értékük ugyanaz-e. Azt ellenőrzi, hogy 2 néven vajon fut-e ugyanaz az
 #objektum. Összehasonlítja a memória címeket. Ha egyeznek True-t ad vissza,
 #ha nem akkor False-t.
#https://www.w3schools.com/python/ref_keyword_is.asp#:~:text=The%20is%20
#keyword%20is%20used,if%20two%20variables%20are%20equal.
#https://stackoverflow.com/questions/2987958/how-is-the-is-keyword-implemented
#-in-python


 #9.1. Itt megegyezik a két objektum:

x = ["apple", "banana", "cherry"]
y = x
print(x is y)


#9.2 Itt már False az érték, a 2 változónak ugyanaz az értéke de nem ugyanazok:

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)

#9.3 Itt is False, mert két sztringet hasonlít össze és azokat a phyton
#különböző memória helyekre írja:

a = 1
print(("a" * 100) is ("a" * 100))




#10. lambda kulcsszó.
#formája: lambda argument(s): expression
#Létrehoz egy kisebb névtelen függvényt, akármennyi
#argumentuma lehet, de csak egy kifejezése.
#https://www.programiz.com/python-programming/anonymous-function
#https://www.w3schools.com/python/ref_keyword_lambda.asp

#10.1. Létrehoz egy olyan függvényt, amely visszaadja a számok kétszeresét.

double = lambda x : x*2
print(double(5))

#ez olyan mint:
x = 5
x = x * 2
print(x)

#vagy ez:

def double(x):
    return x * 2
print(double(5))


#10.2. Van egy listám és azokból kiszedem a páros számokat egy másik listába.

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = list(filter(lambda x: x % 2 == 0, my_list))
print(even_list)


#11. pass kulcsszó. A pass statement a no operation(NOP) vagy null statement,
#arra való, hogy foglaljuk a helyet egy code számára a jövőben. Függvényekben,
#classokban definiciókban, ha pass-t írunk akkor nem fut a program hibára.
#Arra is használható, hogy ha egy feltétel teljesül/nem teljesül akkor
#fusson tovább a program.
#https://www.askpython.com/python/python-pass-statement-keyword
#https://www.w3schools.com/python/ref_keyword_pass.asp
#https://www.programiz.com/python-programming/pass-statement

#11.1: Üres függvény létrehozása (és majd későbbi feltöltése):

def függvény():
    pass


#11.2: Ugyanaz mint a 10.2, azaz egy listából kiszedi a páros számokat egy
#másik listába, de itt most bonyolultabban.

def remove_odds(list_numbers):
    list_evens = []
    for i in list_numbers:
        if i % 2 != 0:
            pass
        else:
            list_evens.append(i)
    return list_evens


l_numbers = [1, 5, 4, 6, 8, 11, 3, 12]
l_evens = remove_odds(l_numbers)
print(l_evens)



#21. Dictionary: Kulcs:érték párokat tartalmaz.

# Egy tel nevű dict a következő értékekkel: zoli=79, feri=80

tel = {'zoli':79, 'feri':80}

#szótár teljen tartalmának listája

print(tel)

#csak a kulcsok listázása

print(list(tel))

# a 'zoli' kulcsszóhoz tartozó érték listázása

print(tel['zoli'])

#ABC sorrendbe rendezve kiíratás a  kulcszavak alapján

print(sorted(tel))

#'zoli' benne van a szótárban?

print('zoli' in tel)

#'Zoli' benne van a szótárban?

print('Zoli' in tel)

#töröljük 'feri'-t a szótárból

del tel['feri']
print(tel)

#31. String formats. Ezek placeholderek, a % után hivnak meg különböző
#függvényeket, és formázzák, illetve helyettesítik az objectumot, ami a
#zárójelben van, esetleg listában

#31.1. Írjuk ki a nevet, mint strig-et, a szám1-et mint integert, és a szám2-t
#mint float tipusú objektumot.

name = 'zoli'
szám1 = 5
szám2 = 6
szám3 = 7


print('%s %d %f %c' % (name, szám1, szám2, szám3))
#41. semicolon(;) operátor: Egy sorba lehet több állítást írni.

name = 'zoli' ; age = 42 ; print(name, end =' '); print(age)
