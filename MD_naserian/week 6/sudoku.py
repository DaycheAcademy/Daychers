##### RULES #####
# 1.outer line : 5
# 2.3*3 lines : 3
# 3.other lines: 1
# 4.hide turtle
# 5.highest speed
# 6.fill sudoku
import turtle
import random


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
        drawer.forward(out/9)
    else:
        drawer.pensize(1)
        drawer.forward(out/9)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(angle)
    drawer.right(angle)
    angle *=-1




# 2. horizental lines 3*3 lines : 3
drawer.forward(out/9)
drawer.setheading(-90)


for i in range(1,9):
    if i % 3==0:
        drawer.pensize(3)
        drawer.forward(out/9)
    else:
        drawer.pensize(1)
        drawer.forward(out/9)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(-90)
    angle *=-1


# inserting the numbers:

y = 470
for j in range(9):
    x_base  = -400
    y -=100
    numbers = random.sample(range(1, 10), k=5)
    filled_positions = random.sample(range(9), k=5)
    for pos, num in zip(filled_positions, numbers):
        turtle.penup()
        turtle.hideturtle()
        x = x_base + pos * 100
        turtle.goto(x, y)
        turtle.speed(0)
        turtle.write(num,  font=("courier", 24, "bold"))
        
    



# try to find X and Y
def btnclick(x, y):
    turtle.clear()
    turtle.hideturtle()
    text = f"x = {x}, y = {y}\n"
    turtle.write(text, align="center", font=("courier", 18, "normal"))
    with open("MD_naserian\\week 6\\location.txt", "a") as f:
        f.write(text)
    



turtle.onscreenclick(btnclick, 1)
turtle.listen()
turtle.mainloop()