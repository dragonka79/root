def derekszogu_e(a, b, c):
    E = 0.000001

    """Meghatároza, hogy a háromszög derékszögű-e"""

    # Háromszög létezés feltétele
    if ((a > 0 and b > 0 and c > 0)) and \
        ((a + b - c > E) and (a + c - b > E) and (b + c - a > E)):
    # A derékszögű feltétel
        if abs(a ** 2 + b ** 2 - c ** 2) < E or \
           abs(a ** 2 + c ** 2 - b ** 2) < E or \
           abs(b ** 2 + c ** 2 - a ** 2) < E:
           return True
        else:
            return False
    else:
        v = "A három adat nem háromszöget határoz meg"
        return v
        

(a, b, c) = (5, 12, 12.9999999)

print(derekszogu_e(a, b ,c))


