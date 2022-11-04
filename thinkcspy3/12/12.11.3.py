# shallow copy vs deep copy
# https://realpython.com/copying-python-objects/
import copy

os = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ss = copy.copy(os)
os[1][2] = 'v'
print(os)
print(ss)

ds = copy.deepcopy(os)
os[1][2] = 6

print(os)
print(ds)

