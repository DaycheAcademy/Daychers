import turtle
import time
import math



surface = turtle.Turtle()
numbers = turtle.Turtle()
seconds = turtle.Turtle()
minutes = turtle.Turtle()
hours = turtle.Turtle()




surface.speed(0)
surface.goto(0,0)
surface.dot(20,"violet")
surface.color("white")
surface.goto(0,-100)



numbers.speed(6)
numbers.penup()
numbers.goto(0,100)

numbers.penup()

for i in range(0,361,30) :

    if i != 0 :
        numbers.goto(0,0)
        numbers.setheading(i)
        numbers.goto(    110*( math.sin(i*math.pi/180) )  ,  110*( math.cos(i*math.pi/180) )     )
        # numbers.write( abs( (-i + 90)/12 ) )
        numbers.write( i/30 ,font = 1)
        # numbers.write("*")
        numbers.penup()

numbers.hideturtle()
surface.hideturtle()


seconds.pensize(3)
seconds.speed(0)
seconds.hideturtle()

minutes.pensize(5)
minutes.speed(0)
minutes.hideturtle()

hours.pensize(7)
hours.speed(0)
hours.hideturtle()



seconds.color("white")
seconds.goto(0,0)
seconds.left(90)

minutes.color("white")
minutes.goto(0,0)
minutes.left(90)

hours.color("white")
hours.goto(0,0)
hours.left(90)

tehranTime = time.localtime()
while (True) :
    turtle.hideturtle()
    # turtle.clear()
    # turtle.update()

    seconds.speed(0)
    seconds.color("blue")
    seconds.setheading(-6 * tehranTime.tm_sec + 90)
    seconds.forward(85)
    seconds.color("white")
    seconds.goto(0, 0)

    if tehranTime.tm_sec > 58 :
        minutes.color("yellow")
        minutes.setheading(-6 * tehranTime.tm_min + 90)
        minutes.forward(75)
        minutes.color("white")
        minutes.goto(0, 0)
    if tehranTime.tm_sec <= 58 :
        minutes.color("yellow")
        minutes.setheading(-6 * tehranTime.tm_min + 90)
        minutes.forward(75)
        minutes.goto(0, 0)

    adding_minute_to_hour = (-6 * tehranTime.tm_min + 90)/12
    hours.color("orange")
    hours.setheading(-30 * tehranTime.tm_hour  + 90  + adding_minute_to_hour )
    hours.forward(65)
    hours.goto(0, 0)


    surface.goto(0,0)
    surface.dot(20, "violet")

    tehranTime = time.localtime()

    time.sleep(0.1)
turtle.done()

