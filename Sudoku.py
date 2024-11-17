import random


# Initialize a 9x9 grid with 0s (empty cells)
def create_empty_grid():
    return [[0 for _ in range(9)] for _ in range(9)]


# Check if placing `num` at grid[row][col] is valid
def is_valid(grid, row, col, num):
    # Check if `num` is in the same row
    if num in grid[row]:
        return False

    # Check if `num` is in the same column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # Check if `num` is in the same 3x3 sub-grid
    subgrid_row = (row // 3) * 3
    subgrid_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[subgrid_row + i][subgrid_col + j] == num:
                return False

    return True


# Function to find the next empty cell
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None


# Backtracking algorithm to fill the grid
def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True  # No empty cells left, solution found
    row, col = empty

    numbers = list(range(1, 10))
    random.shuffle(numbers)  # Shuffle numbers to randomize the grid

    for num in numbers:
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True  # Solution found, return True

            # If placing num didn't lead to a solution, reset the cell and backtrack
            grid[row][col] = 0

    return False  # Trigger backtracking


# Function to generate a complete, valid Sudoku grid
def generate_sudoku():
    grid = create_empty_grid()
    solve_sudoku(grid)
    return grid


# Generate and print a Sudoku grid
sudoku_grid = generate_sudoku()
for row in sudoku_grid:
    print(row)

import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Sudoku Table")
screen.setup(width=600, height=600)

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing speed

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

# Function to draw the Sudoku grid
def draw_sudoku_grid():
    pen.penup()
    pen.goto(-270, 270)  # Start from the top-left corner
    pen.pendown()

    for row in range(9):
        for col in range(9):
            draw_square(60)  # Each cell is 60x60 pixels
            pen.forward(60)
        pen.backward(540)  # Move back to the first column
        pen.right(90)
        pen.forward(60)  # Move down to the next row
        pen.left(90)

    # Draw the bold lines for 3x3 sub-grids
    pen.width(3)
    for i in range(4):
        pen.penup()
        pen.goto(-270, 270 - i * 180)  # Horizontal bold lines
        pen.pendown()
        pen.forward(540)

    pen.right(90)
    for i in range(4):
        pen.penup()
        pen.goto(-270 + i * 180, 270)  # Vertical bold lines
        pen.pendown()
        pen.forward(540)

# Function to write numbers into the Sudoku grid
def write_numbers(grid):
    pen.penup()
    start_x, start_y = -240, 240
    pen.goto(start_x, start_y)
    pen.hideturtle()

    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                pen.goto(start_x + col * 60, start_y - row * 60)
                pen.write(grid[row][col], align="center", font=("Arial", 20, "normal"))

# Call the function to draw the Sudoku grid
draw_sudoku_grid()

# Generate and write Sudoku numbers
write_numbers(sudoku_grid)

# Keep the window open
turtle.done()
