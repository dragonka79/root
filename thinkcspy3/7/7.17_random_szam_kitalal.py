import random # Beszélni fogunk a véletlen számokról...
szam = random.randrange(1, 1000) # véletlen szám [1 és 1000) intervallumban.

tippszam = 0
uzenet = ""

while True:
    tipp = int(input(
        uzenet + "\nTaláld ki az 1 és 1000 közötti számot,amire gondoltam: "
        ))
    tippszam += 1
    if tipp > szam:
        uzenet += str(tipp) + " túl nagy.\n" # DE MITŐL JELENIK MEG??
    elif tipp < szam:
        uzenet += str(tipp) + " túl kicsi.\n"
    else:
        break
input(f"\n\nNagyszerű, kitaláltad {tippszam} tipp segítségével!\n\n")