

# 2.12
# Másodpercek átszámítása órákká, percekké és másodpercekké

másodpercek = int(input("Add meg a másodpercek számát és én kiszámolom, hogy \
az hány óra és hány perc. >> "))

órák = másodpercek // 3600
percek = (másodpercek % 3600) // 60
mperc = (másodpercek % 3600) % 60

print(f"{másodpercek} másodperc = {órák} óra, {percek} perc és {mperc} másodperc")


# 2.14.5

C = int(10000)
m = int(12)
r = float(0.08)
t = int(input("Hány évre kössük le a betétet: > "))

FV = float(C * (1 + (r / m)) ** (m * t))
print("A futamidő végén a kivehető összeg: ", FV)


# 2.14.7

v = int(14 + 51) % 24
print(f"Az óra {v} órakor fog megszólalni.")


# 2.14.8

óra = int(input("Hány óra van? > "))
ébresztő = int(input("Hány órával később csörögjön? > "))
csörög = int((óra + ébresztő) % 24)
print(f"Az óra {csörög} órakor fog ébreszteni.")

# 2.14.8.1 (profibb megoldás)

x = int(input("Hány óra van most? >: "))
t = int(input("Hány órával később szólaljon meg az óra?>: "))
y = int((x + t) % 24)
if y == 12:
    print('Az óra délben csörög')
elif y == 0:
    print('Az óra éjfélkor csörög')
elif y < 12:
    print(f'Az óra délelőtt {y} órakor csörög')
elif y > 12:
    z = y - 12
    print(f'Az óra délután {z} órakor csörög')
