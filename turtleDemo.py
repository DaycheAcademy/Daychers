import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.goto(0, 0)
for _ in range(4):
    turtle.pensize(5)
    turtle.forward(180)
    turtle.left(90)

turtle.pensize(3)
turtle.teleport(60, y=0, fill_gap=False)
turtle.left(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(180)
turtle.teleport(0, y=60, fill_gap=False)
turtle.left(90)
turtle.forward(180)
turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.forward(180)

turtle.pensize(1)
turtle.teleport(0, y=0, fill_gap=False)

for _ in range(4):
    turtle.forward(-20)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(-20)
    turtle.left(90)
    turtle.forward(180)
    turtle.right(90)

turtle.pensize(1)
turtle.teleport(0, y=0, fill_gap=False)

for _ in range(4):
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(180)





turtle.done()





