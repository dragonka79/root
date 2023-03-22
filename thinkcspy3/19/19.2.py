
# Creation of unique exception

def ev_keres():
    ev = int(input("Please give me your age > "))
    if ev < 0:
        sajat_hiba = ValueError("{0} not a valid number for age.".format(ev))
        raise sajat_hiba
    return ev

print(ev_keres())