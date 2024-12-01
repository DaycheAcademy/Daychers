import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Faride Dehghani`s Digital Clock")
screen.setup(width=300, height=300)

clock_turtle = turtle.Turtle()
clock_turtle.color("white")
clock_turtle.hideturtle()
clock_turtle.penup()
clock_turtle.goto(0, 0)

screen.tracer(0)
def update_clock():
    clock_turtle.clear()
    current_time = time.strftime("%H:%M:%S")
    clock_turtle.write(current_time, align="center", font=("Digital-7 Mono", 48, "normal"))
    screen.ontimer(update_clock, 1000)


update_clock()
turtle.done()
