from math import sqrt

(a, b) = (1, 1)
def atfogo(a, b):
    """
    A derékszögő háromszög 2 befogója hosszából visszaadja az átfogó hosszát
    """
    return(sqrt(a **2 + b ** 2))

print(atfogo(a, b))
