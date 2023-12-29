megyék = {
'Hajdú-Bihar' : 'HB',
'Szabolcs-Szatmár-Bereg': 'SZSZB',
'Békés':'B',
'Nógrád': 'N',
'Heves': 'H',
'Baranya':'BA',
'Vas' : 'V'
}

print(megyék)
print(list(megyék))


print('Adj meg egy megyét, nagy kezdőbetűvel, és megnézem, mi a rövidítése.')
i = input(">")

print(f"{i} megye rövidítése:", megyék.get(i, 'nincs a listában'))

print('1#' * 55)

megyeszékhelyek = {
'HB' : 'Debrecen',
'SZSZB' : 'Nyíregyháza',
'B': 'Békéscsaba' ,
'N': 'Salgótarján',
'V': 'Szerep City Galaxis'
}

print(megyeszékhelyek)
print(list(megyeszékhelyek))

print('2#' * 55)
#Adjuk hozzá azokat a városokat amik hiányoznak
megyeszékhelyek['H'] = 'Eger'
megyeszékhelyek['BA'] = 'Pécs'
print(megyeszékhelyek)

print('3#' * 55)


#végigmegyek a megyék szótár kulcsain és kiíratom,
#hogy melyik megyének mi a rövidítése

for i in list(megyék):
    print(f"{i} megye rövidítése: {megyék[i]}")

print('4#' * 55)

#
for i, j in list(megyék.items()):
    print(f"{i} megye székhelye {megyeszékhelyek[j]}")
print(list(megyék.items()))

#Vas megye székhelyét rosszul írtam, kijavítom: töröl + hozzáad

print('5#' * 55)
del megyeszékhelyek['V']
megyeszékhelyek['V'] = 'Szombathely'
print(megyeszékhelyek)

print('6#' * 55)
print('Adj meg egy megyét, nagy kezdőbetűvel, és megnézem, mi a székhelye.')
i = input(">")

be = megyék.get(i)
if be:
    for j,k in list(megyék.items()):
        if j == i:
            print(f"{i} megye székhelye {megyeszékhelyek[k]}")
else:
    print(f"{i} megye nincs benne a listában.")
