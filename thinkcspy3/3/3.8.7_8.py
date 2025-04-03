import turtle

spins = [160, -43, 270, -97, -43, 200, -940, 17, -86]

ablak = turtle.Screen()
ablak.bgcolor("red")

Zoli = turtle.Turtle()
Zoli.color("green")
Zoli.pensize(4)

angle = 0
for i in spins:
    Zoli.forward(100)
    Zoli.left(i)
    angle += i

print(angle % 360)
ablak.mainloop()