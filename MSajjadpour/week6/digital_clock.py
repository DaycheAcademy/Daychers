import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Digital Clock")
screen.bgcolor("black")
screen.setup(width=600, height=200)

# Create turtle object for displaying time
digital_clock = turtle.Turtle()
digital_clock.hideturtle()
digital_clock.color("green")
digital_clock.penup()

# Infinite loop to update time
while True:
    # Clear previous display
    digital_clock.clear()

    # Get current time
    current_time = time.strftime("%H:%M:%S")

    # Display time
    digital_clock.goto(0, 0)
    digital_clock.write(current_time, align="center", font=("Courier", 48, "bold"))

    # Update screen
    screen.update()

    # Wait for 1 second
    time.sleep(1)
