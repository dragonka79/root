import turtle

color = str(input("Give me the color of the background of the window > "))
pensize = int(input("Give me the pensize of the turtle > "))

ablak = turtle.Screen()
ablak.bgcolor(color) # Állítsd be az ablak háttérszínét!
ablak.title("Hello, Eszti!") # Állítsd be az ablak címét!

Eszti = turtle.Turtle()
Eszti.color("blue") # Mond meg Esztinek, hogy változtasson színt!
Eszti.pensize(pensize) # Mond meg Esztinek, hogy változtassa meg a tolla vastagságát!
Eszti.forward(50)
Eszti.left(120)
Eszti.forward(50)

ablak.mainloop()