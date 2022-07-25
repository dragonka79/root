elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltő", "papa", "picur", "szakáll" ]
for utotag in utotagok_listaja:
    if elotag[-1] != utotag[0]:
        print(elotag + utotag)
    else:
        print(elotag + utotag[1:])