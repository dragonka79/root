import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("deeppink")
t.pensize(3)


def square(h):
    for i in range(4):
        t.forward(h)
        t.left(90)
    t.penup()
    t.forward(2 * h)
    t.pendown()

for i in range(5):
    square(20)

a.mainloop()