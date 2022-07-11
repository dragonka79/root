xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a. Írj egy ciklust, amely mindegyik számot kiírja egy új sorba!

for i in xs:
    print(i)
print("\a")

# b. Írj egy ciklust, amely mindegyik számot és azok négyzetét is kiírja egy 
# új sorba!

for i in xs:
    print(i, i**2)
print("\a")

# c.Írj egy ciklust, amely összeadja a listában szereplő összes számot egy 
# összeg változóba! Az összeg változónak 0 értéket kell adnod az összegzés 
# előtt, majd a ciklus befejezése után az összeg változó értékét írasd ki!

összeg = 0
for i in xs:
    összeg += i
print(összeg)
print("\a")


szorzat = 1
for i in xs:
    szorzat *= i
print(szorzat)