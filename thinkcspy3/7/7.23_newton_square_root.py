from math import pow

def gyok(N):
    """Newton's method to find the square root of a positive number N"""
    c = 0   # Counter for the steps
    kozelites = N/2.0
    while True:
        c += 1
        jobb = (kozelites + N/kozelites)/2.0
        if abs(kozelites - jobb) < pow(10, -6):
            return (jobb, c)
        else:
            kozelites = jobb
            # print(jobb)

# Teszt esetek
print(gyok(25.0))
print(gyok(49.0))
print(gyok(81.0))
print(gyok(100.0))
print(gyok(1024.0))
