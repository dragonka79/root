def állatok_az_udvaron(csirkék, kacsák, gyöngytyúkok):
    print(f"Nekünk {csirkék} csirke futkároz az udvaron.")
    print(f"Van még {kacsák} kacsa is.")
    print(f"Ne felejtsük el a {gyöngytyúkok} gyöngytyúkot sem.")
    print(f"Cej, ezekből jól lehetne lakatni egy násznépet \n")

print(f"Meg tudom neked adni, hogy hányan állatunk van.")
állatok_az_udvaron(20,15,10)

print(f"Vagy tudom a darabszámokat nem direkt hanem változókkal is kifejezni")
csirkék = 40
kacsák = 17
gyöngytyúkok = 13

állatok_az_udvaron(csirkék, kacsák, gyöngytyúkok)

print(f"Vagy akár darabokban is meg tudom őket számolni")

állatok_az_udvaron(14 + 19, 5 + 8, 12 + 8)

print (f"Vagy akár hozzá is tudom adni a változókhoz a darabszámokat")
állatok_az_udvaron(csirkék + 5, kacsák -3, gyöngytyúkok + 4)

csirkék = input(f"Te hány csirkét számoltál?\ncsirkék>")
kacsák = input(f"Te hány kacsát számoltál? \nkacsák>")
gyöngytyúkok = input(f"Te hány gyöngytyúkot számoltál?\ngyöngytyúkok>")
állatok_az_udvaron(csirkék, kacsák, gyöngytyúkok)
