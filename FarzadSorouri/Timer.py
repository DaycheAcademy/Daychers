import time
import turtle
import math
screen = turtle.Screen()
myTurtle = turtle.Turtle()
circleTurtle = turtle.Turtle()
screen.setup(width=1000, height=600)
myTurtle.hideturtle()
myTurtle.pensize(3)
myTurtle.speed("fastest")
screen.tracer(0)
def draw_second_hand():
    # Get current time
    current_time = time.localtime()
    second = current_time.tm_sec

    # Calculate the angle for the second hand
    angle = 90 - (second * 6)

    # Move the turtle to the starting position
    secondCircleTurtle.penup()
    secondCircleTurtle.goto(250, 110)  # Go to the center
    secondCircleTurtle.setheading(angle)
    secondCircleTurtle.pendown()
    secondCircleTurtle.forward(100)  # Draw the hand

    # Hide the turtle immediately after drawing
    secondCircleTurtle.penup()
    secondCircleTurtle.backward(100)  # Return to center


while True:
    myTurtle.penup()
    myTurtle.clear()


    myTurtle.goto(-150,100)
    myTurtle.pendown()

    myTurtle.forward(150)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.forward(150)
    myTurtle.left(90)
    myTurtle.forward(50)
    myTurtle.left(90)
    myTurtle.write(time.strftime("%H:%M:%S"),font=("Arial", 26, "normal"))
    #------------------------------------------
    circleTurtle.penup()
    circleTurtle.hideturtle()
    circleTurtle.pensize(3)
    circleTurtle.goto(250,10)
    circleTurtle.pendown()
    circleTurtle.circle(100)
    circleTurtle.penup()

    for i in range(1, 13):
        # Calculate the angle for each number
        angle = i * -30 + 90

        # Calculate x, y coordinates based on polar coordinates
        x = 90 * math.cos(math.radians(angle)) + 250  # Circle radius 100, center at (250, 100)
        y = 90 * math.sin(math.radians(angle)) + 100
        circleTurtle.goto(x, y)
        circleTurtle.write(str(i), align="center", font=("Arial", 14, "normal"))
    screen.update()
#---------------------------secondCircleTurtle----------------------------------------------------

    secondCircleTurtle=turtle.Turtle()
    current_time = time.localtime()
    hour = current_time.tm_hour
    second = current_time.tm_sec
    minute = current_time.tm_min
    secondCircleTurtle.color('red')
    secondCircleTurtle.width(2)
    angle = 90 - (second * 6)
    secondCircleTurtle.clear()
    # Move the turtle to the starting position
    secondCircleTurtle.penup()
    secondCircleTurtle.goto(250, 110)  # Go to the center
    secondCircleTurtle.setheading(angle)
    secondCircleTurtle.pendown()
    secondCircleTurtle.forward(100)  # Draw the hand

    # Hide the turtle immediately after drawing
    secondCircleTurtle.penup()
    secondCircleTurtle.backward(100)  # Return to center

    screen.update()
    secondCircleTurtle.clear()
 # ---------------------------minuteCircleTurtle----------------------------------------------------

    minuteCircleTurtle = turtle.Turtle()
    minuteCircleTurtle.color('blue')
    minuteCircleTurtle.width(2)

    angleMinute = 90 - (minute * 6.1)
    minuteCircleTurtle.clear()
    # Move the turtle to the starting position
    minuteCircleTurtle.penup()
    minuteCircleTurtle.goto(250, 110)  # Go to the center
    minuteCircleTurtle.setheading(angleMinute)
    minuteCircleTurtle.pendown()
    minuteCircleTurtle.forward(100)  # Draw the hand

    # Hide the turtle immediately after drawing
    minuteCircleTurtle.penup()
    minuteCircleTurtle.backward(100)  # Return to center

    # ---------------------------hourCircleTurtle----------------------------------------------------

    hourCircleTurtle = turtle.Turtle()
    hourCircleTurtle.color('green')
    hourCircleTurtle.width(2)

    angleMinute = 90 - (hour * 33.5)
    hourCircleTurtle.clear()
    # Move the turtle to the starting position
    hourCircleTurtle.penup()
    hourCircleTurtle.goto(250, 110)  # Go to the center
    hourCircleTurtle.setheading(angleMinute)
    hourCircleTurtle.pendown()
    hourCircleTurtle.forward(100)  # Draw the hand

    # Hide the turtle immediately after drawing
    hourCircleTurtle.penup()
    hourCircleTurtle.backward(100)  # Return to center

    time.sleep(1)

    # minuteCircleTurtle.hideturtle()

turtle.done()