j = 6
numbers = []
def loop(arg):
    i = 0
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


loop(j)
print("The numbers: ")

for num in numbers:
    print(num)
print(numbers)
