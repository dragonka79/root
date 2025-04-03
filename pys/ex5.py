name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print (f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually taht's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair")
print(f"He's teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

print (f"Let's talk about", name, ".")
név = 'Dienes Zoltán'
kor = 42
print(f"Az én nevem {név} és {kor} éves vagyok.")

#convert inches to centimeters
inch = 5
centimeter = inch * 2.54
print(f"{inch} inch az {centimeter} centiméter.")
# convert pounds to kilograms

pound = 5
kilogram = 0.453592 * pound
print(f"{pound} font az {kilogram} kilogram.")

a1 = 15.453592
print(round(a1))
print(round(a1,3))
print(float(a1))
print(int(a1))
