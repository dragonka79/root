# Fedőnevek és másolás

ellentetek = {"fel": "le", "jó": "rossz", "igen": "nem"}
alnev = ellentetek
masolat = ellentetek.copy() # Felszínes másolás

# Módosítás változtat minden fedőnévben, de a másolatban nem.

# alnev["jó"] = "hibás"
# print(alnev["jó"])
# print(ellentetek["jó"])
# print(masolat["jó"])


ellentetek["jó"] = "hibás"
print(ellentetek["jó"])
print(alnev["jó"])
print(masolat["jó"])