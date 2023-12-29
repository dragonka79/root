megyék = {
'Hajdú-Bihar' : 'HB',
'Szabolcs-Szatmár-Bereg': 'SZSZB',
'Békés':'B',
'Nógrád': 'N',
'Vas' : 'V'
}
print("A 'megyék' szótár nem sorba rendezve:\n", megyék)
print("\r")

#Szótár kulcs szerinti sorba rendezése

megyék_sorted = list(sorted(megyék.items()))
print("A 'megyék' szótár sorba rendezve:\n", megyék_sorted)
