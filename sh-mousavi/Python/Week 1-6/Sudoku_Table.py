import turtle

turtle.hideturtle()
turtle.speed("fastest")

# turtle.penup()
# turtle.goto(-135,135)
# turtle.pendown()
turtle.teleport(-135, 135)

turtle.pensize(5)
for _ in range(4):
    turtle.forward(270)
    turtle.right(90)

gridLines = [(3, 90), (1, 30), (1, 60), (1, 120)]

for item in gridLines:
    turtle.pensize(item[0])
    for _ in range(4):
        turtle.penup()
        turtle.forward(item[1])
        turtle.right(90)
        turtle.pendown()
        turtle.forward(270)
        turtle.right(90)
        turtle.penup()
        turtle.forward(item[1])
        turtle.right(90)

turtle.done()
