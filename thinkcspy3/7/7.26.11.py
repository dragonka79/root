import turtle

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")
Zoli = turtle.Turtle()
Zoli.color("blue")
Zoli.pensize(3)
Zoli.speed(1)

path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for (spin, go) in path:
    Zoli.right(spin)
    Zoli.forward(go)

ablak.mainloop()

