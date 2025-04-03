# Decapitalizing and removing some characters

j = "ABcv,U:l.,"
k = j.casefold().replace(",", "").replace(":", "").replace(".", "")
l = j.lower().replace(",", "").replace(":", "").replace(".", "") # <- lower is same as casefold but doing in a safely manner

print(k)
print(l)