from math import pi

r = 1
def kor_terulet(r):
    """Visszaadja egy r sugarú kör területét 3 tizedesjegyig"""
    return round((r ** 2 *pi), 3)

print(kor_terulet(r))
