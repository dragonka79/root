# LIST COMPREHENSION

num_string = " one, two, three "

# 1.1 Making a list of 'num_string'

num_list = list()

for numbers in num_string.split(","):
    num_list.append(numbers.strip())
print("num list: ", num_list)

# 1.2 Making a list of 'num_string', advanced level, same result using list comprehension

num_list_2 = [ numbers.strip() for numbers in num_string.split(",")]
print("num_list_2: ", num_list_2)


# 2.0 Printing numbers in a range

j = [str(i) for i in range(1,10)]
print(j)


# 3.0 Printing odd numbers only in a range

l = [ p for p in range(1,15) if p%2 != 0 ]
print(l)