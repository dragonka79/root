string_text = "Ez a Sztring Kis es Nagy Betuket tartalmaz.0."
string_text_lower = string_text.lower()
betu_szamlalo = {}
for betu in string_text.lower():
    betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1

betuk = list(betu_szamlalo.items())
betuk.sort()

ABC = "abcdefghijklmnopqrstuvwxyz0123456789"

for b in betuk:
    if b[0] in ABC:
        print(f"{b[0]}  {b[1]}")

