def add(a, b):
    print(f"ADDING {a} + {b}")
    return int(a + b)

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return int(a - b)

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return int(a * b)

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return int(a / b)


print(f"Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


#A puzzle for the extra credit, type it in anyway.
print("Here's the puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what2 = add(age, subtract(height, multiply(weight + 20, divide(iq + 30, 2) +26)))
print("That becomes: ", what, "Can you do it by hand?\n")
print("That becomes: ", what2, "Can you do it by hand?")
print("\n\n\n")


def négyzet(a):
    print(f"NÉGYZETRE {a} * {a}")
    return (a * a)

terület = négyzet(15)
print(f"{terület}\n\n\n")

def add1(c, d):
    return (c + d)
def sub1(c, d):
    return(c - d)
def oszt1 (c, d):
    return(c / d)

a1 = add1(24, 34)
b1 = sub1(100, 1023)
c1 = oszt1(a1, b1)

print(f"a1 = {a1}\nb1 = {b1}\nc1 ={c1}")


#Két számot add össze, a két számot bekéri billentyűzetről

def összead(e, f):
    print(f"Ez a függvény összead két számot, {e}-t és {f}-t.")
    return(e + f)
print("Adj meg két számot és összeadom őket.")
e = int(input("Első szám: "))
f = int(input("Második szám: "))
összeg = összead(e, f)
print(f"A két szám összege: {összeg}.")



#Megadja két szám szántani közepét

def számtani_közép(e, f):
    print(f"Ez a függvény megadja két szám számtani közepét, {e}-t és {f}-t.")
    return((e + f)/2)
print("Adj meg két számot és kiszámolom a számtani közepüket.")
e = int(input("Első szám: "))
f = int(input("Második szám: "))
szközép = int(számtani_közép(e, f))
print(f"A két szám számtani közepe: {szközép}.")
