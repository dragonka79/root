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
