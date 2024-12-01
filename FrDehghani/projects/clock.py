import turtle
import math
import time

screen = turtle.Screen()
screen.setup(width=400, height=400)
screen.title("Faride Dehghani`s Analog Clock")
screen.bgcolor("lightyellow")

face_turtle = turtle.Turtle()
face_turtle.speed(0)
face_turtle.hideturtle()
face_turtle.penup()
face_turtle.goto(0, -120)
face_turtle.pendown()
face_turtle.pensize(10)
face_turtle.pencolor('lightblue')
face_turtle.circle(120)
turtle.speed(0)
turtle.tracer(0)
for num in range(1, 13):
    angles = 90 - num * (360 / 12)
    x = 100 * math.cos(math.radians(angles))
    y = 100 * math.sin(math.radians(angles))
    turtle.penup()
    turtle.goto(x+2, y-15)
    turtle.pendown()
    turtle.hideturtle()
    turtle.pencolor('blue')
    turtle.write(str(num), align="center", font=("Arial", 16, "bold"))

hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

for hand in [hour_hand, minute_hand, second_hand]:
    hand.hideturtle()
    hand.speed(0)
    # hand.shape("classic")


def draw_hand(turtle_obj, length, angle, color, pensize):
    turtle_obj.color(color)
    turtle_obj.pensize(pensize)
    turtle_obj.penup()
    turtle_obj.goto(0, 0)
    turtle_obj.setheading(angle)
    turtle_obj.pendown()
    turtle_obj.forward(length)


screen.tracer(0)  # Disable auto-update for manual control

try:
    while True:
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        hour_angle = 90 - (hours * 30 + minutes * 0.5)
        minute_angle = 90 - (minutes * 6)
        second_angle = 90 - (seconds * 6)

        hour_hand.clear()
        draw_hand(hour_hand, 50, hour_angle, "green", 5)

        minute_hand.clear()
        draw_hand(minute_hand, 70, minute_angle, "lightgreen", 3)

        if seconds == 0:
            second_hand.clear()
        else:
            second_hand.undo()

        draw_hand(second_hand, 90, second_angle, "red", 1)

        screen.update()
        time.sleep(1)
except turtle.Terminator:
    print('Dont close the Turtle graphics window!')
except Exception as e:
    print(f"An error occurred: {e}")
