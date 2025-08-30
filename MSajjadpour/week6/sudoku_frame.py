import turtle
import random

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

# Create a valid Sudoku solution
sudoku_board = [[0 for _ in range(9)] for _ in range(9)]

# Fill the diagonal 3x3 boxes
for box in range(3):
    numbers = list(range(1, 10))
    random.shuffle(numbers)

    for i in range(3):
        for j in range(3):
            row = box * 3 + i
            col = box * 3 + j
            sudoku_board[row][col] = numbers[i * 3 + j]


# Solve the rest of the Sudoku using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # Randomize the order of numbers

                for num in numbers:
                    # Check if the number is valid in this position
                    valid = True

                    # Check row
                    for c in range(9):
                        if board[row][c] == num:
                            valid = False
                            break

                    # Check column
                    if valid:
                        for r in range(9):
                            if board[r][col] == num:
                                valid = False
                                break

                    # Check 3x3 box
                    if valid:
                        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
                        for r in range(3):
                            for c in range(3):
                                if board[start_row + r][start_col + c] == num:
                                    valid = False
                                    break

                    if valid:
                        board[row][col] = num

                        # Recursively try to solve the rest
                        if solve_sudoku(board):
                            return True

                        # If not valid, backtrack
                        board[row][col] = 0

                return False

    return True


# Solve the Sudoku
solve_sudoku(sudoku_board)

# Display numbers in grid cells
pen.penup()
for i in range(9):
    for j in range(9):
        x = start_x + j * cell_size + cell_size / 3
        y = start_y - i * cell_size - cell_size * 2 / 3
        pen.goto(x, y)
        pen.write(sudoku_board[i][j], align="center", font=("Arial", 14, "normal"))

# Keep window open
turtle.done()