def karakter_szamlalas(string, karakter):
    darab = 0
    for ch in string:
        if ch == karakter:
            darab += 1
    return darab

string = "banán"
karakter = "e"
print(karakter_szamlalas(string, karakter))
