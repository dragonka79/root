j = 6
k = 2
numbers = []
def loop(j,k):
    i = 0
    while i < j:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + k
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


loop(j,k)
print("The numbers: ")

for num in numbers:
    print(num)
print(numbers)
