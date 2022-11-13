# 90 fokos forgatás pozitív irányba
# 90 fokos forgatásnál a forgatás után az első elem a legbalra lévő lesz, tehát az eredetileg a legnagyobb értékű.
# Ennek az elemnek az indexe lesz a forgatás utáni első elem értéke

def rotate_90(megoldas):
    rotate90 = []
    x = len(megoldas) - 1
    while x != -1:
        rotate90.append(megoldas.index(x))
        x -= 1
    return rotate90

print(rotate_90([0, 4, 7, 5, 2, 6, 1, 3]))