import turtle

ablak = turtle.Screen()
ablak.bgcolor("orange")

Zoli = turtle.Turtle()
Zoli.color("green")
Zoli.pensize(4)
# Zoli.speed(1)


for i in range(3):
    Zoli.forward(100)
    Zoli.left(120)


Zoli.penup()
Zoli.forward(150)
Zoli.color("blue")
Zoli.pendown()

for i in range(4):
    Zoli.forward(100)
    Zoli.left(90)

Zoli.penup()
Zoli.right(90)
Zoli.forward(150)
Zoli.color("red")
Zoli.pendown()

for i in range(6):
    Zoli.forward(100)
    Zoli.right(60)


Zoli.penup()
Zoli.right(135)
Zoli.forward(300)
Zoli.color("brown")
Zoli.pendown()

for i in range(8):
    Zoli.forward(100)
    Zoli.left(45)


ablak.mainloop()
