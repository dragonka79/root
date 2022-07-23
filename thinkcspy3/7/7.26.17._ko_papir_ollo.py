import random


folytat = 'y'
print("""Ez a kő-papír-olló játék a számítógép ellen.
        Kő = 1
        Papír = 2
        Olló = 3
        """)

gep = 0
user = 0
egal = 0
count = 0

while folytat != 'n':
    count += 1
    try:
        u = int(input("Kő, papír vagy olló ( 1 / 2 / 3 )?")) # user tipp
        if u in [1, 2, 3]:
            v = random.randrange(1, 4) # gép tipp
            if v != u:
                if (u == 1 and v == 3) or \
                    (u == 2 and v == 1) or \
                   (u == 3 and u == 2):
                    user += 1
                    print("Én nyertem.")
                else:
                    gep += 1
                    print("A gép nyert.")
            else:
                egal += 1
                print("Döntetlen")

            gep_nyert = round(((gep/count) * 100), 3)
            user_nyert = round(((user/count) * 100), 3)

            print(f"A gép tippje: {v} volt\n")
            print(f"""Az eddig állás:
                    gép nyert: {gep} alkalommal.
                    én nyertem:{user} alkalommal.
                    döntetlen: {egal} alkalommal.\n""")
            print(f"""Az eddigi nyerési arány:
                        gép nyert {gep_nyert} %-ban
                        én nyertem {user_nyert} %-ban\n""")

            folytat = input("Akarsz még játszani?(any key for 'yes'/ 'n' for no)")
            print('\n\a')
        else:
            print("Üss 1 / 2 / 3-at")
            continue
    except:
        print("Üss 1 / 2 / 3-at")
        continue

print("Köszönöm a játékot.\n")




