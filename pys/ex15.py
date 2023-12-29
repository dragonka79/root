
###Beimportáljuk a sys package-ből az argv feature-t
from sys import argv

###Az argumentumnak legyen 2 értéke : a script neve és a txt file neve
###aminek az értékét ki akarjuk olvastatni.
script, filename = argv

###Megnyitom a txt file-t és ezt berakom egy változóba
###ITT A TXT FILE HELYE UGYANAZ MINT A SCRIPT FILE HELYE
txt = open(filename)

###Kiíratom egy sorba, hogy itt a van a file-od neve
print(f"Here's your file {filename}:")

###Elolvasom a file-t, azt a file-t amit megnyitottam, direktben nem megy,
###és kiíratom azt ami benne van
print(txt.read())

###bezárom a file-t
txt.close()

###Megkérem a usert, hogy gépelje be a file nevét újra
print("Type the filename again:")
###Az új sorban a > mint kurzor jelenjen meg, és azt a nevet amit a user begépelt
###berakom egy változóba
file_again = input("> ")

###Megnyitom a begépelt nevű filet és berakom egy változóba
txt_again = open(file_again)

###Elolvasom a megnyitott filet és közlöm, azaz kinyomtatom
print(txt_again.read())
txt_again.close()

###Megnyitni és olvasni a file-t script nélkül direkt pythonbólc


#zolcs@zolcs-CM:~/Dropbox/python/pys$ python3.6
#Python 3.6.9 (default, Nov  7 2019, 10:44:02)
#[GCC 8.3.0] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>>
#>>> jj = open('/home/zolcs/Dropbox/python/pys/ex15_sample.txt','r')
#>>> print(jj.read())
#This is stuff I typed into a file.
#It is really cool stuff.
#Lots and lots of fun to have in here.

#>>> jj.close()




from sys import argv
script, file = argv
prompt = '> '

nyit = open(file)
print('\r')
print(nyit.read())
nyit.close()
