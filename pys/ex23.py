#A python moduláris felépítésű, a sys modul tartalmazza többek között a
#függvényeket
import sys

#A sys.argv egy lista amely parancssori argumentumokat ad vissza a python-nak.
#A script neve mindig az első, az index 0-ik helyen.
script, encoding, error = sys.argv

#A main nevű függvény definiálása, 3 argumentuma van.
def main(language_file, encoding, errors):
#A main nevű függvény a language_file-t soronként beolvassa.
    line = language_file.readline()
#Azt teszteli, hogy a line változónak van-e értéke, azaz az olvasott sorban
#van-e karakter. Fogdd így fel: 'if line' = 'if line = true'
    if line:
#A print_line nevű függvényt hívom meg (azért, hogy az adott sort kinyomtassa.)
        print_line(line, encoding, errors)
#Amíg nem kapok vissza üres sort a file-ból addig hívom meg a main függvényt,
#azaz így végiglépkedek soronként a language_file-on
        return main(language_file, encoding, errors)

#A print_line nevű függvény definiálása
def print_line(line, encoding, errors):
#A line string (azaz az éppen olvasott sor) végéről leszedi a sortörést és
#beleteszi egy next_lang változóba a teljes sort.
    next_lang = line.strip()
#raw_bytes =  numberical bytes in hexadecimal. Fogja az olvasott sort és
#átrakja, azaz enkódolja raw byte-sba és ezt belerakja egy raw_bytes változóba.
#Az errors=errors jelenti, hogy hogyan kezelje a hibákat, ezt nem értem.
    raw_bytes = next_lang.encode(encoding, errors=errors)
#A raw byte-okat visszadekódolom string-be, ennek egyeznie kell végül a
#next_lang sringgel.
    cooked_string = raw_bytes.decode(encoding, errors=errors)

#A raw byte-ok és a string kinyomtatása, elválasztva őket egy <====> jellel.
    print(raw_bytes, "<===>", cooked_string)

#A függvények definició immár készen vannak, most megnyitom a languages.txt
#file-t, utf-8-as (alapértelmezett) enkódolást használva.
languages = open("languages.txt", encoding="utf-8")

#A main függvény futtatása. Oda fog minden helyre ugrani, ahol a main függvény
#definiálva volt
main(languages, encoding, error)

#A magyar változat, amin jobban látszik, hogy mit miért csinál a program
print("\n" * 5)

import sys
script, enkódolás, hibák = sys.argv
def main (nyelvi_szöveg, enkódolás, hibák):
    sor = nyelvi_szöveg.readline()
    if sor:
        sornyomtat(sor,enkódolás, hibák)
        return main (nyelvi_szöveg, enkódolás, hibák)
def sornyomtat(sor, encoding, hibák):
    enter_nélküli_sor = sor.strip()
    nyers_byteok = enter_nélküli_sor.encode(encoding, errors=hibák)
    vissza_byteok_stringbe = nyers_byteok.decode(encoding, errors=hibák)
    print(nyers_byteok, "<====>", vissza_byteok_stringbe)
nyelvek = open("languages.txt")
main(nyelvek, enkódolás, hibák)
