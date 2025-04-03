# TUPLES ARE IMMUTABLE, FASTER THAN LISTS AND - SINCE IT IS IMMUTABLE- THE VALUES CAN BE A KEY FOR A DICTIONARY

t = (1, 2, 3, 4)
print(t)
print(t[1])
print(type(t))

l = [4, 5 ,6, 7]
print('l típusa: ', type(l))
s = tuple(l)
print('s típusa: ', type(s))
print(len(l))
