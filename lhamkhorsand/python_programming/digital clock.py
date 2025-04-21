import time
import turtle

clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
screen = turtle.Screen()
screen.title("Digital Clock")

def clock():
    clock_turtle.clear()
    current_time = time.strftime("%H:%M:%S")
    clock_turtle.write(current_time, align="center", font=("Arial", 100, "normal"))
    screen.ontimer(clock, 1000)

clock()
screen.mainloop()
