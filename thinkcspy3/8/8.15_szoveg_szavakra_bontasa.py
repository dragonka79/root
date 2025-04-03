import string

"""Egy szöveget szavakra bont"""

def irasjel_eltavolitas(szoveg):
    """Kiszedi a nem írásjeleket a szövegből"""
    irasjel_nelkuli = ""
    for karakter in szoveg:
        if karakter not in string.punctuation:
            irasjel_nelkuli += karakter
    return irasjel_nelkuli

a_tortenetem = """
A pitonok nem méreggel ölnek, hanem kiszorítják a szuszt az áldozatukból.
A prédájuk köré tekerik magukat, minden egyes lélegzeténél egy kicsit
szorosabban, egészen addig, amíg a légzése abba nem marad. Amint megáll
a zsákmány szíve, lenyelik az egészet. A bunda és a tollazat kivételével
az egész állat a kígyó gyomrába lesz temetve. Mit gondolsz, mi történik
a lenyelt bundával, tollakkal, csőrökkel és tojáshéjakkal? A felesleges
'dolgok' távoznak, -- jól gondolod -- kígyó ÜRÜLÉK lesz belőlük!"""

szavak = irasjel_eltavolitas(a_tortenetem).split()
print(szavak)