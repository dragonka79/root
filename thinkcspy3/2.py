
def collatz(n):
    """ 
    A sorozat következő tagja n /2 ha n páros, 3n +1 ha n páratlan
    A sorozat n = 1-ig fut.
    """
    counter = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2 #  //: int típust ad vissza és nem float-ot                   
        else:
            n = (3 * n) + 1
        counter += 1
        print(n)
    print('\a')
    return counter
    

print(collatz(181))