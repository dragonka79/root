import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Gyönyörű minta")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(0)
# t.hideturtle()

def minta(sz):
    for i in range(1, 96):
        t.right(90)
        t.forward(i * sz)
    t.right(90)

sz = 4
minta(sz)
a.mainloop()