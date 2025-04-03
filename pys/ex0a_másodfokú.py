from math import sqrt
from decimal import *

print("Add meg a másodfokú egyenlet együtthatóit (a, b ,c):")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print("A másodfoku egyenlet tehát a következő:")

print(f"{a}*x^2 + {b}*x + {c}")

disk1 = (b*b + 4*a*c)
disk2 = (b*b - 4*a*c)

if disk1 >= 0:

    print(f"A másodfokú egyenlet egyik gyöke:")
    print(-b + sqrt(négyzetgyök1) / 2*a)
else:
    disk1 = -1 * disk1
    neggyök1 = -b  + sqrt(disk1)
    print(f"{neggyök1}i")

if négyzetgyök2 >= 0:

    print(f"A másodfokú egyenlet másik gyöke:")
    print(sqrt(négyzetgyök2))
else:
    négyzetgyök2 = -1 * négyzetgyök2
    neggyök2 = sqrt(négyzetgyök2)
    print(f"{neggyök2}i")



#print("Ennek az egyenletnek az egyik gyöke komplex szám")
#print("Ennek az egyenletnek az egyik gyöke komplex szám")
