hallgatok = [
("Jani", ["Informatika", "Fizika"]),
("Kata", ["Matematika", "Informatika", "Statisztika"]),
("Peti", ["Informatika", "Könyvelés", "Közgazdaságtan", "Menedzsment"]),
("Andi", ["Információs rendszerek", "Könyvelés", "Közgazdaságtan", "Vállalkozási jog"]),
("Linda", ["Szociológia", "Közgazdaságtan", "Jogi ismeretek", "Statisztika", "Zene"])]



def inf_targy_hallgatok(hallgatok):
    """Az Informatika tárgyat hallgatók száma"""
    inf = 0
    for (nev, targyak) in hallgatok:
        for i in targyak:
            if i.lower() == "informatika":
                inf += 1
    return(inf)

print(inf_targy_hallgatok(hallgatok))
