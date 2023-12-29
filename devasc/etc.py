# Ez a kis program egy bemeneti szövegből levágja az első n karaktert és kisbetűkké konvertálja azt

n = 20
be = input(f"Adj meg egy bármit de legyen az első {n} karakterében nagybetű: ")
kis = str.lower(str(be[:n]))

print(kis)
