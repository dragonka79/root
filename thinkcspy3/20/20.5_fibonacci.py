# # Fibonacci: recursion only

# def fib(n):
#     if n <= 1:
#         return n
#     t = fib(n-1) + fib(n-2)
#     return t

# import time
# n = 35
# t0 = time.process_time()
# eredmeny = fib(n)
# t1 = time.process_time()
# print("fib({0}) = {1}, ({2:.2f} masodperc)".format(n, eredmeny, t1-t0))


# Fibonacci: rekursion + dictionary

# import sys
# print(sys.getrecursionlimit()) # Lekérem a rekurzió limitet, ami alapértelmezetten 1000
# sys.setrecursionlimit(1500)

import time
known = {0: 0, 1: 1}


def fib(n):
    if n not in known:
        new_value = fib(n-1) + fib(n-2)
        known[n] = new_value
    return known[n]


print(fib(100))
print("\t")

n = 1086  # 1086 utolsó szám amire még lefut az alapértelmezett 1000 rekurzió limittel
t0 = time.process_time()
eredmeny = fib(n)
t1 = time.process_time()
print("fib({0}) = {1}, ({2:.2f} masodperc)".format(n, eredmeny, t1-t0))
print("\t")

count = 0
eredmeny_string = str(eredmeny)
for nn in eredmeny_string:
    count += 1
print(f"The given fibonacci number has {count} digits.")
