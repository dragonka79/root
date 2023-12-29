#a formatter változó definiálása, ami string
formatter = "{} {} {} {}"

# az 1,2,3,4 kinyomtatása a képernyőre. Mivel a formatterbe 4 változó lett
# belerakva, ezért 4 változó, string, int kell mindig bele
print(formatter.format(1, 2, 3, 4))
# a one, two, three, four kinyomtatása a képernyőre
print(formatter.format("one", "two", "three", "four"))
# a formatter változó értékének kinyomtatása 4-szer, szóközökkel elválasztva
print(formatter.format(formatter, formatter, formatter, formatter))
# 4 soros szöveg kiiratása egy sorba szóközökkel elválasztva
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
#ez is 4x írja ki a formatter értékét de nincs közöttük szóköz
print(formatter *4)

#ua mint a 11-ik sor
for _ in range(4):
    print(formatter, end=' ')
print('')

x = 3*2
print(formatter.format(x, "hello", 5*4, formatter))

#egymás alá 4 sorba írja ki a 4 soros szöveget
print(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear", sep='\n'
)

print('\n')

#ua mint 29
lista =["Try your","Own text here","Maybe a poem","Or a song about fear"]
for i in lista:
    print(i, end='\n')
print('')
#fordított sorrendben írva ki a 4 soros szöveget
print('\n')
for i in lista[::-1]:
    print(i, end='\n')
print('')


kiskutya = "l {} {} {}"

print(kiskutya.format(1, 2, 3, 4))
print(kiskutya.format("one", "two", "three", "four"))
print(kiskutya.format(True, False, False, True))
print(kiskutya.format(kiskutya, kiskutya, kiskutya.format(1, 2, 3, 4), kiskutya))
print(kiskutya.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
