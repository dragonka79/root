import turtle

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Gyönyörű minta")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(0)
# t.hideturtle()

angle = 89
def minta(sz):
    for i in range(1, 96):
        t.right(angle)
        t.forward(i * sz)
    t.right(angle)

sz = 4
minta(sz)
a.mainloop()