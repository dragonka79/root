from teszt import teszt

def vektorialis_szorzat(u, v):
    """Két vektor vektoriális szorzatát adja vissza
    """
    c1 = u[1] * v[2] - u[2] * v[1]
    c2 = u[2] * v[0] - u[0] * v[2]
    c3 = u[0] * v[1] - u[1] * v[0]
    c = [c1, c2, c3]
    return c

# print(vektorialis_szorzat([1, 2, 3], [4, 5, 6]))

teszt(vektorialis_szorzat([1, 2, 3], [4, 5, 6]) == [-3, 6, -3])
teszt(vektorialis_szorzat([-1, 1, 0], [1, -1, 2]) == [2, 2, 0])