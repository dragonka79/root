ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff = ten_things.split(' ')
print("Ten things", stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee","Corn", "Banana", "Girl", "Boy"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
print("There we go: ", stuff)
print("Let's do some things with stuff.")
print(more_stuff)
print("stuff első eleme (nem nulladik):", stuff[1])
print("stuff utolsó eleme:", stuff[-1])
print(stuff.pop()) # = print(stuff(pop(-1)))
#A stuff-ban lévő elemek közé szóközt rak, ez a split visszafele.
print(' '.join(stuff)) # what? cool!
#A stuff harmadik és negyedik eleme közé egy #-t rak.
print('#'.join(stuff[3:5]))#super stellar!
#A stuff harmadik eleme és a tőle ötödikre lévő elem közé #-t rak, ez a slice
print('#'.join(stuff[3::5]))# über super stellar!

#Sorba rendezem a stuff lista tagjait és belerakom egy másik listába
stuffsorted = sorted(stuff)
print(stuffsorted)
for i in stuffsorted:
    print(i)
