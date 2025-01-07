import turtle, time

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=300)
screen.title("Digital Clock")
screen.title("Digital Clock")
screen.bgcolor("black")

# Configure the turtle for writing the clock
turtle.color("white")
turtle.ht()
turtle.speed(0)

while True:
    turtle.tracer(0)
    turtle.clear()
    tehranTime = time.localtime()
    turtle.write(f"{tehranTime.tm_hour:02}:{tehranTime.tm_min:02}:{tehranTime.tm_sec:02}",
                 align="center", font=("Arial", 24, "bold"))
    turtle.update()
