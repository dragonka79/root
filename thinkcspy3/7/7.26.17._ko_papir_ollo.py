import random


folytat = 'y'
print("""Ez a kő-papír-olló játék a számítógép ellen.
        Kő = 1
        Papír = 0
        Olló = -1
        """)

gep = 0
user = 0
egal = 0

while folytat != 'n':
    try:
        u = int(input("Kő, papír vagy olló ( 1 / 0 /- 1 ?")) # user tipp
        if u in [1, 0, -1]:
            v = random.randrange(-1, 2) # gép tipp
            if v != u:
                if (u == 1 and v == -1) or (u == 0 and v == 1) or (u == -1 and u == -0):
                    user += 1
                    print("Én nyertem.")
                else:
                    gep += 1
                    print("A gép nyert.")
            else:
                egal += 1
                print("Döntetlen")
            print(f"A gép tippje: {v} volt")
            print(f"""Az eddig állás:
                    gép nyert: {gep} alkalommal.
                    én nyertem:{user} alkalommal.
                    döntetlen: {egal} alkalommal.""")

            folytat = input("Akarsz még játszani? (y/n)")
            print('\n\n')
    except:
        print("Üss 1/0/-1-et")
        continue

print("Köszönöm a játékot.")




