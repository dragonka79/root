#Itt van 16 darab listával kapcsolatos feladat, a megoldás a feladatok végén
#forrás: https://docs.python.org/3/tutorial/introduction.html#lists

# #1. Adva van a következő lista:
# squares = [1, 4, 9, 16, 25]
# Add vissza a lista első elemét

# #2.Feladat: Add vissza a lista utolsó elemét

# #3.Feladat: Add vissza a lista utolsó 3 elemét(slicing)

# #4.Feladat: Másoljuk(shallow copy) a teljes squares listát egy másik listába,
#neve legyen squares_shallow_copy. Nyomtassuk ki ezt a listát.

# #5.Feladat: Adjuk hozzá(csatoljuk a végére, konkatenáció) a squares listához
# #a következő listát:[36, 49, 64, 81, 100], az új lista neve legyen
# #squares_append

# #6-ik feladat: Mennyi 4-nek a köbe és a negyedik hatványa?

# #7.Feladat: Adott a következő cubes lista:
# cubes = [1, 8, 27, 65, 125]
# #A 4-ik elem nem jó, cseréljük le a 65-öt 64-re.

# #8.Feladat: Add hozzá a cubes lista végéhez a 216-os számot illetve
# # 7 harmadik hatványát

# #9.Feladat: Adva van a következő lista:
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# #Hány eleme van a listának?

# #10. Feladat:Cseréljük ki a 'c', 'd' és 'e' karaktereket
# #'C','D' és 'E' karakterekre egyben

# #11.Feladat: A 'C', 'D' és 'E' karaktereket töröljük ki a listából

# #12.Feladat: Töröljük ki minden elemét a letters listának, legyen üres a lista


#13.Feladat: Adott 'a' és 'n' lista:

# a = ['a', 'b', 'c']
# n = [1, 2, 3]
#Tegyük be ezt a 2 lista minden eleméz egy 'x' listába, a lista elemek elől,
#n lista elemek hátul, tehát egy listát kapok 6 lista elemmel.

# #14.Feladat:
# #Tegyük be az a és n listákat egy 'xx' nevű listába, amelynek 2 eleme van
#a elől, n hátul, ezzel tehát
# # egy olyan listát kapunk (nested), amelynek 2 eleme van és azok listák

# #15.Feladat: Listázzuk ki xx listának a első elemét

# #16.Feladat: Listázzuk ki xx 0-ik elemének második elemét







#MEGOLDÁSOK:













#Adva van a következő lista:
squares = [1, 4, 9, 16, 25]

#1.Feladat: Add vissza a lista első elemét

print(squares[0])

#2.Feladat: Add vissza a lista utolsó elemét
print(squares[-1])

#3.Feladat: Add vissza a lista utolsó 3 elemét(slicing)
print(squares[-3:])

#4.Feladat: Másoljuk(shallow copy) a teljes squares listát egy másik listába,
#neve legyen squares_shallow_copy. Nyomtassuk ki ezt a listát.
squares_shallow_copy = squares[:]
print(squares_shallow_copy)

#5.Feladat: Adjuk hozzá(csatoljuk a végére, konkatenáció) a squares listához
#a következő listát:[36, 49, 64, 81, 100], az új lista neve legyen
#squares_append
squares_append = squares + [36, 49, 64, 81, 100]
print(squares_append)

#6-ik feladat: Mennyi 4-nek a köbe és a negyedik hatványa?

print(4**3, 4**4)

#7.Feladat: Adott a következő cubes lista:
cubes = [1, 8, 27, 65, 125]
#A 4-ik elem nem jó, cseréljük le a 65-öt 64-re.

cubes[3] = 64
print(cubes[:]) #vagy print(cubes)

#8.Feladat: Add hozzá a cubes lista végéhez a 216-os számot illetve
# 7 harmadik hatványát
cubes.append(216)
cubes.append(7**3)
print(cubes)

#9.Feladat: Adva van a következő lista:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
#Hány eleme van a listának?
print(len(letters[:]))

#10. Feladat:Cseréljük ki a 'c', 'd' és 'e' karaktereket
#'C','D' és 'E' karakterekre egyben
letters[2:5] = ['C', 'D', 'E']
print(letters)

#11.Feladat: A 'C', 'D' és 'E' karaktereket töröljük ki a listából
letters[2:5] = []
print(letters)

#12.Feladat: Töröljük ki minden elemét a letters listának, legyen üres a lista
letters[:] = []
print(letters)

#13.Feladat: Adott 'a' és 'n' lista:

a = ['a', 'b', 'c']
n = [1, 2, 3]
#Tegyük be ezt a 2 lista minden eleméz egy 'x' listába, a lista elemek elől,
#n lista elemek hátul, tehát egy listát kapok 6 lista elemmel.
x = a + n
print(x)
# #14.Feladat:
# #Tegyük be az a és n listákat egy 'xx' nevű listába, amelynek 2 eleme van
#a elől, n hátul, ezzel tehát
# # egy olyan listát kapunk (nested), amelynek 2 eleme van és azok listák
xx = [a, n]
print(xx[:])

# #15.Feladat: Listázzuk ki xx listának az első elemét
print(xx[0])


# #16.Feladat: Listázzuk ki xx első elemének második elemét
print(xx[0][1])
