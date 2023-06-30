sztring = "Missi ssippi"
betu_szamlalo = {}
for betu in sztring:
    betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1

print(betu_szamlalo)
