import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)
t.speed(1)
t.hideturtle()


def star(n):
    t.left(36)
    for i in range(5):
        t.forward(n)
        t.left(144)

star(100)

a.mainloop()