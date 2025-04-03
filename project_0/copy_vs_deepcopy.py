
from copy import copy
from copy import deepcopy

xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Shallow copy
ys = copy(xs)

xs.append("új_copy")
xs[2][2] = 0
print(f"xs: {xs}")
print(f"ys: {ys}")

# Deepcopy

zs = deepcopy(xs)

xs.append("új_deepcopy")
xs[2][2] = 1
print(f"xs: {xs}")
print(f"zs: {zs}")