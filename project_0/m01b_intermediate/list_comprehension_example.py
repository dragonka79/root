
# Non list comprehension way

list1 = list()

for i in range(1,5):
    list1.append(i)
print("list1:",list1)

# List comprehension way

list2 = [i for i in range(1,5)]
print("list2:", list2)

# List comprehension way with conditional
# Listing the even numbers between [2,10]

list_even = [i for i in range(1,11) if i%2 ==0]
print("list_even:", list_even)

# List comprehension way with conditional
# Listing the even numbers between (1,18) except the ones cannot be divided by 4.

list_even_except_4 = [i for i in range(1,18) if ( i%2 ==0 and not i%4==0)]
print("list_even_except_4:", list_even_except_4)