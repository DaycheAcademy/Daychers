# without lifting the pen (penup-goto-pendown)
import pytz
import datetime
import time
import turtle

# turtle.speed(0)

turtle.pencolor("white")

turtle.backward(250)
turtle.left(90)
turtle.backward(250)

turtle.pencolor("black")
turtle.pensize(3)

for i in range(4):
    turtle.forward(540)
    turtle.right(90)

turtle.forward(180)
turtle.right(90)
for i in range(4):
    for j in range(2):
        turtle.forward(180)
        turtle.left(90)
    for k in range(3):
        turtle.forward(180)
        turtle.right(90)

turtle.pensize(1)

turtle.left(90)

turtle.backward(180)
for i in range(4):
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(540)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(540)
    turtle.right(90)

turtle.forward(60)
turtle.right(90)
for i in range(4):
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(540)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(540)
    turtle.right(90)

turtle.done()


#  Another solution using penup-goto-pendown


# import turtle
#
# def draw_grid():
#     turtle.speed(0)
#     turtle.pensize(5)
#
#     turtle.penup()
#     turtle.goto(-270, 270)
#     turtle.pendown()
#     for _ in range(4):
#         turtle.forward(540)
#         turtle.right(90)
#
#     turtle.pensize(2)
#
#     for i in range(1, 9):
#
#         if i % 3 == 0:
#             turtle.pensize(4)
#         else:
#             turtle.pensize(1)
#
#         turtle.penup()
#         turtle.goto(-270 + i * 60, 270)
#         turtle.pendown()
#         turtle.goto(-270 + i * 60, -270)
#
#         turtle.penup()
#         turtle.goto(-270, 270 - i * 60)
#         turtle.pendown()
#         turtle.goto(270, 270 - i * 60)
#
#     turtle.done()
#
# draw_grid()
