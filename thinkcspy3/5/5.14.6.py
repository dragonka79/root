xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 
40, 39.9, 2, 0, -1]

def pont_jegy(x):
    """A pontszámok alapján kiszámítja az érdemjegyet"""
    if x < 60 and x >= 0:
        print(f"{x}, azaz elégtelen")
    elif x >= 60 and x < 70:
        print(f"{x}, azaz elégséges")
    elif x >= 70 and x < 80:
        print(f"{x}, azaz közepes")
    elif x >= 80 and x < 90:
        print(f"{x}, azaz jó")
    elif x >= 90:
        print(f"{x}, azaz jeles")
    else:
        print(f"{x} pontszám nincs")

for i in xs:        
    pont_jegy(i)
    