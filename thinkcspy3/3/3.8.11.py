import turtle

ablak = turtle.Screen()
Zoli = turtle.Turtle()
Zoli.pensize(3)
Zoli.speed(2)
Zoli.right(72)
Zoli.hideturtle()

for i in range(5):
    Zoli.forward(300)
    Zoli.right(144)

Zoli.showturtle()
ablak.mainloop()