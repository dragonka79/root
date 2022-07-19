from unittest import teszt

def triangular_numbers(n):
    """The first n triangular number"""
    j = 0
    for i in range(1, n+1):
        j += i
        print(f'{i}\t{j}')

triangular_numbers(5)