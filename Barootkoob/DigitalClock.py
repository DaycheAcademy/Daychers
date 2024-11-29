import turtle
import time

# Set up the turtle window
window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=300)
window.title("Digital Clock")
window.tracer(0)

# Create the turtle to draw the clock
clock_turtle = turtle.Turtle()
clock_turtle.hideturtle()
clock_turtle.color("white")
clock_turtle.goto(0, 0)
clock_turtle.speed(0)

# Main loop to keep updating the time
while True:
    clock_turtle.clear()  # Clear the previous time (use the turtle object here)
    TehranTime = time.localtime()  # Get the local time (Tehran's time if your system is set to that timezone)

    # Format the time as HH:MM:SS
    current_time = f"{TehranTime.tm_hour:02}:{TehranTime.tm_min:02}:{TehranTime.tm_sec:02}"

    # Display the time on the screen
    clock_turtle.write(current_time, align="center", font=("Arial", 50, "bold"))
    window.update()
    time.sleep(1)  # Pause for 1 second before updating again



