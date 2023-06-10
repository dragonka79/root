k = 1.65

def szamlalo_3(n):
    """Decimális számjegyek számlálása valós számokban, csúnya módszer"""
    n = abs(n)
    j = 0
    if n > 1:
        for i in str(n):
            if i == '.':
                break
            else:
                j += 1
    else:
        print("A szám kisebb mint 0, decimális számjegyek száma:")
    return j


print(szamlalo_3(k))

