elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll"]
for utotag in utotagok_listaja:
    if elotag[-1] == utotag[0]:
        print(elotag + utotag[1:])
    else:
        print(elotag + utotag)
