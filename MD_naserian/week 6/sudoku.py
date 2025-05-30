##### RULES #####
# 1.outer line : 5
# 2.3*3 lines : 3
# 3.other lines: 1
# 4.hide turtle
# 5.highest speed
# 6.fill sudoku


import turtle
import random
screen = turtle.Screen()
screen.setup(height=600, width=600)

out = 550

drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()
drawer.goto(-out/2, out/2)
drawer.speed(speed=0)
drawer.pendown()


# 1.outer line : 5
for _ in range(4):
    drawer.pensize(5)
    drawer.forward(out)
    drawer.right(90)


# 2. vertical lines 3*3 lines : 3
angle = 90
for i in range(1, 9):
    if i % 3==0:
        drawer.pensize(3)
        drawer.forward(out/9)
    else:
        drawer.pensize(1)
        drawer.forward(out/9)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(angle)
    drawer.right(angle)
    angle *=-1




# 2. horizental lines 3*3 lines : 3
drawer.forward(out/9)
drawer.setheading(-90)


for i in range(1,9):
    if i % 3==0:
        drawer.pensize(3)
        drawer.forward(out/9)
    else:
        drawer.pensize(1)
        drawer.forward(out/9)

    drawer.right(angle)
    drawer.forward(out)
    drawer.setheading(-90)
    angle *=-1


# inserting the default numbers:(unique for rows:) but not for columns:( )

# y = (out/2)+(out*.044)
# for j in range(9):
#     x_base  = -(out/2)+(.11*(out/2))
#     y -=out/9
#     numbers = random.sample(range(1, 10), k=5)
#     filled_positions = random.sample(range(9), k=5)
#     for pos, num in zip(filled_positions, numbers):
#         turtle.penup()
#         turtle.hideturtle()
#         x = x_base + pos * (out/9)
#         turtle.goto(x, y)
#         turtle.speed(0)
#         turtle.write(num,  font=("courier", 18, "bold"))
#solution by ai:

# ... (keep all previous code for drawing the grid)

# MODIFIED NUMBER INSERTION SECTION
columns_used = [set() for _ in range(9)]  # Track used numbers in each column
y = (out/2)+(out*.044)

for j in range(9):
    x_base = -(out/2)+(.11*(out/2))
    y -= out/9
    
    # Generate 5 random positions
    filled_positions = random.sample(range(9), k=5)
    valid_numbers = []
    valid_positions = []
    
    # Shuffle positions to reduce conflict chances
    random.shuffle(filled_positions)
    
    for pos in filled_positions:
        # Get available numbers for this cell
        available = set(range(1,10)) - columns_used[pos]
        
        # Remove numbers already chosen for this row
        available -= set(valid_numbers)
        
        if available:
            chosen = random.choice(list(available))
            valid_numbers.append(chosen)
            valid_positions.append(pos)
            columns_used[pos].add(chosen)
    
    # Write valid numbers to grid
    for pos, num in zip(valid_positions, valid_numbers):
        x = x_base + pos * (out/9)
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(num, font=("courier", 18, "bold"))

# ... (keep rest of the code for user input handling)

    
#insert numbers by user:

def add_number(x, y):
    text = turtle.textinput(title="insert your number", prompt="can't be reptited")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.color("red")
    turtle.write(text,  font=("courier", 24, "bold"))


# try to find X and Y
# def btnclick(x, y):
#     turtle.clear()
#     turtle.hideturtle()
#     text = f"x = {x}, y = {y}\n"
#     turtle.write(text, align="center", font=("courier", 18, "normal"))
#     with open("MD_naserian\\week 6\\location.txt", "a") as f:
#         f.write(text)
    


turtle.onscreenclick(add_number, 1)
# turtle.onscreenclick(btnclick, 1)
turtle.listen()
turtle.mainloop()