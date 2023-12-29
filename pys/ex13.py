from sys import argv
# read the WYSS section for how to run this

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

print(argv)

from sys import argv
from math import sqrt
script, második, harmadik = argv

print("Ez az első argumentuma az argv-nek, a script neve", script)
print("Ez a második argumentuma az argv-nek, a gyöke ", (sqrt(float(második))))
print("Ez a harmadik argumentuma az argv-nek, a 3-ik hatvány", int(harmadik) * 3)


from sys import argv
from math import sqrt
#script, négyzetgyök, háromszoros = argv

négyzetgyök = float(input("Adj meg egy számot és én gyököt vonok belőle: \n>"))
háromszoros = float(input ("Adj meg egy számot és felszorzom hárommal: \n>"))

print(f"A {négyzetgyök} négyzetgyöke: ", sqrt(négyzetgyök))
print(f"A {háromszoros} háromszorosa: ", (háromszoros) * 3 )
