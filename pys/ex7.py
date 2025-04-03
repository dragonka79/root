print("Marry had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everwhere that Mary went.")
print("." *10) #what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that come at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# 10 darab pontot rajzol a képernyőre egymás alá
i = '.'
for _ in range(10):
    print(i)

print('')

# 10 darab pontot rajzol a képernyőre átlóban balra dőlve while-lal

j = 0
while j<10:
    print(' ' * j, end='')
    print('.')
    j+=1

# 10 darab pontot rajzol a képernyőre átlóban jobbra dőlve for-ral

for j in range(10,0,-1):
    print(' ' * j, end='')
    print('.')
