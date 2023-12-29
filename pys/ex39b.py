dolgok = {
'Zoli' : 'okos',
'Zsuzska': 'szép'
}

print("Írj be egy nevet és megmondom, hogy milyen az illető")

be = input("> ")
print(f"{be}, ő", dolgok.get(be, 'róla nincs infóm'))
