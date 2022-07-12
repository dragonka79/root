def kamatos_kamat(c, r, m ,t):
    """Kamatos kamat számítás c alapra"""

    fv = c * ((1 + r / m) ** (m * t))
    return fv

alap = float(input(' > '))
vegosszeg = round(kamatos_kamat(alap, 8/100, 12, 5), 3)
print(vegosszeg)

