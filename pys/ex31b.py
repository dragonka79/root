print("Csoki vagy saláta? Üss be 1-et ha a csokit, 2-t ha a salátát szereted.")
x = input("> ")
if x == "1":

    csoki = 100
    ropi = 50
    keksz = 150
    kcal = 2000

    print(f"A csokiban van {csoki} kCal,a ropiban van {ropi} kCal, \
a kekszben van {keksz} kCal.")

    print(f"Válogatsd úgy össze, hogy {kcal} kCal jöjjön ki, hány csokit, \
ropit és kekszet ehetek? Vigyázz, ha valamelyikből 8-nál többet \
választasz akkor torkos vagy.")

    print("Hány csoki?")
    csokidb = int(input())
    print("Hány ropi?")
    ropidb = int(input())
    print("Hány keksz?")
    kekszdb = int(input())

    if csokidb > 8 or ropidb > 8 or kekszdb > 8:
        print("Falánk vagy!")
    elif csokidb < 5 and ropidb < 5 and kekszdb < 5:
        print("Legyél kicsit merészebb!")
    else:
        print("Ez így korrekt!")

    sum = (csoki * csokidb) + (ropi * ropidb) + (keksz * kekszdb)
    diffa = kcal - sum
    diffb = -1 * diffa
    print(f"Ennyi az össz kalória: {sum}.")

    if kcal > sum:
        print(f"Kevés, {diffa} kalória még hiányzik.")
    elif kcal < sum:
        print(f"Sok, {diffb}-vel több.")
    else:
        print(f"Gratula, ez pont {kcal}.")

elif x == "2":
    print("Ez nem az a hely, itt az édességet preferáljuk.")
else:
    print("Szereted ezt is, azt is. Jó neked.")
