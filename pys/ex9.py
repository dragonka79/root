# Here's some mew strange stuff, remember type exactly.

days = "Mon Tue Wed Thu Fri Sat Sun "
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days ", days*2)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# 3 sorba írja ki a days változó értékét, a sorok között üres sor
#Ezt a \n-nel érem el, ez a new line

for _ in range(3):
    for i in days:
        print(i, end = '')
    print('\n')


# 3 sorba írja ki a days változó értékét, a sorok között NINCS üres sor
#Ezt a \r-nel érem el, ez a line feed

for _ in range(3):
    for i in days:
        print(i, end = '')
    print('\r')
