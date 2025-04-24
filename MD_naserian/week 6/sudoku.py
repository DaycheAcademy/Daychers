##### RULES #####
# 1.outer line : 5
# 2.3*3 lines : 3
# 3.other lines: 1
# 4.hide turtle
# 5.highest speed
import turtle


drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.goto(-450, 450)
drawer.speed(speed=0)
drawer.pendown()


# 1.outer line : 5
out = 900
for _ in range(4):
    drawer.pensize(5)
    drawer.forward(out)
    drawer.right(90)


# 2. vertical lines 3*3 lines : 3
angle = 90
for i in range(1, 9):
    if i % 3==0:
        drawer.pensize(3)
        drawer.forward(out/8)
    else:
        drawer.pensize(1)
        drawer.forward(out/8)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(angle)
    drawer.right(angle)
    angle *=-1


# 2. horizental lines 3*3 lines : 3
drawer.setheading(-90)


for i in range(1, 9):
    if i % 3==0:
        drawer.pensize(3)
        drawer.forward(out/8)
    else:
        drawer.pensize(1)
        drawer.forward(out/8)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(-90)
    angle *=-1












turtle.done()