types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not ="don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w +e)

érez = 'Jól'
igaz = True
hogyan = "Hogyan érzed most magad? {}"
print(hogyan.format(érez))
print(hogyan.format(igaz))


kilo = 65.5
z = f"{kilo} kiló vagyok most."
zz = f"Azt mondtam, hogy {z}"
print(zz)

fal = 'fehér'
milyen = "Milyen szinű a fal? {}"
print(milyen.format(fal))
