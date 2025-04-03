#Általánosítva, r = 13-hoz igazítva tetszőleges r < 100-ra
r = 11

print(' ' * 5, end='')
for i in range(1,r):
    print("{0:>5}".format(i), end='')
print('\a')
print(f"  :",'-' * (61 + (r-13) * 5))

for i in range(1,r):
    print("{0:>2}:{1}".format(i, ' ' * 2), end='')
    for j in range(1, r):
        print("{0:>5}".format(i * j),end='')
    print('\a')
