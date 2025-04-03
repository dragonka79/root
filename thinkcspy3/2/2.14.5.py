C = 10000
r = 8 /100
m = 12
t = int(input("Give the years in integer > "))

FV = round(float(C * ((1 + (r / m)) ** ( m * t))), 3)

print(f"You  have {FV} HuF after {t} years")