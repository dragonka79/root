print("I \"understand\" joe.")

# escape double–quote inside string
print("I am 6'2\" tall.")

# escape single–quote inside string
print('I am 6\'2" tall.')

#a \t tabot nyom
tabby_cat = "\tI'm tabbed in."

# \n sort tör (entert üt)
persian_cat = "I'm split\non a line."
persian_cat2 = "I'm split\n on a line."
persian_cat3 = "I'm split\ron a line."

# backslash kiírása
backslash_cat = "I'm \\ a \\ cat. "

backslash_cat2 = "I'm \ a \ cat. "
backslash_cat3 = "I'm \a a \ cat. "

# a \n fölösleges mert minden sor végén entert üt
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(persian_cat2)
print(persian_cat3)
print(backslash_cat)
print(backslash_cat2)
print(backslash_cat3)
print(fat_cat)

x = "Hello"
print("\t",x, "\bNane")
y = "\tHolla"
print(y.format(y))
print("\n\n\n")

###Gyakorlás, nem az anyag része
print("I \"understand\" Joe")
print("I am 6'2\" tall.")
print("\t I'm tabbed in")
print("I am split\non a line.")
print("I'm \\ a \\ cat.")
print("I am a \\ cat.")
print("""
\t*Cat food
\t*Fishies
""")
y = "Namiva"
print(f"Hello{y}")
print(f"Hello,\b{y}")
