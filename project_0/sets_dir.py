s1 = {1, 2, 3}
s2 = {2, 3, 4, 5}

s_union = s1.union(s2)
print(" union of s1 and s2 sets: ", s_union)
s_intersect = s1.intersection(s2)
print(" intersection of s1 and s2 sets: ", s_intersect)

print(type(s_union))

# What the dirs(aka functions) sets can be operated on.

print(dir(s_union))
