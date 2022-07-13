def derekszogu_e(a, b, c):
    """Meghatároza, hogy a háromszög derékszögű-e"""

    # Háromszög létezés feltétele
    if ((a > 0 and b > 0 and c > 0)) and \
        (abs(a + b - c > 0.000001) or \
         abs(a + c - b > 0.000001) or \
         abs(b + c - a > 0.000001)):
    # A derékszögű feltétel
        if abs(a ** 2 + b ** 2 - c ** 2 < 0.000001) or \
           abs(a ** 2 + c ** 2 - b ** 2 < 0.000001) or \
           abs(b ** 2 + c ** 2 - a ** 2 < 0.000001):
           return True
        else:
            return False
    else:
        v = "A három adat nem háromszöget határoz meg"
        return v
        

(a, b, c) = (5, 12, 5)

print(derekszogu_e(a, b ,c))
