import turtle


def hori(b):
    for i in range(int(b)):
        turtle.forward(180)
        turtle.penup()
        turtle.goto(0, -20*(i+1))
        turtle.pendown()


for i in range(9):
    turtle.penup()
    turtle.goto(0, -20*i)
    turtle.pendown()
    hori(1)

turtle.right(90)
turtle.penup()
turtle.goto(0, 0)

for i in range(9):
    turtle.penup()
    turtle.goto(20*i, 0)
    turtle.pendown()
    hori(1)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(5)

for i in range(4):
    turtle.forward(180)
    turtle.left(90)

turtle.penup()
turtle.goto(60, 0)
turtle.pensize(3)

for i in range(2):

    turtle.goto(60 * (i + 1), 0)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()

turtle.left(90)
turtle.penup()

for i in range(2):

    turtle.goto(0, -60 * (i + 1))
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()

turtle.done()

