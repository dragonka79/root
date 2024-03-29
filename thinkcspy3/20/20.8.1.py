ABC = "abcdefghijklmnopqrstuvwxyz0123456789"
string_text = "Ez a Sztring Kis es Nagy Betuket tartalmaz.0."
string_text_lower = string_text.lower()
betu_szamlalo = {}
for betu in string_text.lower():
    if betu in ABC:
        betu_szamlalo[betu] = betu_szamlalo.get(betu, 0) + 1

betuk = list(betu_szamlalo.items())
betuk.sort()

for b in betuk:
    if b[0] in ABC:
        print(f"{b[0]}  {b[1]}")

## Full list, including non-existing values

for a in ABC:
        print(f"{a}   {betu_szamlalo.get(a, 0)}")
