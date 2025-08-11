

import turtle
import time
import random
import turtle
import threading
from playsound import playsound
import threading
import pygame
import copy

def draw_grid(my_turtle):
    my_turtle.pencolor("white")
    my_turtle.speed(0)
    my_turtle.hideturtle()
    for _ in range(3):
        my_turtle.penup()
        my_turtle.goto(N*-W/2, N*-W/2)
        my_turtle.pendown()
        my_turtle.pensize(5)
    for _ in range(4):
        my_turtle.forward(N*W)
        my_turtle.left(90)
    direction = 1
    for i in range(N):
        if i in range(0,10,3):
            my_turtle.pensize(3)
        else:
            my_turtle.pensize(1)
        my_turtle.forward(N * W)
        my_turtle.left(90* direction)
        my_turtle.forward(W)
        my_turtle.left(90* direction)
        direction *= -1



    direction = 1
    for i in range(N):
        if i in range(2,10,3):
            my_turtle.pensize(3)
        else:
            my_turtle.pensize(1)
        my_turtle.forward(W)
        my_turtle.left(90* direction)
        my_turtle.forward(N * W)
        direction *= -1
        my_turtle.left(90* direction)

written_cell= [[False for _ in range(9)] for _ in range(9)]
def fill_random(my_turtle , array, color):
    my_turtle.hideturtle()
    my_turtle.color(color)
    for r in range(9):
        for c in range(9):
            my_turtle.penup()
            my_turtle.goto(W * (-N/2 + 0.5 + r), W * (N/2 - 1 - c) )
            # -N * W / 2   + r * W + W  / 2 ,
            #  N * W / 2   - c * W - W / 1.5

            # #-N * W / 2 + r *W + W/2
            my_turtle.pendown()
            if array[r][c]!= 0 and not written_cell[r][c]:
                value= array[r][c]
                my_turtle.write(value, align="center", font=("Arial", 26, "normal"))

                written_cell[r][c] = True
            else:
                pass



def create_number_network():
    num_array = [[0 for r in range(N)] for c in range(N)]
    return num_array


def fill_network(array):
    for r in range(N):
        for c in range(N):
            if array[r][c] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(array, r, c , num) :
                        array[r][c] = num
                        if fill_network(array):
                            return True
                        array[r][c] = 0
                return False
    return True

def is_valid(array ,row, col, num):
        if num  in array[row]:
            return False
        if num  in [row[col] for row in array]:
            return False

        start_row = (row//3)*3
        start_col = (col//3)*3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if array[r][c] == num:
                    return False
        return True


def remove_number(array, n):
    removed=0
    while removed<n:
        r= random.randint(0,8)
        c= random.randint(0, 8)
        if array[r][c]!= 0:
            backup= array[r][c]
            array[r][c] = 0
            copy_arr = copy.deepcopy(array)
            if not fill_network(copy_arr):
                array[r][c]= backup
            else:
                removed +=1


def confetti_stream(screen, width, height, count_per_frame=5):
    screen.tracer(0)

    colors = ['#4362FF', '#F808B9']

    confettis = []

    start_time = time.time()
    duration = 20

    while time.time() - start_time < duration:
        for _ in range(count_per_frame):
            x = random.randint(-width//2, width//2)
            y = height // 2
            c = turtle.Turtle()
            c.hideturtle()
            c.penup()
            c.goto(x, y)
            c.color(random.choice(colors))
            c.shape("circle")
            c.shapesize(stretch_wid=0.3, stretch_len=0.3)
            c.showturtle()
            confettis.append(c)

        for c in confettis[:]:
            x, y = c.position()
            y -= random.uniform(3, 7)
            x += random.uniform(-3, 3)
            c.goto(x, y)

            if y < -height // 2:
                c.hideturtle()
                confettis.remove(c)

        screen.update()
        time.sleep(0.01)


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:/Users/Asus/Documents/Documents/Dayche/پایتون/Repo/ReStart/src/my exers/Handling.small.number.of.people(128).mp3")
    pygame.mixer.music.play()


if __name__ == '__main__':
    N = 9
    W = 40

    WIDTH = N * W + 800
    HEIGHT = N * W + 400
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor((0.2, 0.2, 0.2))
    turtle.bgcolor((0.2, 0.2, 0.2))

    my_array = create_number_network()
    fill_network(my_array)
    remove_number(my_array, 30)

    t1 = turtle.Turtle()
    draw_grid(t1)

    t2 = turtle.Turtle()
    fill_random(t2, my_array, 'white')
    fill_network(my_array)
    fill_random(t2, my_array, '#A7FF65')
    #
    threading.Thread(target=play_sound, daemon=True).start()
    time.sleep(0.5)
    confetti_stream(screen, WIDTH, HEIGHT)
    turtle.done()






