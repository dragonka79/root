import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Gyönyörű minta")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(0)
t.hideturtle()

def minta(sz):
    for i in range(2):
        for i in range(4):
            t.forward(sz)
            t.left(90)
        t.right(90)
    for i in range(4):
        t.forward(sz)
        t.right(90)
    for i in range(4):
        t.forward(sz)
        t.left(90)
    t.right(165)

sz = 150

for i in range(6):
    minta(sz)

a.mainloop()