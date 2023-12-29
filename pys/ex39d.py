megyék = {
'Hajdú-Bihar' : 'HB',
'Szabolcs-Szatmár-Bereg': 'SZSZB',
'Békés':'B',
'Nógrád': 'N',
'Vas' : 'V'
}
print("A 'megyék' szótár eredetileg:\n", megyék)
print("\nA megyék szótár kulcsai:")
print(megyék.keys())
#ua mint: print(list(megyék))

#rakjunk a megyék szótárba egy új elemet(key + value)
megyék.update({'Bács-Kiskun': 'Kecskemét'})
# ua. mint: megyék['bács-kiskun'] = 'kecskemét'
print("\nA megyék szótár az update után:\n", megyék)
print("\nA megyék szótár kulcsai az update után:\n", megyék.keys())



#A kiszedi az utolsó elemet a szótárból és visszaadja annak az értékét
print('A megyék szótár:', megyék)
kiszedett = megyék.popitem()
print('A kiszedett elem: ', kiszedett)
print('A maradék szótár:', megyék)



#A kiszedi az adott kulcsú elemet a szótárból és visszaadja annak az értékét
print('A megyék szótár:', megyék)
kiszedett = megyék.pop('Békés')
print('A kiszedett elem: ', kiszedett)
print('A maradék szótár:', megyék)



#A kiszedi az adott kulcsú elemet a szótárból és visszaadja annak az értékét,
#ha nincs az adott kulcsú elem a szótárban akkor a második paraméter értékével
#tér vissza, de azt nem írja bele a szótárba, hanem csak a képernyőre küldi
print('A megyék szótár:', megyék)
kiszedett = megyék.pop('Békéss', 'Ilyen megye nincs a szótárban')
print('A kiszedett elem: ', kiszedett)
print('A maradék szótár:', megyék)
