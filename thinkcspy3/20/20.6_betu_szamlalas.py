# Betűk számlálása előfordulásuk gyakoriságával

string_text = "Egy ilyen gyakorisági táblázat hasznos lehet egy szövegfájl tömörítéséhez."
betu_szamlalo = {}
for betu in string_text:
    betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1

betuk = list(betu_szamlalo.items())
betuk.sort()

print(betuk)