known = {0: 0, 1: 1}


def fib(n):
    if n not in known:
        new_value = fib(n-1) + fib(n-2)
        known[n] = new_value
    return known[n]


print("\n", fib(100), "\n")
