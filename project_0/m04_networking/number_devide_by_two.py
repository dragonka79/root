# Dividing an even number by two and returning the value with exception handling.

try:
    number = int(input("Give me a number:> "))
    assert number % 2 == 0
except:
    print("Not an even number!")
else:
    x = int(number / 2)
    print(x)