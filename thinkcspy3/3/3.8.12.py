import turtle

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

Zoli = turtle.Turtle()
Zoli.color("blue")
Zoli.shape("turtle")
Zoli.pensize(3)
Zoli.speed(3)

Zoli.stamp()
Zoli.penup()
Zoli.left(90)

for i in range(12):
    Zoli.forward(100)
    Zoli.pendown()
    Zoli.forward(10)
    Zoli.penup()
    Zoli.forward(20)
    Zoli.pendown()
    Zoli.stamp()
    Zoli.penup()
    Zoli.backward(130)
    Zoli.right(30)

Zoli.right(90)
ablak.mainloop()
