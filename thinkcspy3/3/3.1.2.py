import turtle

color = str(input("Give me the color of the background of the window > "))
pencolor = str(input("Give me the pencolor of the turtle > "))

ablak = turtle.Screen()
ablak.bgcolor(color) # Állítsd be az ablak háttérszínét!
ablak.title("Hello, Eszti!") # Állítsd be az ablak címét!

Eszti = turtle.Turtle()
Eszti.color(pencolor) # Mond meg Esztinek, hogy változtasson színt!
Eszti.pensize(3) # Mond meg Esztinek, hogy változtassa meg a tolla vastagságát!
Eszti.forward(50)
Eszti.left(120)
Eszti.forward(50)

ablak.mainloop()