import string

## Szöveg tisztítása függvény az egyéb karakterektől

def irasjel_eltavolitas(szoveg):
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli


with open("C:/Users/A44793837/OneDrive - Deutsche Telekom AG/python/20/alice_in_wonderland.txt") as open_text:
    lower_text = open_text.read().lower()

szavak = irasjel_eltavolitas(lower_text).split()

szavak_szamlalo = {}
for szo in szavak:
    szavak_szamlalo[szo] = szavak_szamlalo.get(szo, 0) + 1

szavak_lista = list(szavak_szamlalo.items())
szavak_lista.sort()

print(f"Szavak{' ' * 73}Száma\t")
print('=' *84)
for i in range(len(szavak_lista)):
    print(f"{szavak_lista[i][0]:<40}{' ' * 40}{szavak_lista[i][1]:>4}")

print('\t')

print('Alice {0}-szor szerepel a szövegben.'.format(szavak_szamlalo['alice']))
