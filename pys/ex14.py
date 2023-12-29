from sys import argv

# Megadom, hogy 2 argumentum legyen. A script neve (ez mindig van, inkább
#ez a nulladik, a user_name pedig egy másik, amire bármilyen
#néven hivatkozhatok, pl zolcs, béla)
script, user_name, type = argv

#prompt = '> '
prompt = '!...!'

print(f"Hi {user_name} {type}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name} {type}?")

#Új sorba ugrik, megjeleníti a prompt értékét és várja a választ mert input,
#és a választ egy likes változóba rakja.
likes = input(prompt)

print(f"Where do you live {user_name} {type}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"How old are you {user_name}?")
age = input(prompt)

print(f"""
Allright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are {age} years old.
And you have a {computer} computer. Nice.
""")
