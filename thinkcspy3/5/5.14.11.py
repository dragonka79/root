def derekszogu_e(a, b, c):
    """Meghatároza, hogy a háromszög derékszögű-e"""

    # Háromszög létezés feltétele
    if ((a > 0 and b > 0 and c > 0))and \
        ((a + b > c) or (a + c > b) or (b + c > a)):
    # A derékszögű feltétel
        if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or \
           (b ** 2 + c ** 2 == a ** 2) or (a ** 2 + c ** 2 == b ** 2):
           return True
        else:
            return False
    else:
        v = "A három adat nem háromszöget határoz meg"
        return v
        

(a, b, c) = (13, 12, 5)

print(derekszogu_e(a, b ,c))
