import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("9x9 Sudoku Grid")

# Create a turtle for drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)  # Fastest speed

# Define dimensions
cell_size = 40
grid_size = 9 * cell_size
start_x = -grid_size / 2
start_y = grid_size / 2

# Draw the outer box with thickness 5
pen.pensize(5)
pen.penup()
pen.goto(start_x, start_y)
pen.pendown()
pen.goto(start_x + grid_size, start_y)  # Top
pen.goto(start_x + grid_size, start_y - grid_size)  # Right
pen.goto(start_x, start_y - grid_size)  # Bottom
pen.goto(start_x, start_y)  # Left
pen.penup()

# Draw the grid lines
for i in range(1, 9):
    # Determine line thickness
    if i % 3 == 0:
        thickness = 3
    else:
        thickness = 1

    # Vertical lines
    x = start_x + i * cell_size
    pen.pensize(thickness)
    pen.penup()
    pen.goto(x, start_y)
    pen.pendown()
    pen.goto(x, start_y - grid_size)
    pen.penup()

    # Horizontal lines
    y = start_y - i * cell_size
    pen.pensize(thickness)
    pen.penup()
    pen.goto(start_x, y)
    pen.pendown()
    pen.goto(start_x + grid_size, y)
    pen.penup()

# Keep the window open
turtle.done()
