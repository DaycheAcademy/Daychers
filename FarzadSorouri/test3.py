import turtle

screen = turtle.Screen()
screen.setup(width=1000, height=600)
# Loop for First Layer
myTurtleMain = turtle.Turtle()
layer1=360
myTurtleMain.penup()
myTurtleMain.goto(-160, 220)
myTurtleMain.pendown()
myTurtleMain.pensize(5)
myTurtleMain.speed('fastest')  # 0 is the fastest speed
# Draw a square
for _ in range(4):
    myTurtleMain.forward(layer1)
    myTurtleMain.right(90)

myTurtleMain.hideturtle()  # Hide the turtle after drawing
#================================================================
# Loop for second row
layer2 = 120
myTurtleLayer2 = turtle.Turtle()
for lc2 in range(3):
    for shapCount2 in range(1, 4):

        myTurtleLayer2.penup()
        myTurtleLayer2.goto(120 * shapCount2-280, 120*lc2-20)
        myTurtleLayer2.pendown()
        myTurtleLayer2.pensize(3)
        myTurtleLayer2.speed('fastest')  # 0 is the fastest speed

        # Draw a square
        for _ in range(4):
            myTurtleLayer2.forward(layer2)
            myTurtleLayer2.right(90)

        myTurtleLayer2.hideturtle()  # Hide the turtle after drawing
#================================================================
# Loop for Third row
layer3 = 40
myTurtleLayer3 = turtle.Turtle()
for lc in range(9):
    for shapCount in range(1, 10):

        myTurtleLayer3.penup()
        myTurtleLayer3.goto(40 * shapCount-200, 40*lc-100)
        myTurtleLayer3.pendown()
        myTurtleLayer3.pensize(1)
        myTurtleLayer3.speed('fastest')  # 0 is the fastest speed

        # Draw a square
        for _ in range(4):
            myTurtleLayer3.forward(layer3)
            myTurtleLayer3.right(90)

        myTurtleLayer3.hideturtle()  # Hide the turtle after drawing

turtle.done()